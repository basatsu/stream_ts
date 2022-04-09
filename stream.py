import streamlit as st
import pandas as pd
#import numpy as np
import openpyxl 
# DataFrame の表示
st.markdown('## DataFrameでの表示')
st.markdown('- 各列でのソートが可能')

st.sidebar.subheader("サイドバー表示")
st.sidebar.markdown('- 読み込むごとに数値をランダムに生成')

st.title("File uplodaer")
#uploaded_file =st.file_uploader("ファイルアップロード", type='csv')

global df
uploaded_file = st.file_uploader('アップロードしてください.', type=["csv","xlsx"])

#if st.button('表示する'):
if uploaded_file:
    #read csv
    print("データを表示")
    print("ファイル名："+uploaded_file.name)
    try:
        
        df=pd.read_csv(uploaded_file)
        #df=pd.read_excel(uploaded_file)
        #プレースホルダーphという変数をテーブル表示より先に割り当てる
        ph = st.empty()
        #st.table(df)
        

        #計算した総人口をプレースホルダーに代入する。
        df_sum = df['Price'].sum()
        ph.metric('値段合計:',str(df_sum) + '円')

        if st.button('表示する'):
            #横持ち変換
             #tb_long = pd.melt(df, id_vars=['Order type','Product type','Date'],var_name='variable', value_name='value')
             #df1=tb_long[["Order type","Product type","value"]]
             dg = df['Product type']
             #dglst = dg.astype(str).tolist()
             #dgstr = '\r\n'.join(dglst) 
             #st.write("SET DEFINE OFF"+"\r\n"+dgstr)

             st.download_button(label="File Download!!",data=dg.to_csv(index=False,header=False),file_name="Output.txt")

    
    except Exception as e:
        print(e)

#try:
#    st.write(df)
#except Exception as e:
#    print(e)
#    st.write("初期状態")
#else:    
 #   st.warning("you need to upload a csv or excel file")