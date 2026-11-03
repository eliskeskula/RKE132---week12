import sqlite3


def search_games_by_publisher(publisher_name):
    with sqlite3.connect("TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Game.name, Publisher.name
            FROM Game
            JOIN GamePublisher ON Game.id = GamePublisher.gameId
            JOIN Publisher ON Publisher.id = GamePublisher.publisherId
            WHERE LOWER(Publisher.name) = LOWER(?)
            ORDER BY Game.name;
        """, (publisher_name,))

        return cursor.fetchall()


games = search_games_by_publisher("Nintendo")

for game in games:
    print(f"Mäng: {game[0]}, kirjastaja: {game[1]}")