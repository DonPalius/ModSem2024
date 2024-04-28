import streamlit as st
from Query import LoLQueries  
import pandas as pd

endpoint_url = "http://localhost:7200/repositories/LOL" 
lol_queries = LoLQueries(endpoint_url)  

st.title('League of Legends Ontology')





def get_table_from_results(results):
    # Define the headers
    headers = ["Label", "Comment"]
    
    # Initialize an empty DataFrame with the specified headers
    df = pd.DataFrame(columns=headers)

    for binding in results["results"]["bindings"]:
        label = binding.get("label", {}).get("value") 
        comment = binding.get("comment", {}).get("value")
        
        # Append each row to the DataFrame
        df = df.append({"Label": label, "Comment": comment}, ignore_index=True)

    # Display the DataFrame
    st.dataframe(df, use_container_width=True)




# Define tabs
tabs = st.tabs(["Champion Information", "Player Information", "Game Information"])

def run_query(selected_option):
  # Execute the function corresponding to the selected option
  if selected_option in option_to_function:
        result = option_to_function[selected_option]()
        get_table_from_results(result)
  else:
      st.write("Please select an option.")

# Define a dictionary mapping options to functions
option_to_function = {
    "Get Assassin Champions": lol_queries.get_assassin_champions,
    "Get List of Players that played a match": lol_queries.get_players_list,
    "Visualize Abilities of Zed": lol_queries.get_champion_abilities,
    "Get Tank Count": lol_queries.get_tank_champions_count,
    "Get Domination Runes": lol_queries.get_dominance_runes,
    # "Get Loadout for Player (Match Name Required)": lambda: lol_queries.get_loadout_for_player_in_match(st.text_input("Enter Player Name:"), st.text_input("Enter Match Name:")),
    "Get Attack Stat Objects": lol_queries.get_attack_stat_objects,
    "Get Ability Power Scaling Champions": lol_queries.get_ability_power_scaling_champions,
    "Get Rune Pages Used by Faker": lol_queries.get_rune_pages_used_by_player,
    "Get Available Game Modes": lol_queries.get_game_modes_available,
    "Get Tournaments Participated by Faker": lol_queries.get_tournaments_participated_by_player,
    "Get Teams Played by Rekkles":  lol_queries.get_teams_played_by_player
}

# Run queries based on tabs
with tabs[0]:  # Champion Information Tab
    selected_option = st.selectbox("Select an action:", [
        "Get Assassin Champions",
        "Visualize Abilities of Zed",
        "Get Tank Count",
        "Get Ability Power Scaling Champions"
    ])
    run_query(selected_option)

with tabs[1]:  # Player Information Tab
    selected_option = st.selectbox("Select an action:", [
        "Get List of Players that played a match",
        # "Get Loadout for Player (Match Name Required)",
        "Get Rune Pages Used by Faker",
        "Get Tournaments Participated by Faker",
        "Get Teams Played by Rekkles"
    ])
    run_query(selected_option)

with tabs[2]:  # Game Information Tab
    selected_option = st.selectbox("Select an action:", [
        "Get Domination Runes",
        "Get Attack Stat Objects",
        "Get Available Game Modes"
    ])
    run_query(selected_option)

footer = """
<style>
.footer {
    position: fixed;
    left: 0;  /* Align to left edge */
    bottom: 0;
    width: 100%;
    background-color: #333;
    color: white;
    text-align: center;  /* Center text horizontally */
}
</style>
<div class="footer">
    <p>© 2024 Gamba di squalo da 6 esami a giugno. All rights reserved.</p>
</div>

"""

st.markdown(footer, unsafe_allow_html=True)
