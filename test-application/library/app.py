import streamlit as st

from data import categories, books, members, library

st.set_page_config(
    page_title="Smart Library",
    page_icon="📚",
    layout="wide"
)

# -------------------------
# Session State
# -------------------------

if "library" not in st.session_state:
    st.session_state.library = library.copy()

# -------------------------
# Header
# -------------------------

st.title("📚 Smart Library Management System")

st.write("Learn Python Collections using Streamlit")

# -------------------------
# Sidebar
# -------------------------

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Show Categories",
        "Show All Books",
        "Search Book",
        "Borrow Book",
        "Return Book",
        "Available Books",
        "Members",
        "Unique Books",
        "Count Each Book",
        "Low Stock",
        "Search by Letter"
    ]
)

# -------------------------
# 1 Categories
# -------------------------

if menu == "Show Categories":

    st.header("📂 Categories")

    for category in categories:
        st.success(category)

# -------------------------
# 2 All Books
# -------------------------

elif menu == "Show All Books":

    st.header("📘 All Books")

    for book in books:
        st.write(book)

# -------------------------
# 3 Search Book
# -------------------------

elif menu == "Search Book":

    st.header("🔍 Search Book")

    search = st.text_input("Book Name")

    if st.button("Search"):

        found = False

        for book in books:

            if search.lower() in book.lower():
                st.success(book)
                found = True

        if not found:
            st.error("Book Not Found")

# -------------------------
# 4 Borrow Book
# -------------------------

elif menu == "Borrow Book":

    st.header("📖 Borrow Book")

    book = st.selectbox(
        "Select Book",
        list(st.session_state.library.keys())
    )

    if st.button("Borrow"):

        if st.session_state.library[book] > 0:

            st.session_state.library[book] -= 1

            st.success(f"You borrowed {book}")

        else:

            st.error("Book Out Of Stock")

# -------------------------
# 5 Return Book
# -------------------------

elif menu == "Return Book":

    st.header("📥 Return Book")

    book = st.selectbox(
        "Select Book",
        list(st.session_state.library.keys())
    )

    if st.button("Return"):

        st.session_state.library[book] += 1

        st.success("Book Returned Successfully")

# -------------------------
# 6 Available Books
# -------------------------

elif menu == "Available Books":

    st.header("📚 Available Books")

    for book, count in st.session_state.library.items():

        if count > 0:

            st.write(f"**{book}** → {count}")

# -------------------------
# 7 Members
# -------------------------

elif menu == "Members":

    st.header("👨‍🎓 Library Members")

    for member in members:
        st.write(member)

# -------------------------
# 8 Unique Books
# -------------------------

elif menu == "Unique Books":

    st.header("⭐ Unique Books")

    unique_books = set(books)

    for book in unique_books:
        st.write(book)

# -------------------------
# 9 Count Books
# -------------------------

elif menu == "Count Each Book":

    st.header("📊 Book Inventory")

    for book, count in st.session_state.library.items():

        st.metric(book, count)

# -------------------------
# 10 Low Stock
# -------------------------

elif menu == "Low Stock":

    st.header("⚠ Low Stock Books")

    low = False

    for book, count in st.session_state.library.items():

        if count < 3:

            st.warning(f"{book} : {count}")

            low = True

    if not low:
        st.success("No Low Stock Books")

# -------------------------
# 11 Search Letter
# -------------------------

elif menu == "Search by Letter":

    st.header("🔠 Search By Starting Letter")

    letter = st.text_input("Starting Letter")

    if st.button("Find"):

        found = False

        for book in books:

            if book.lower().startswith(letter.lower()):

                st.success(book)

                found = True

        if not found:
            st.error("No Books Found")