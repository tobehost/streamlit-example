# import pymysql

import pandas as pd
import streamlit as st
from st_supabase_connection import SupabaseConnection
# import datetime


st.set_page_config(page_title="PEGO节点管理")

st.image('')

st.markdown('### **PEGO** _节点管理_')


    # 连接数据库
    conn = st.experimental_connection("supabase",type=SupabaseConnection)

    # Perform query.
    rows = conn.query("*", table="pego_7a47_vt_base", ttl="10m").execute()

    # Print results.
    for row in rows.data:
    st.write(f"{row['address']} has a :{row['clubof']}:")
