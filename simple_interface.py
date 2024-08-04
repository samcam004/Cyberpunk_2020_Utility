import sqlite3 as sq


def main():
     # Connect to the database (or create it if it doesn't exist)
    conn = sq.connect("cyberpunk2020.db")

    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
    while True:
        query = input("Enter your query (type 'quit' to exit): ")
        if query.lower() == 'quit':
            print("Exiting the loop. Goodbye!")
            conn.close()
            break
        else:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

if __name__ == '__main__':
    main()

