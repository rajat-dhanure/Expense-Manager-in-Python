def graph():

    import sqlite3
    import matplotlib.pyplot as plt

    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    cur.execute("SELECT item_name, item_price*quantity FROM expense_record")
    data = cur.fetchall()
    
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title('Expense Distribution')
    plt.show()

    conn.close()