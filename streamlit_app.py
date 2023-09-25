import pymysql
import pandas as pd
import streamlit as st
import datetime


st.set_page_config(page_title="PEGO节点管理")

st.image('https://marketplace.canva.cn/EADcCIofLbk/1/0/800w/canva-%E6%B9%96%E8%93%9D%E5%87%A0%E4%BD%95%E7%90%83%E4%BD%93linkedin-banner-YvIEH_UH5YQ.jpg')

st.markdown('### **PEGO** _节点管理_')

def query(cursor):

    sql = 'select * from st order by id;'

    # 执行sql中的语句

    try:

        cursor.execute(sql)

        # 获得列名

        column = ['编号', '钱包地址', '建档时间', '俱乐部', 'VT初始余额']

        # 获得数据

        data = cursor.fetchall()

    except Exception as e:

        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')

    # 获得DataFrame格式的数据

    data_df = pd.DataFrame(list(data), columns=column)

    st.table(data_df)

def remove(cursor):

    sql = 'select * from sp;'

    # 执行sql中的语句

    try:

        cursor.execute(sql)

        # 获得列名

        column = [col[0] for col in cursor.description]

        # 获得数据

        data = cursor.fetchall()

    except Exception as e:

        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')

    # 获得DataFrame格式的数据

    data_df = pd.DataFrame(list(data), columns=column)

    # 执行sql中的语句

    name = st.selectbox('你想删除哪个商品?', data_df['name'])

    '你选择了: ', name

    sql = "delete from sp where name=%s"

    if st.button('删除'):

        try:

            cursor.execute(sql, name)

            db.commit()

            st.success("删除成功！")

        except Exception as e:

            db.rollback()

            st.error(f'删除失败！原因：{str(e).split(",")[1][1:-1]}')

def add(cursor):

    sql = 'select * from lx;'

    # 执行sql中的语句

    try:

        cursor.execute(sql)

        # 获得列名

        column = ['编号', '俱乐部名称']

        # 获得数据

        data = cursor.fetchall()

    except Exception as e:

        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')

    # 获得DataFrame格式的数据

    df = pd.DataFrame(list(data), columns=column)

    list1 = df.values.tolist()

    dict_lx = {}

    for i in list1:

        dict_lx[i[1]] = i[0]

    list_lx = list(dict_lx.keys())

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input('钱包地址')

        itime = st.date_input("建档日期：", datetime.date(2020, 1, 1))

    with col2:

        price = st.text_input('VT初始余额')

        type = st.selectbox('俱乐部?', list_lx)

    sql = "INSERT INTO sp(name,itime,price,type) VALUES (%s,%s,%s,%s)"

    if st.button('添加'):

        try:

            cursor.execute(sql, (name,itime,price,

                                 dict_lx[type]))

            db.commit()

            st.success("添加成功！")

        except Exception as e:

            db.rollback()

            st.error(f'添加失败！原因：{str(e).split(",")[1][1:-1]}')

def modify(cursor):

    sql = 'select * from lx;'

    # 执行sql中的语句

    try:

        cursor.execute(sql)

        # 获得列名

        column = ['编号', '俱乐部名称']

        # 获得数据

        data = cursor.fetchall()

    except Exception as e:

        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')

    # 获得DataFrame格式的数据

    df = pd.DataFrame(list(data), columns=column)

    list1 = df.values.tolist()

    # 键为商品类型名，值为商品类型编号

    dict_lx = {}

    # 键为商品类型编号，值为商品类型名

    dict_lx2 = {}

    for i in list1:

        dict_lx[i[1]] = i[0]

        dict_lx2[i[0]] = i[1]

    list_type = list(dict_lx.keys())

    sql = 'select * from sp;'

    try:

        # 执行sql中的语句

        cursor.execute(sql)

        # 获得列名

        column = [col[0] for col in cursor.description]

        # 获得数据

        data = cursor.fetchall()

    except Exception as e:

        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')

    # 获得DataFrame格式的数据

    data_df = pd.DataFrame(list(data), columns=column)

    # 执行sql中的语句

    name = st.selectbox('你想修改哪个地址?', data_df['name'])

    '你选择了: ', name

    sql = "select * from sp where name=%s"

    try:

        cursor.execute(sql, name)

        id_, name, price, type, itime=cursor.fetchone()

    except Exception as e:

        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')

    with st.container():

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input('钱包地址', name)

            price = st.text_input('VT初始余额')  

        with col2:

            type = st.selectbox('俱乐部名称?', list_type)

            itime= st.date_input("建档日期：",datetime.date(2023,6,23))        

    sql = "UPDATE sp set name=%s,itime=%s,price=%s,type=%s where id=%s"

    if st.button('修改'):

        try:

             cursor.execute(sql, (name,itime,price,

                                  dict_lx[type],id_))

             db.commit()

             st.success("修改成功！")

        except Exception as e:

             db.rollback()

             st.error(f'修改失败！原因：{str(e).split(",")[1][1:-1]}')

