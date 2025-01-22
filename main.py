import streamlit as st
import pandas as pd
import mysql.connector
import datetime
st.title("EMPLOYEE MANAGEMENT SYSTEM")
choice=st.sidebar.selectbox("My Menu",("Home","User","Department"))
if(choice=="Home"):
    st.image("https://img.freepik.com/free-vector/business-people-showing-document-client_1262-19209.jpg")
    st.write("This is a web application developed by me")
elif(choice=="User"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    eid=st.text_input("Enter Employee ID")
    epwd=st.text_input("Enter password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="Ra45@",database="ems")
        c=mydb.cursor()
        c.execute("select * from employees")
        for r in c:
                  if (r[0]==eid and r[4]==epwd):
                      st.session_state['login']=True
                         
        if(not st.session_state['login']):
            st.write("Incorrect ID or Password")
    if(st.session_state['login']):
        st.write("Login Successful")
        choice2=st.selectbox("Features",("None","View All Employees","Employees Update"))
        if(choice2=="View All Employees"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="Ra45@",database="ems")
            df=pd.read_sql("Select * from employees",mydb)
            st.dataframe(df)
        elif(choice2=="Employees Update"):
            eid=st.text_input("Enter Employee ID: ")
            did=st.text_input("Enter Departmaent ID: ")
            btn2=st.button("Update")
            if btn2:
                jid=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost",user="root",password="Ra45@",database="ems")
                c=mydb.cursor()
                c.execute("insert into up values(%s,%s,%s)",(eid,did,jid))
                mydb.commit()
                st.header("Employee Updated Successfully")
elif(choice=="Department"):
    if 'dlogin' not in st.session_state:
        st.session_state['dlogin']=False
    dept_id=st.text_input("Enter Department ID")
    dept_name=st.text_input("Enter Department Name")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="Ra45@",database="ems")
        c=mydb.cursor()
        c.execute("select * from deprt")
        for r in c:
                  if (r[0]==dept_name and r[1]==dept_id):
                      st.session_state['dlogin']=True
                         
        if(not st.session_state['dlogin']):
            st.write("Incorrect ID or Password")
    if(st.session_state['dlogin']):
        st.write("Login Successful")
        choice2=st.selectbox("Features",("None","View All Departments","Add New Employee"))
        if(choice2=="View All Departments"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="Ra45@",database="ems")
            df=pd.read_sql("Select * from deprt",mydb)
            st.dataframe(df)
        elif(choice2=="Add New Employee"):
            ename=st.text_input("Enter Employee name: ")
            eid=st.text_input("Enter Employee ID: ")
            cname=st.text_input("Enter Company name: ")
            emname=st.text_input("Enter Employee Mail: ")
            epwd=st.text_input("Enter password")
            btn2=st.button("Add New Employee")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="Ra45@",database="ems")
                c=mydb.cursor()
                c.execute("insert into employees values(%s,%s,%s,%s,%s)",(eid,ename,cname,emname,epwd))
                mydb.commit()
                st.header("Employee Added Successfully")
     
