import streamlit as st

# Sample book database (you can replace it with an actual database or API)
books_db = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "Moby Dick", "author": "Herman Melville"}
]

# Function to search books by title
def search_books_by_title(title):
    results = [book for book in books_db if title.lower() in book['title'].lower()]
    return results

# Function to search books by author
def search_books_by_author(author):
    results = [book for book in books_db if author.lower() in book['author'].lower()]
    return results

# Streamlit application
st.title("Library Book Search")

st.write("Welcome to the library book search application!")

# Create two input forms for title and author search
search_type = st.radio("Search by", ("Title", "Author"))

if search_type == "Title":
    title = st.text_input("Enter the book title:")
    if title:
        results = search_books_by_title(title)
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']}")
        else:
            st.write("No books found with this title.")
        
elif search_type == "Author":
    author = st.text_input("Enter the author's name:")
    if author:
        results = search_books_by_author(author)
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']}")
        else:
            st.write("No books found by this author.")
