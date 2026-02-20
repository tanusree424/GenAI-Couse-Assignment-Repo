import streamlit as st
st.title("Price Calculator")
price=st.number_input("Enter Price",min_value=0.00)
discount=st.slider("Select Discount Percentage",0,50)
if st.button("Calculate Discount"):
    discount_amount = (price*discount) /100
    final_price = price - discount_amount

    st.success(f"The final price after discount {discount} % discount:{final_price}")
    data =[
        ["Original Price",price],
        ["Final Price",final_price]
    ]
    st.table(data)