def query_zy(cursor):

    sql = 'select * from lx order by id_type;'

    try:

        # 执行sql中的语句

        cursor.execute(sql)

        column = ['编号', '钱包地址']

        # 获得数据

        data = cursor.fetchall()

    except Exception as e:

        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')

    # 获得DataFrame格式的数据

    data_df = pd.DataFrame(list(data), columns=column)

    st.table(data_df)

def remove_zy(cursor):

    sql = 'select * from lx;'

    try:

        # 执行sql中的语句

        cursor.execute(sql)

        # 获得列名

        column = [col[0] for col in cursor.description]

        # 获得数据

        data = cursor.fetchall()

    except Exception as e:

        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')

    # 获得DataFrame格式的数据

    data_df = pd.DataFrame(list(data), columns=column)

    # 执行sql中的语句

    col1, col2 = st.columns(2)

    with col1:

        name = st.selectbox('你想删除哪个俱乐部名称?', data_df['name_type'])

        '你选择了: ', name

    sql = "delete from lx where name_type=%s"

    if st.button('删除'):

        try:

            cursor.execute(sql, name)

            db.commit()

            st.success("删除成功！")

        except Exception as e:

            db.rollback()

            st.error(f'删除失败！原因：{str(e).split(",")[1][1:-1]}')

def add_zy(cursor):

    col1, col2 = st.columns(2)

    with col1:

        id_type = st.text_input('俱乐部名称编号（2位数字）：')

        name_type = st.text_input('俱乐部名称：')

    sql = "INSERT INTO lx(id_type,name_type) VALUES (%s,%s)"

    if st.button('添加'):

        try:

            cursor.execute(sql, (id_type, name_type))

            db.commit()

            st.success("添加成功！")

        except Exception as e:

            db.rollback()

            st.error(f'添加失败！原因：{str(e).split(",")[1][1:-1]}')

def modify_zy(cursor):

    sql = 'select * from lx;'

    try:

        # 执行sql中的语句

        cursor.execute(sql)

        # 获得列名

        column = [col[0] for col in cursor.description]

        # 获得数据

        data = cursor.fetchall()

    except Exception as e:

        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')

    # 获得DataFrame格式的数据

    data_df = pd.DataFrame(list(data), columns=column)

    # 执行sql中的语句

    col1, col2 = st.columns(2)

    with col1:

        name = st.selectbox('你想修改哪个俱乐部?', data_df['name_type'])

        '你选择了: ', name

    sql = "select * from lx where name_type=%s"

    try:

        cursor.execute(sql, name)

        id_, name = cursor.fetchone()

    except Exception as e:

        st.error(f'查询失败！原因：{str(e).split(",")[1][1:-1]}')

    with st.container():

        col1, col2 = st.columns(2)

        with col1:

            nid = st.text_input('新俱乐部编号：', id_)

            name = st.text_input('新俱乐部名称：', name)

    sql = "UPDATE type set id_type=%s,name_type=%s where id_type=%s"

    if st.button('修改'):

        try:

            cursor.execute(sql, (nid, name, id_))

            db.commit()

            st.success("修改成功！")

        except Exception as e:

            db.rollback()

            st.error(f'修改失败！原因：{str(e).split(",")[1][1:-1]}')

if __name__ == '__main__':

    action = st.sidebar.selectbox(

        "你想进行的操作？",

        ['查看钱包地址', '删除钱包地址', '修改钱包地址', '添加钱包地址', '查看俱乐部', '删除俱乐部', '修改俱乐部', '添加俱乐部']

    )

    # 连接数据库

    db = pymysql.connect(host='localhost', user='alexia',

                         passwd='89854663', port=3306, db='temp')

    # 开启一个游标cursor

    cursor = db.cursor()

    if action == '查看钱包地址':

        query(cursor)

    elif action == '删除钱包地址':

        remove(cursor)

    elif action == '添加钱包地址':

        add(cursor)

    elif action == '修改钱包地址':

        modify(cursor)

    elif action == '查看俱乐部':

        query_zy(cursor)

    elif action == '删除俱乐部':

        remove_zy(cursor)

    elif action == '添加俱乐部':

        add_zy(cursor)

    elif action == '修改俱乐部':

        modify_zy(cursor)

    else:

        pass

    cursor.close()

    db.close()


# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))
