import streamlit as st
from collections import Counter

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="🍽️ ITK Restaurant",
    page_icon="🍽️",
    layout="wide"
)

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#FF4B4B;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.bill-box{
    background:#F8F9FA;
    padding:20px;
    border-radius:12px;
    border:1px solid #DDD;
}

.summary-box{
    background:#EAF7EA;
    padding:20px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# Restaurant Menu
# ==========================================

menu = {
    "Paneer Butter Masala": 220,
    "Veg Biryani": 200,
    "Butter Chicken": 280,
    "Chicken Biryani": 300,
    "Garlic Naan": 40,
    "Lassi": 60,
    "Cold Coffee": 80,
}

# Session State
if "customers" not in st.session_state:
    st.session_state.customers = set()

if "sales" not in st.session_state:
    st.session_state.sales = {}

# ==========================================
# Header
# ==========================================

st.markdown("<div class='main-title'>🍽️ ITK RESTAURANT</div>",
            unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>Simple Restaurant Management System</div>",
    unsafe_allow_html=True
)

# ==========================================
# Layout
# ==========================================

left, right = st.columns([2,1])

# ==========================================
# LEFT SIDE
# ==========================================

with left:

    st.subheader("👤 Customer Details")

    customer = st.text_input("Customer Name")

    st.subheader("📋 Menu")

    menu_data = []

    for item, price in menu.items():
        menu_data.append({
            "Item": item,
            "Price (₹)": price
        })

    st.dataframe(menu_data,
                 use_container_width=True,
                 hide_index=True)

    st.subheader("🛒 Place Order")

    ordered_items = st.multiselect(
        "Select Items",
        list(menu.keys())
    )

# ==========================================
# RIGHT SIDE
# ==========================================

with right:

    st.subheader("💵 Bill")

    if st.button("Generate Bill", use_container_width=True):

        if customer.strip() == "":
            st.warning("Please enter customer name.")
            st.stop()

        st.session_state.customers.add(customer.title())

        total = 0

        st.markdown("### Ordered Items")

        for item in ordered_items:
            st.write(f"✅ {item} - ₹{menu[item]}")
            total += menu[item]

            if item in st.session_state.sales:
                st.session_state.sales[item] += 1
            else:
                st.session_state.sales[item] = 1

        st.divider()

        st.metric(
            "💰 Total Bill",
            f"₹ {total}"
        )

        st.success("Order Successfully Placed!")

# ==========================================
# Summary
# ==========================================

st.divider()

st.header("📊 Restaurant Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "👥 Unique Customers",
        len(st.session_state.customers)
    )

with c2:

    total_orders = sum(st.session_state.sales.values())

    st.metric(
        "🍴 Total Items Sold",
        total_orders
    )

with c3:

    if st.session_state.sales:

        best = max(
            st.session_state.sales,
            key=st.session_state.sales.get
        )

        st.metric(
            "🏆 Best Seller",
            best
        )

    else:
        st.metric(
            "🏆 Best Seller",
            "-"
        )

# ==========================================
# Sales Table
# ==========================================

st.subheader("📈 Sales Report")

if st.session_state.sales:

    sales_table = []

    for item, qty in st.session_state.sales.items():

        sales_table.append({
            "Item": item,
            "Quantity Sold": qty,
            "Revenue": qty * menu[item]
        })

    st.dataframe(
        sales_table,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No sales yet.")

# ==========================================
# Footer
# ==========================================

st.divider()

st.caption("Made with ❤️ using Streamlit")