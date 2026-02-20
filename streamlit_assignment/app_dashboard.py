import streamlit as st

st.title("Simple Sales Dashboard")
selected_months=st.selectbox("Months", [
    "January", "February" , "March" ,"April"
])

sales = {
    "January":1200,
    "February":1500,
    "March":900,
    "April":2000,
    

}

st.metric(label=f"{selected_months} Sales", value=sales[selected_months])
st.bar_chart(list(sales.values()))