import pandas as pd

# ================= LOAD DATA =================
def load_matches_data():
    try:
        df = pd.read_csv("matches.csv")
        return df
    except FileNotFoundError:
        print("matches.csv file not found")
        return pd.DataFrame()

def load_players_data():
    try:
        df = pd.read_csv("players.csv")
        return df
    except FileNotFoundError:
        print("players.csv file not found")
        return pd.DataFrame()


# ================= DATA CLEANING =================
def clean_matches_data(df):
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df

def clean_players_data(df):
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df


# ================= TEAM ANALYSIS =================
def get_team_stats(df, team):
    team_matches = df[(df['team1'] == team) | (df['team2'] == team)]

    wins = team_matches[team_matches['winner'] == team].shape[0]
    losses = team_matches.shape[0] - wins

    return wins, losses


# ================= PLAYER ANALYSIS =================
def get_player_stats(df, player):
    player_data = df[df['name'] == player]

    if not player_data.empty:
        runs = int(player_data['runs'].values[0])
        matches = int(player_data['matches'].values[0])
        strike_rate = float(player_data['strike_rate'].values[0])

        return runs, matches, strike_rate
    else:
        return 0, 0, 0.0