import psycopg2

from data.player import Player


class Database:
    # initializes an empty dictionary to start
    def __init__(self):
        self.db = dict()

        self.con = self.connect_to_db()
        self.curr = self.con.cursor()
        self.create_player_table()

    # returns the number of players in the database
    def __len__(self):
        return len(self.db)

    def __iter__(self):
        return self.db.__iter__()

    # prints player info and stats (id -> full_name)
    def list_all_players(self):
        print("\nLISTING ALL PLAYERS IN DATABASE")
        print("===============================")
        for player_id, _player in self.db.items():
            # FINISH THIS
            _player.get_player_stats()

    # adds a player to the database if they haven't been added before
    def add_player(self, player_id, full_name, first_name, last_name, is_active):
        if player_id not in self.db:
            self.db[player_id] = Player(
                player_id, full_name, first_name, last_name, is_active
            )
        else:
            print(f"{player_id} is already in the database!")

    # adds a game log to the Player class
    def add_game_log(self, player_id, player_game_log):
        self.db[player_id].add_game_log_entry(player_game_log)

    # connect to the db
    def connect_to_db(self):
        h = "localhost"
        db = "nba_db"
        usr = "kai"
        pw = "123"
        prt = 5432

        con = psycopg2.connect(host=h, database=db, user=usr, password=pw, port=prt,)

        print(f" --> connected to database: '{db}' <-- ")

        return con

    # close connection to db
    def close_connection(self):
        self.con.close()
        print(f" --> closed connection to database <-- ")

    # drop table
    def drop_table(self, table_name):
        command = f"DROP TABLE IF EXISTS {table_name};"
        self.curr.execute(command)
        self.con.commit()
        print(f" --> dropping table: '{table_name}' <-- ")

    # create PLAYER table
    def create_player_table(self):
        table_name = "Player"
        self.drop_table(table_name)

        command = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                player_id INT PRIMARY KEY,
                lname TEXT,
                fname TEXT,
                position TEXT,
                is_active BOOLEAN
            );
        """

        self.curr.execute(command)
        self.con.commit()
        print(f" --> created table: '{table_name}' <-- ")

    # insert player id's and names to database
    def insert_player_data(self):
        for player_id, _player in self.db.items():
            # print(player_id, _player)
            command = """
                INSERT INTO Player (player_id, lname, fname, is_active)
                VALUES (%s, %s, %s, %s)
            """

            self.curr.execute(
                command,
                (player_id, _player.last_name, _player.first_name, _player.is_active,),
            )
        self.con.commit()
