#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x

import json
import os
import sys

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError, NotFoundError
from elasticsearch.helpers import bulk


class ErrorHunter(object):
    @staticmethod
    def capture_connection_error(func):
        def _decorator(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ConnectionError as  e:
                sys.stderr.write("%s\n" % e)
                sys.exit(-1)

        return _decorator

    @staticmethod
    def capture_notfind_error(func):
        def _decorator(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except NotFoundError as e:
                sys.stderr.write("%s\n" % e)
                sys.exit(-1)

        return _decorator


class ElasticSearchImporter(object):
    batch_search_size = 1000

    def __init__(self, host, port=9200, username=None, password=None):
        if not username or not password:
            self.es = Elasticsearch(hosts=[host], port=port)
        else:
            self.es = Elasticsearch(hosts=[host], port=port, http_auth=(username, password))

    @ErrorHunter.capture_connection_error
    def index_is_exist(self, index_name):
        res = self.es.indices.exists(index=index_name)
        sys.stdout.write("index[%s] exist state is \n" % index_name, res)
        return res

    @ErrorHunter.capture_connection_error
    @ErrorHunter.capture_notfind_error
    def search_size(self, index_name, doc_type):
        res = self.es.search(index=index_name, doc_type=doc_type, body={"query": {"match_all": {}}})
        sys.stdout.write("search response is \n", res)
        return res["hits"]["total"]

    @ErrorHunter.capture_connection_error
    def _create_index(self, index_name):
        res = self.es.indices.create(index=index_name, ignore=400)
        sys.stdout.write("response of create index[%s]:" % index_name, res)

    def insert_by_batch(self, index_name, doc_type, data_list):
        batch_size = len(data_list) / self.batch_search_size + 1
        for i in range(int(batch_size)):
            begin_index = self.batch_search_size * i
            end_index = begin_index + self.batch_search_size
            res = self.insert_data_list(index_name=index_name, doc_type=doc_type,
                                        data_list=data_list[begin_index:end_index])

    @ErrorHunter.capture_connection_error
    def insert_data_list(self, index_name, doc_type, data_list):
        if not self.index_is_exist(index_name):
            self._create_index(index_name)

        actions = [
            {
                "_op_type": "index",
                "_index": index_name,
                "_type": doc_type,
                "_source": d
            }
            for d in data_list
        ]
        res = bulk(self.es, actions)
        sys.stdout.write("response of insert is : ", res)

    @ErrorHunter.capture_connection_error
    @ErrorHunter.capture_notfind_error
    def search_data(self, index_name, doc_type):
        if not self.index_is_exist(index_name):
            raise StopIteration

        total_size = self.search_size(index_name=index_name, doc_type=doc_type)
        # search data by page
        total_page = total_size / self.batch_search_size + 1
        for page_num in range(total_page):
            batch_result_data = self.es.search(index=index_name, doc_type=doc_type, from_=page_num,
                                               size=self.batch_search_size)
            id_data_list = [(result[u"_id"], result[u"_source"])
                            for result in batch_result_data[u"hits"][u"hits"]]
            for id_data in id_data_list:
                yield id_data

    @ErrorHunter.capture_connection_error
    @ErrorHunter.capture_notfind_error
    def search_by_body(self, index_name, doc_type, **kwargs):
        body = {
            "query": {
                "match": kwargs
            },
            "size": 1
        }
        res = self.es.search(index_name, doc_type, body)
        sys.stdout.write("%s\n" % res)

    @ErrorHunter.capture_connection_error
    @ErrorHunter.capture_notfind_error
    def update_data_list(self, index_name, doc_type, id_data_dict):
        if not id_data_dict:
            return
        actions = [
            {
                # "_op_type": "update",
                "_index": index_name,
                "_type": doc_type,
                "_source": d,
                "_id": id_index
            }
            for id_index, d in id_data_dict.iteritems()
        ]

        res = bulk(self.es, actions)
        sys.stdout.write("%s\n" % res)

    @ErrorHunter.capture_connection_error
    @ErrorHunter.capture_notfind_error
    def delete_index_doc(self, index_name):
        res = self.es.indices.delete(index=index_name)
        sys.stdout.write("%s\n" % res)
        return res

    def json_import(self, index_name, doc_type, json_file):
        if not os.path.exists(json_file):
            sys.stderr.write("This json file[%s] is not exist.\n" % json_file)
            sys.exit(-1)
        with open(json_file, "r") as f:
            data_list = json.load(f)
            self.insert_data_list(index_name=index_name, doc_type=doc_type, data_list=data_list)
            sys.stdout.write("Success import json file to ES.\n")


def test_search():
    builds_index_name = "builds_data"
    builds_doc_type = "data_stat_doc"
    es_import = ElasticSearchImporter(host="localhost")
    es_import.index_is_exist(builds_index_name)
    es_import.search_by_body(index_name=builds_index_name, doc_type=builds_doc_type,
                             data_path="/var/www/html/ec_latest_builds/DENALI_NGXTRAFFIC/CN_AXF_16Q2/DENALI_NGXTRAFFIC-CN_AXF_16Q2-TnMapDataAccess-linux-centos6x64-2.9.491956-trunk-20170510093257-RC")


def test_import():
    index_name = "sales"
    doc_type = "sales_doc"
    json_file_path = os.path.join(os.path.dirname(__file__), "sales.json")

    es_import = ElasticSearchImporter(host="localhost")
    es_import.json_import(index_name, doc_type, json_file_path)


if __name__ == '__main__':
    # import_builds_data("pbf_statistic_autonavi.json")
    # test_search()
    test_import()
