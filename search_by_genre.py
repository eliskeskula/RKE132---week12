import sqlite3

def search_games_by_genre(genre_name):

    with sqlite3.connect("TopGamesDB.db") as connection:
        cursor = connection.cursor()

        genre_name_lower = genre_name.lower()
        cursor.execute(""" 
            SELECT Game.name, Game.releaseYear, Genre.name
            FROM Game
            JOIN GenreInGame ON Game.id = GenreInGame.gameId
            JOIN Genre ON Genre.id = GenreInGame.genreId
            WHERE LOWER(Genre.name) = LOWER(?)
            ORDER BY Game.name;
        """, (genre_name,))

        return cursor.fetchall()

games = search_games_by_genre("adventure")

for game in games:
    print(f"Game: {game[0]}, {game[1]}, {game[2]}")
