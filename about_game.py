import sqlite3

def get_all_games():

    with sqlite3.connect("TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute(""" 
            SELECT id, name, releaseYear
            FROM Game
            ORDER BY releaseYear;
        """)

        return cursor.fetchall()

def get_games_with_genres():

    with sqlite3.connect("TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute(""" 
            SELECT Game.name, Genre.name
            FROM Game
            JOIN GameGenre ON Game.id = GameGenre.gameId
            JOIN Genre ON GameGenre.genreId = Genre.id
            ORDER BY Game.name, Genre.name;
        """)

        return cursor.fetchall()

def search_games(keyword):



    with sqlite3.connect("TopGamesDB.db") as connection:
        cursor = connection.cursor()

        keyword_lower = keyword.lower()
        cursor.execute(""" 
            SELECT id, name, releaseYear
            FROM Game
            WHERE LOWER(name) LIKE ?
            ORDER BY name;
        """, (f"%{keyword_lower}%",))

        return cursor.fetchall()

games = search_games("witch")

for game in games:
    print(f"Game: {game[0]}, Genre: {game[1]}.")


   