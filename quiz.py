import streamlit as st

# Title
st.title("💳 Credit Card Billing System")

# Input section
st.header("Enter Card Details")
name = st.text_input("Enter Card Holder Name")

st.header("Enter Your Transactions")
t1 = st.number_input("Enter first transaction amount (₹)", min_value=0.0)
t2 = st.number_input("Enter second transaction amount (₹)", min_value=0.0)
t3 = st.number_input("Enter third transaction amount (₹)", min_value=0.0)

# Function to calculate bill
def calculate_bill(transactions):
    return sum(transactions)

# Button to show total
if st.button("Show Total Bill"):
    transactions = [t1, t2, t3]
    total = calculate_bill(transactions)

    st.success(f"🧾 Card Holder: {name}")
    st.info(f"💰 Transactions: {transactions}")
    st.success(f"✅ Total Credit Card Bill: ₹ {total}")
    st.balloons()
