import streamlit as st

st.set_page_config(
    page_title="ITK Python Bank",
    page_icon="🏧",
    layout="wide"
)

# --------------------------------------
# Custom CSS
# --------------------------------------

st.markdown("""
<style>

.stApp{
    background:linear-gradient(135deg,#0f172a,#1e293b,#111827);
}

.main-title{
    font-size:42px;
    font-weight:bold;
    color:white;
    text-align:center;
}

.subtitle{
    color:#d1d5db;
    text-align:center;
    margin-bottom:30px;
}

.bank-card{
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0px 5px 20px rgba(0,0,0,.25);
}

.balance{
    background:#22c55e;
    color:white;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
}

.small-title{
    font-size:24px;
    font-weight:bold;
    color:#1f2937;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------
# Database
# --------------------------------------

accounts = {
    "123456": {
        "pin": "1234",
        "balance": 15000,
        "name": "Rahul"
    },
    "789012": {
        "pin": "5678",
        "balance": 8500,
        "name": "Priya"
    },
    "789013": {
        "pin": "1289",
        "balance": 20000,
        "name": "ITK"
    }
}

# --------------------------------------
# Session
# --------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

if "card" not in st.session_state:
    st.session_state.card=None

# --------------------------------------
# LOGIN PAGE
# --------------------------------------

if not st.session_state.logged_in:

    st.markdown("<h1 class='main-title'>🏧 ITK PYTHON BANK</h1>",unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Secure Internet Banking ATM</p>",unsafe_allow_html=True)

    col1,col2,col3=st.columns([1,2,1])

    with col2:

        st.markdown("<div class='bank-card'>",unsafe_allow_html=True)

        st.subheader("Login")

        card=st.text_input("Card Number")

        pin=st.text_input(
            "PIN",
            type="password"
        )

        if st.button("Login",use_container_width=True):

            if card in accounts:

                if pin==accounts[card]["pin"]:

                    st.session_state.logged_in=True
                    st.session_state.card=card
                    st.success("Login Successful")
                    st.rerun()

                else:
                    st.error("Incorrect PIN")

            else:
                st.error("Card Not Found")

        st.markdown("</div>",unsafe_allow_html=True)

# --------------------------------------
# DASHBOARD
# --------------------------------------

else:

    account=accounts[st.session_state.card]

    st.title("🏦 ITK Python Bank")

    st.success(f"Welcome {account['name']}")

    st.markdown(
        f"""
        <div class="balance">
        ₹ {account['balance']:,}
        <br>
        <span style="font-size:18px;">Available Balance</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    menu=st.sidebar.radio(
        "Choose Option",
        [
            "Check Balance",
            "Withdraw",
            "Deposit",
            "Logout"
        ]
    )

    # ------------------------
    # Balance
    # ------------------------

    if menu=="Check Balance":

        st.subheader("Account Balance")

        st.metric(
            "Current Balance",
            f"₹ {account['balance']:,}"
        )

    # ------------------------
    # Withdraw
    # ------------------------

    elif menu=="Withdraw":

        st.subheader("Withdraw Cash")

        amount=st.number_input(
            "Amount",
            min_value=100,
            step=100
        )

        if st.button("Withdraw"):

            if amount%100!=0:
                st.error("Amount should be multiple of 100")

            elif amount>10000:
                st.error("Maximum withdrawal is ₹10,000")

            elif amount>account["balance"]:
                st.error("Insufficient Balance")

            else:

                account["balance"]-=amount

                st.success(f"₹ {amount:,} Withdrawn Successfully")

                st.rerun()

    # ------------------------
    # Deposit
    # ------------------------

    elif menu=="Deposit":

        st.subheader("Deposit Money")

        amount=st.number_input(
            "Deposit Amount",
            min_value=100,
            step=100,
            key="deposit"
        )

        if st.button("Deposit"):

            account["balance"]+=amount

            st.success(f"₹ {amount:,} Deposited")

            st.rerun()

    # ------------------------
    # Logout
    # ------------------------

    elif menu=="Logout":

        st.session_state.logged_in=False
        st.session_state.card=None

        st.success("Logged Out")

        st.rerun()