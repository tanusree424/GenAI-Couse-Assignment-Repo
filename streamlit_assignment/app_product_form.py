import streamlit as st
st.sidebar.header("Add Product Form")

product_name = st.sidebar.text_input("Enter Product Name:")

category= st.sidebar.selectbox("Category",["Electronics","Clothing","Book",])
price = st.sidebar.slider("Price",min_value=10, max_value=500000)
button_addProduct=st.sidebar.button("Add Product")
if button_addProduct:
    st.success("Product Added Successfuuly")

    st.write("---Product Deatils---")
    st.write("Product Name:",product_name)
    st.write(f"{product_name} Price is: {price}")
    st.write(f"{product_name} is: {category} Category")
