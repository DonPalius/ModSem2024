import streamlit as st
from Query import LoLQueries  

endpoint_url = "http://localhost:7200/repositories/LOL" 
lol_queries = LoLQueries(endpoint_url)  

st.title('League of Legends Knowledge Base')
st.write("League of Legends Ontology for Semantic Web Exam")

selected_option = st.sidebar.selectbox("Select an action:", [
 "Get Assassin Champions",
 "Get List of Players",
 "Visualize Abilities (Champion Name Required)",
 "Get Tank Count",
 "Get Domination Runes",
 "Get Loadout for Player (Match Name Required)",
 "Get Attack Stat Objects",
 "Get Ability Power Scaling Champions",
 "Get Players in Match (Match Name Required)",
 "Get Rune Pages Used by Player",
 "Get Available Game Modes",
 "Get Tournaments Participated by Player",
 "Get Teams Played by Player"
])

# Define a dictionary mapping options to functions
option_to_function = {
 "Get Assassin Champions": lol_queries.get_assassin_champions,
 "Get List of Players": lol_queries.get_players_list,
 "Visualize Abilities (Champion Name Required)": lambda: lol_queries.get_champion_abilities(st.text_input("Enter Champion Name:")),
 "Get Tank Count": lol_queries.get_tank_champions_count,
 "Get Domination Runes": lol_queries.get_dominance_runes,
 "Get Loadout for Player (Match Name Required)": lambda: lol_queries.get_loadout_for_player_in_match(st.text_input("Enter Player Name:"), st.text_input("Enter Match Name:")),
 "Get Attack Stat Objects": lol_queries.get_attack_stat_objects,
 "Get Ability Power Scaling Champions": lol_queries.get_ability_power_scaling_champions,
 "Get Players in Match (Match Name Required)": lambda: lol_queries.get_players_in_match(st.text_input("Enter Match Name:")),
 "Get Rune Pages Used by Player": lambda: lol_queries.get_rune_pages_used_by_player(st.text_input("Enter Player Name:")),
 "Get Available Game Modes": lol_queries.get_game_modes_available,
 "Get Tournaments Participated by Player": lambda: lol_queries.get_tournaments_participated(st.text_input("Enter Player Name:")),
 "Get Teams Played by Player": lambda: lol_queries.get_teams_played_by_player(st.text_input("Enter Player Name:"))
}

# Execute the function corresponding to the selected option
if selected_option in option_to_function:
    result = option_to_function[selected_option]()
    if isinstance(result, tuple):
        st.write(f"{result[0]}:")
        st.write(result[1])
    else:
        st.write(result)
else:
    st.write("Please select an option.")

footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #333;
    color: white;
    text-align: center;
    padding: 10px 0;
}
</style>
<div class="footer">
    <p>© 2024 Gamba di squalo da 6 esami a giugno. All rights reserved.</p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
