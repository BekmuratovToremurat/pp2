import psycopg
from config import *

conn = psycopg.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

def get_player(username):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM players WHERE username=%s", (username,))
        row = cur.fetchone()
        if row:
            return row[0]

        cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
        conn.commit()
        return cur.fetchone()[0]


def save_game(pid, score, level):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO game_sessions(player_id, score, level_reached)
            VALUES (%s, %s, %s)
        """, (pid, score, level))
        conn.commit()


def leaderboard():
    with conn.cursor() as cur:
        cur.execute("""
            SELECT p.username, g.score, g.level_reached, g.played_at
            FROM game_sessions g
            JOIN players p ON p.id = g.player_id
            ORDER BY g.score DESC
            LIMIT 10
        """)
        return cur.fetchall()