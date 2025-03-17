# database.py
import sqlite3

def init_db():
    """Initializes the database and creates the papers table if it doesn't exist."""
    conn = sqlite3.connect("papers.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            abstract TEXT,
            source TEXT
        )
    """)
    conn.commit()
    conn.close()

def store_papers(papers, source):
    """Stores a list of paper dictionaries into the database."""
    conn = sqlite3.connect("papers.db")
    cursor = conn.cursor()
    for paper in papers:
        cursor.execute("""
            INSERT INTO papers (title, abstract, source)
            VALUES (?, ?, ?)
        """, (paper["title"], paper["abstract"], source))
    conn.commit()
    conn.close()

def get_all_papers():
    """Retrieves all papers from the database."""
    conn = sqlite3.connect("papers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM papers")
    rows = cursor.fetchall()
    conn.close()
    return rows
