import pandas as pd

# 1. Load players data
def load_players(file_path):
    players_df= pd.read_csv(file_path)
    print(players_df)
    return players_df
# 2. Load matches data
def load_matches(file_path):
    return pd.read_csv(file_path)

# 3. Merge players and matches on PlayerID
def merge_players_matches(players_df, matches_df):
    return pd.merge(players_df, matches_df, on='PlayerID')

# 4. Total runs scored per team
def total_runs_per_team(merged_df):
    return merged_df.groupby('Team')['Runs'].sum().reset_index()

# 5. Strike rate = (Runs / Balls) * 100
def calculate_strike_rate(merged_df):
    merged_df['StrikeRate'] = (merged_df['Runs'] / merged_df['Balls']) * 100
    return merged_df[['PlayerID', 'Name', 'Runs', 'Balls', 'StrikeRate']]

# 6. Run aggregation (mean, max, min) per player
def runs_agg_per_player(merged_df):
    return merged_df.groupby(['PlayerID', 'Name'])['Runs'].agg(['mean', 'max', 'min']).reset_index()

# 7. Average age by player role
def avg_age_by_role(players_df):
    return players_df.groupby('Role')['Age'].mean().reset_index()

# 8. Total number of matches played by each player
def total_matches_per_player(matches_df):
    print("DEBUG: Columns in matches_df =>", matches_df.columns.tolist())

    # Step 1: Get counts (index: PlayerID, column: count)
    match_counts = matches_df['PlayerID'].value_counts().reset_index()

    # Step 2: Rename columns explicitly and cleanly
    match_counts.columns = ['PlayerID', 'MatchCount']

    return match_counts


# 9. Top 3 players by total wickets
def top_wicket_takers(merged_df):
    return (
        merged_df.groupby(['PlayerID', 'Name'])['Wickets']
        .sum()
        .reset_index()
        .sort_values(by='Wickets', ascending=False)
        .head(3)
    )

# 10. Average strike rate per team
def avg_strike_rate_per_team(merged_df):
    merged_df['StrikeRate'] = (merged_df['Runs'] / merged_df['Balls']) * 100
    return merged_df.groupby('Team')['StrikeRate'].mean().reset_index()

# 11. Catch-to-match ratio per player
def catch_to_match_ratio(merged_df):
    matches_played = merged_df.groupby('PlayerID').size()
    total_catches = merged_df.groupby('PlayerID')['Catches'].sum()
    ratio = (total_catches / matches_played).reset_index(name='CatchToMatchRatio')
    return ratio
