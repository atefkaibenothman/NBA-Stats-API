import psycopg2

from data.player import Player
from data.team import Team


class Database:
    # initializes an empty dictionary to start
    def __init__(self):
        self.db_player = dict()
        self.db_team = dict()
        self.con = self.connect_to_db()
        self.curr = self.con.cursor()

    # returns the number of players in the database
    def __len__(self):
        return len(self.db_player)

    def __iter__(self):
        return self.db_player.__iter__()

    # prints player info and stats (id -> full_name)
    def list_all_players(self):
        print("\nLISTING ALL PLAYERS IN DATABASE")
        print("===============================")
        for player_id, _player in self.db_player.items():
            # FINISH THIS
            _player.get_player_stats()

    # adds a player to the database if they haven't been added before
    def add_player(self, player_id, full_name, first_name, last_name, is_active):
        if player_id not in self.db_player:
            self.db_player[player_id] = Player(
                player_id, full_name, first_name, last_name, is_active
            )
        else:
            print(f"{player_id} is already in the database!")

    # adds a team to the database
    def add_team(self, team_id, full_name, abbr, nick_name, city):
        if team_id not in self.db_team:
            self.db_team[team_id] = Team(team_id, full_name, abbr, nick_name, city)
        else:
            print(f"{team_id} is already in the database!")

    # adds a game log to the Player class
    def add_game_log(self, player_id, player_game_log):
        self.db_player[player_id].add_game_log_entry(player_game_log)

    # adds common info to Player class
    def add_player_common_info(self, player_id, info):
        self.db_player[player_id].add_common_info(info)

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
                team_id INT,
                team_abr TEXT,
                is_active BOOLEAN
            );
        """

        self.curr.execute(command)
        self.con.commit()
        print(f" --> created table: '{table_name}' <-- ")

    # create TEAM table
    def create_team_table(self):
        table_name = "Team"
        self.drop_table(table_name)

        command = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                team_id INT PRIMARY KEY,
                team_name TEXT,
                team_abr TEXT
            );
        """

        self.curr.execute(command)
        self.con.commit()
        print(f" --> created table: '{table_name}' <-- ")

    # insert player id's and names to database
    def insert_player_data(self):
        for player_id, _player in self.db_player.items():
            # print(player_id, _player)
            command = """
                INSERT INTO Player (player_id, lname, fname, position, team_id, team_abr, is_active)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """

            self.curr.execute(
                command,
                (
                    player_id,
                    _player.last_name,
                    _player.first_name,
                    _player.position,
                    _player.team_id,
                    _player.team_abbreviation,
                    _player.is_active,
                ),
            )
        self.con.commit()
        print("inserted data into table")

    # insert team data to database
    def insert_team_data(self):
        for team_id, _team in self.db_team.items():
            command = """
                INSERT INTO Team (team_id, team_name, team_abr)
                VALUES (%s, %s, %s);
            """

            self.curr.execute(
                command, (team_id, _team.nick_name, _team.abbr,),
            )
        self.con.commit()
        print("inserted data into team table")
