import streamlit as st

st.header('Factorial Application')
st.write('This app will calculate factorial')
num= st.number_input('Enter a number',value=0)
btn= st.button('Calculate')
if btn:
   result=1
   for i in range(1,num+1):

    result=result*i
   st.subheader(result)


    


