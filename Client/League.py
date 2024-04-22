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

if selected_option == "Get Assassin Champions":
  champions = lol_queries.get_assassin_champions()
  st.write("Assassin Champions:")
  st.write(champions)
elif selected_option == "Get List of Players":
  players = lol_queries.get_players_list()
  st.write("Players:")
  st.write(players)
elif selected_option == "Visualize Abilities (Champion Name Required)":
  champion_name = st.text_input("Enter Champion Name:")
  if champion_name:
    abilities = lol_queries.get_champion_abilities(champion_name)
    st.write(f"{champion_name}'s Abilities:")
    st.write(abilities)
  else:
    st.write("Please enter a champion name.")
elif selected_option == "Get Tank Count":
  tank_count = lol_queries.get_tank_champions_count()
  st.write("Number of Tank Champions:")
  st.write(tank_count)
elif selected_option == "Get Domination Runes":
  domination_runes = lol_queries.get_dominance_runes()
  st.write("Domination Runes:")
  st.write(domination_runes)
elif selected_option == "Get Loadout for Player (Match Name Required)":
  player_name = st.text_input("Enter Player Name:")
  match_name = st.text_input("Enter Match Name:")
  if player_name and match_name:
    loadout = lol_queries.get_loadout_for_player_in_match(player_name, match_name)
    st.write(f"{player_name}'s Loadout in {match_name}:")
    st.write(loadout)
  else:
    st.write("Please enter both player name and match name.")
elif selected_option == "Get Attack Stat Objects":
  attack_objects = lol_queries.get_attack_stat_objects()
  st.write("Attack Stat Objects:")
  st.write(attack_objects)
elif selected_option == "Get Ability Power Scaling Champions":
  ap_champions = lol_queries.get_ability_power_scaling_champions()
  st.write("Ability Power Scaling Champions:")
  st.write(ap_champions)
elif selected_option == "Get Players in Match (Match Name Required)":
  match_name = st.text_input("Enter Match Name:")
  if match_name:
    players = lol_queries.get_players_in_match(match_name)
    st.write(f"Players in Match {match_name}:")
    st.write(players)
  else:
    st.write("Please enter a match name.")
elif selected_option == "Get Rune Pages Used by Player":
  player_name = st.text_input("Enter Player Name:")
  if player_name:
    rune_pages = lol_queries.get_rune_pages_used_by_player(player_name)
    st.write(f"{player_name}'s Rune Pages:")
    st.write(rune_pages)
  else:
    st.write("Please enter a player name.")
elif selected_option == "Get Available Game Modes":
  game_modes = lol_queries.get_game_modes_available()
  st.write("Available Game Modes:")
  st.write(game_modes)
elif selected_option == "Get Tournaments Participated by Player":
  player_name = st.text_input("Enter Player Name:")
  if player_name:
    tournaments = lol_queries.get_tournaments_participated



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
