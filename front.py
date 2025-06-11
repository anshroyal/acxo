import streamlit as st 

import joblib as jo

st.set_page_config(
   page_title="Acxo ai",
   page_icon='favi.jpg'

)

st.title(" ACXO Anemia " )
st.write(" BETA version")



st.title(" ")

gender = st.radio("Gender",['Male','Female'])
Gender = 1 if gender == 'male' else 0 
hemo = st.number_input("Hemoglobin",min_value=0.0 , max_value= 20.0, value= 12.0)
mcv = st.number_input("MCV", min_value=0.0,max_value=120.0,value=85.0)
mchc = st.number_input("MCHC",min_value=0.0,max_value=40.0,value=33.0)
mch = st.number_input('MCH',min_value=0.0,max_value=40.0,value=28.0)

st.markdown("policy")
terms = st.checkbox('terms_policy')

with st.expander('terms_policy'):
   st.write(""" This AI tool is in beta stage .
            user must confirm the result with the doctor also  
            It does not provide medicl advice please consult to a doctor taking any action 
            users are agree that developer of this ai tool are not liable for any outcomes or wrong result 
            the user is agreeing all this terms and policy ... """
   "")


if terms:
    if st.button(' GO '):
    

     results = jo.load("anemia.pkl")
     result = results.predict([[Gender,hemo,mchc,mcv,mch]])[0]
     if 0 == result :
         st.success("NORMAL ")
     if 1 == result :
        st.warning(" likely AMENIA  ")
        with st.expander("Recommended"):
         st.write("consult to professional Doctor ")
    
st.write("version   0.1 (beta)")
