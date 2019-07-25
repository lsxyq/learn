#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import json
import re

import requests
import urllib3
from bs4 import BeautifulSoup


class YunKao(object):
    client = requests.session()
    kaoshi = ""

    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def write_page_as_html(self, html, name):
        with open(name, 'w', encoding='utf8') as f:
            f.write(html)

    def vip_login(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36 Code(3oyNB0J61GsJzhhhSmH9M4GSP2wZGxZ1)",
            'referer': "https://easy.ykzbao.com/soft/index.php?user-app-login",
        }
        post_data = {
            'userlogin': 1,
            'args[username]': '15726802600',
            'args[userpassword]': 'asdf0987',
        }
        login_url = "https://easy.ykzbao.com/soft/index.php?user-app-login"
        r = self.client.post(url=login_url, data=post_data, headers=headers, verify=False)
        r.encoding = 'utf8'

    def get_chapter_page(self):
        url = "https://easy.ykzbao.com/soft/index.php?exam-app-lesson"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36 Code(3oyNB0J61GsJzhhhSmH9M4GSP2wZGxZ1)",
            'referer': "https://easy.ykzbao.com/soft/index.php?exam",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        r = self.client.post(url=url, headers=headers)
        self.parser_chapter_list(r.text)

    def get_lesson_page(self, api, chapter):
        url = "https://easy.ykzbao.com/soft/{}".format(api)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36 Code(3oyNB0J61GsJzhhhSmH9M4GSP2wZGxZ1)",
            'referer': "https://easy.ykzbao.com/soft/index.php?exam",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        r = self.client.post(url=url, headers=headers)
        self.parser_lesson_list(r.text, chapter)

    def get_question_page(self, api, lesson, chapter):
        url = "https://easy.ykzbao.com/soft/{}".format(api)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36 Code(3oyNB0J61GsJzhhhSmH9M4GSP2wZGxZ1)",
            'referer': "https://easy.ykzbao.com/soft/index.php?exam",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        r = self.client.post(url=url, headers=headers)
        self.parser_question_list(r.text, lesson, chapter)

    def parser_chapter_list(self, html):
        chapter_list = BeautifulSoup(html, 'lxml').find_all('div', attrs='lesson-chapter-li')
        for chapter in chapter_list:
            tag_a = chapter.find('a')
            api = tag_a['href']
            chapter = tag_a.attrs.get('data-title')
            print(chapter)
            self.get_lesson_page(api, chapter)

    def parser_lesson_list(self, html, chapter):

        lesson_list = BeautifulSoup(html, 'lxml').find_all('div', attrs='lesson-chapter-li')
        for lesson in lesson_list:
            tag_a = lesson.find('a', attrs='ajax')
            title = tag_a.find('div', attrs='lesson-chapter-li_t').get_text().strip('\xa0')
            api = tag_a['href']
            self.get_question_page(api, title, chapter)

    def parser_question_list(self, html, lesson, chapter):
        question_list = BeautifulSoup(html, 'lxml').find_all('div', attrs='swiper-slide questioncontent')
        for question_tag in question_list:
            try:
                self.clean_data(question_tag, chapter, lesson)
            except Exception as e:
                print(question_tag)

    def clean_data(self, question_tag, chapter, lesson):
        type, case, question = self.get_case_question(question_tag)
        data, other_sections = self.get_selector(question_tag)
        data.update({
            "kaoshi": self.kaoshi,
            "subject": chapter,
            "chapter": lesson,
            "section": "",
            "question": question,
            "tixing": type,
            "case": case,
            "answer": self.get_answer(question_tag) or '',
            "analysis": self.get_analysis(question_tag),
            "source": str(question_tag),
            "other_sections": json.dumps(other_sections) if other_sections else "",
        })

    def get_answer(self, question_tag):
        try:
            answer_tag = question_tag.find("span", attrs="rightanswer")
            answer = str(answer_tag).split(';">', 1)[-1].replace("</span>", "")
            return answer
        except Exception as e:
            print(e)

    def get_analysis(self, question_tag):
        try:
            analysis_tag = question_tag.find('p', attrs='questiondescribe')
            analysis = str(analysis_tag).split(';">')[1].replace("</p>", "")
            analysis = self.replace_word(analysis)
            if analysis == "暂无解析":
                analysis = ""
            return analysis
        except Exception as e:
            pass

    def get_selector(self, question_tag):
        try:
            choice_list = question_tag.find_all('li', attrs="questionselector")
            data = {}
            other_sections = {}
            keys = ["a", "b", "c", "d", "e"]
            for li in choice_list:
                index = li.attrs.get('rel')
                p_tag = li.find('p', attrs="answer")
                answer = str(p_tag).replace("</p>", "").replace(r'<p class="answer">', "")
                answer = self.replace_word(answer)
                if index.lower() not in keys:
                    other_sections[index.lower()] = answer
                    continue
                data[index.lower()] = answer
            return data, other_sections
        except Exception as e:
            return {}, {}

    def get_case_question(self, question_tag):
        detail_list = question_tag.find_all('div', attrs='d1-1 txt txt-left')
        type = re.findall("\\[(.*?)]", detail_list[0].get_text())[0]
        if type == "填空题":
            question_detail = detail_list[0]
            question = self.get_question(question_detail)
            return type, "", question
        if len(detail_list) > 1:
            case_tag = detail_list[0]
            case = self.get_case(case_tag)
            question_detail = detail_list[1]
        else:
            case = ""
            question_detail = detail_list[0]
        question = self.get_question(question_detail)
        return type, case, question

    def get_case(self, case_tag):
        case_list = str(case_tag).split("<br/>", 1)
        if len(case_list) > 1:
            case = ""
            for choice in case_list[-1].split("<br/>"):
                choice = re.sub("\n,\r,\r\n,\n\r,\t", "", choice)
                case = case + choice.replace("</div>", '') + "\n"
        else:
            case = str(case_tag).rsplit("</span>")[-1].replace("</div>", "")
            case = self.replace_word(case)
        return case

    def get_question(self, question_detail):
        question = str(question_detail).rsplit("</span>")[-1].replace("</div>", "").split(';">')[-1]
        question = question.split("（提示：", 1)[0]
        question = self.replace_word(question)
        return question

    def replace_word(self, world):
        world = re.sub("\n,\r,\r\n,\n\r,\t,", "", world)
        world = world.replace(" ", '')
        return world.strip()

    def init_kaoshi(self):
        self.kaoshi = input("请输入考试科目：").strip("\n") or "主治医师儿科"
        cid = input("请输入爬取科目编号:").strip("\n") or 59
        return self.set_current_subject(cid)

    def set_current_subject(self, cid):
        url = "https://easy.ykzbao.com/soft/index.php?exam-app-index-setCurrentBasic&basicid={}".format(cid)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36 Code(3oyNB0J61GsJzhhhSmH9M4GSP2wZGxZ1)",
            'referer': "https://easy.ykzbao.com/soft/index.php?exam",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        r = self.client.post(url=url, headers=headers)
        print(r.content.decode('utf8'))
        print(r.status_code)
        return r.status_code == 200

    def start_spider(self):
        self.vip_login()
        if not self.init_kaoshi():
            return
        self.get_chapter_page()


"""
cid     name
59      主治医师儿科
260     神经电生理
197     妇产科护理
"""

if __name__ == '__main__':
    t = YunKao()
    t.start_spider()
