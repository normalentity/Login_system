def save_user(Records):
    import sqlite3

    con = sqlite3.connect("Users.db")

    cur = con.cursor()

    query = (
        """ CREATE TABLE Users (Id INTEGER PRIMARY KEY,Username TEXT,Password TEXT); """
    )

    insert_query = """ INSERT INTO Users (Username,Password) VALUES (?,?); """

    cur.execute(insert_query, Records)
    con.commit()
