# main.py

import streamlit as st
from db import fetch_books, search_books_by_title, search_books_by_author, add_new_book

st.title("Library Database")

st.header("Books in the Library")
books = fetch_books()
for book in books:
    st.write(f"**Title**: {book[1]}")
    st.write(f"**Author**: {book[2]} {book[3]}")
    st.write(f"**Publisher**: {book[4]}")
    st.write(f"**Genre**: {book[5]}")
    st.write(f"**Publication Year**: {book[6]}")
    st.write(f"**Price**: {book[7]} RUB")
    st.write(f"**Available Copies**: {book[8]}")
    st.write("---")

st.header("Search Books by Title")
search_title = st.text_input("Enter book title to search:")
if search_title:
    search_results = search_books_by_title(search_title)
    for book in search_results:
        st.write(f"**Title**: {book[1]}")
        st.write(f"**Author**: {book[2]} {book[3]}")
        st.write(f"**Publisher**: {book[4]}")
        st.write(f"**Genre**: {book[5]}")
        st.write(f"**Publication Year**: {book[6]}")
        st.write(f"**Price**: {book[7]} RUB")
        st.write(f"**Available Copies**: {book[8]}")
        st.write("---")

st.header("Search Books by Author")
search_author = st.text_input("Enter author name to search:")
if search_author:
    search_results = search_books_by_author(search_author)
    for book in search_results:
        st.write(f"**Title**: {book[1]}")
        st.write(f"**Author**: {book[2]} {book[3]}")
        st.write(f"**Publisher**: {book[4]}")
        st.write(f"**Genre**: {book[5]}")
        st.write(f"**Publication Year**: {book[6]}")
        st.write(f"**Price**: {book[7]} RUB")
        st.write(f"**Available Copies**: {book[8]}")
        st.write("---")

st.header("Add a New Book")
title = st.text_input("Book Title")
author_id = st.number_input("Author ID", min_value=1)
publisher_id = st.number_input("Publisher ID", min_value=1)
genre_id = st.number_input("Genre ID", min_value=1)
publication_year = st.number_input("Publication Year", min_value=1000, max_value=9999)
isbn = st.text_input("ISBN")
price = st.number_input("Price", min_value=0.0, format="%.2f")
pages = st.number_input("Pages", min_value=1)
available_copies = st.number_input("Available Copies", min_value=0)

if st.button("Add Book"):
    add_new_book(title, author_id, publisher_id, genre_id, publication_year, isbn, price, pages, available_copies)
    st.success(f"Book '{title}' has been added to the database.")
