import pandas as pd
import pymysql


def parser_excel():
    df = pd.read_excel('C:\Projects\learn\孕妇信息登记表.xlsx')
    print(df.keys())
    for i in df.index.values:
        print(i)
        data = df.ix[i].values
        keys = ['date_of_entry', 'source', 'name', 'phone',
                'gestation', 'trash', 'institution', 'build_date',
                'address', 'invitation_record', 'into_date', 'comment',
                'order_status', 'shoot_status',
                ]
        data_dict = dict(zip(keys, data))
        data_dict.pop('trash')
        data_dict = dict((key, value) for key, value in data_dict.items() if str(value) != 'nan' and str(value)!='NaT')
        insert_form(data_dict)


def connect_db():
    MYSQL_HOSTS = 'worker.qmgkj.cn'
    MYSQL_USER = 'gravida'
    MYSQL_PASSWORD = 'gravida'
    MYSQL_PORT = 3300
    MYSQL_DB = 'gravida'
    conn = pymysql.connect(
        host=MYSQL_HOSTS,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWORD,
        db=MYSQL_DB,
        charset="utf8")
    return conn


def select_id(name):
    conn = connect_db()
    sql = '''select id from Institution where name=%s'''
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql,name)
        data = cursor.fetchone()
        id = data.get('id')
        return id
    except Exception as e:
        pass


def insert_data(table, keys, values):
    conn = connect_db()
    cursor = conn.cursor()
    params = ['%s' for i in range(len(keys))]
    sql = '''INSERT INTO {}({}) VALUES({})'''.format(table, ','.join(keys), ','.join(params))
    cursor.execute(sql, values)
    conn.commit()


def insert_ins(name):
    id = select_id(name)
    if id:
        return id
    keys = ['name', ]
    values = [name, ]
    insert_data('Institution', keys, values)
    return select_id(name)


def insert_form(data):
    name = data.pop('institution')
    if name:
        institution_id = insert_ins(name)
    else:
        institution_id = None
    data['institution_id'] = institution_id
    keys, values = check(data)
    insert_data('register_form', keys, values)


def check(data):
    keys, values = [], []
    for k, v in data.items():
        if not v:
            continue
        keys.append(k)
        values.append(str(v))
    return keys, values


parser_excel()

