import pymysql
import search_paths
from builtins import int

# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='hDA186', db='hda_drc')
# 创建游标
cursor = conn.cursor()
# conn.set_character_set('utf8')
# cursor.execute('SET NAME utf8;')
# cursor.execute('SET CHARACTER SET utf8;')
# cursor.execute('SET character_set_connection=utf8;')

sql = "select * from files_drc"
sql_desc = "desc files_drc"
sql_insert = "insert into files_drc values (%s,%s,%s,%s,%s,%x)"
list_insert = [('asdf111', 'ww', 'aa\/bb\/', '333', 'docx', ""),
               ('asdf222', 'ee', 'aa\/bb\/', '222', 'docx', "")]

def register_drc():
    with open('E:\\info.txt', 'r+') as fp:
            for line in fp:
                print(line)
cursor.executemany(sql_insert, list_insert)

cursor.execute(sql_desc)

print(cursor.execute(sql))
row = cursor.fetchone()  # 获取一行

print(row)
conn.commit()
cursor.close()

conn.close()
