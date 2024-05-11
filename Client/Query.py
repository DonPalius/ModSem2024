# Import SPARQLWrapper for executing SPARQL queries and JSON for handling JSON data
from SPARQLWrapper import SPARQLWrapper, JSON

# Define a class for handling League of Legends (LoL) queries
class LoLQueries:
    def __init__(self, endpoint_url):
        # Initialize SPARQLWrapper with the endpoint URL and set the return format to JSON
        self.sparql = SPARQLWrapper(endpoint_url)
        self.sparql.setReturnFormat(JSON)

    # Method to execute a SPARQL query and return the results
    def execute_query(self, query):
        self.sparql.setQuery(query)
        results = self.sparql.query().convert()
        return results

    # Method to get assassin champions
    def get_assassin_champions(self):
        query = """
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT?label?comment
        WHERE {
          ?x rdf:type LoL:Assassin.
            OPTIONAL {?x rdfs:label?label }
            OPTIONAL {?x rdfs:comment?comment }
        }
        """
        return self.execute_query(query)

    # Method to get a list of players that played a match
    def get_players_list(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT?y?label?comment
        WHERE {
          ?x rdf:type LoL:Match_role;
            LoL:playerParticipating?y.
            OPTIONAL {?x rdfs:label?label }
            OPTIONAL {?x rdfs:comment?comment }
        }
        GROUP BY?y?label?comment
        """
        return self.execute_query(query)

    # Method to get the abilities of a specific champion (e.g., Zed)
    def get_champion_abilities(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT?x?label?comment
        WHERE {
          ?x rdf:type LoL:Abilità;
            LoL:ability_of?y.
            VALUES?y {LoL:Zed}.
            OPTIONAL {?x rdfs:label?label }
            OPTIONAL {?x rdfs:comment?comment }
        }
        """
        return self.execute_query(query)

    # Method to get the count of tank champions
    def get_tank_champions_count(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT (COUNT(?y) AS?count)
        WHERE {
          ?x rdf:type?y.
            VALUES?y {LoL:Tank}.
        }
        """
        return self.execute_query(query)

    # Method to get runes in the Domination path
    def get_dominance_runes(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT?label?comment
        WHERE {
          ?x rdf:type LoL:Rune;
            LoL:in_path LoL:Domination.
            OPTIONAL {?x rdfs:label?label }
            OPTIONAL {?x rdfs:comment?comment }
        }
        """
        return self.execute_query(query)

    # Method to get the loadout of faker in a match
    def get_loadout_for_player_in_match(self, player_name):
        query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        SELECT?loadout
        WHERE {{
          ?player rdf:type LoL:Player;
                    LoL:hasLoadout?loadout.
          ?match_role rdf:type LoL:Match_role;
                        LoL:playerParticipating?player.
            FILTER (?player = LoL:{player_name})
        }}
        """
        return self.execute_query(query)

    # Method to get attack stat objects
    def get_attack_stat_objects(self):
        query = """
        PREFIX : <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT?label?comment
        WHERE {
          ?x rdf:type LoL:Oggetto;
            LoL:has_stat?y.
          ?y rdf:type LoL:Attack.
            OPTIONAL {?x rdfs:label?label }
            OPTIONAL {?x rdfs:comment?comment }
        }
        """
        return self.execute_query(query)

    # Method to get champions that scale with ability power
    def get_ability_power_scaling_champions(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT?label?comment
        WHERE {
          ?x rdf:type LoL:Campione;
            LoL:scales_with_stat?y.
          ?y rdf:type?z.
          ?z rdfs:subClassOf LoL:Magic.
            OPTIONAL {?x rdfs:label?label }
            OPTIONAL {?x rdfs:comment?comment }
        }
        """
        return self.execute_query(query)

    # Method to get players in a match
    def get_players_in_match(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT?y?label?comment
        WHERE {
          ?x rdf:type LoL:Match_role;
            LoL:playerParticipating?y.
            OPTIONAL {?x rdfs:label?label }
            OPTIONAL {?x rdfs:comment?comment }
        }
        GROUP BY?y?label?comment
        """
        return self.execute_query(query)

    # Method to get rune pages used by a specific player
    def get_rune_pages_used_by_player(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        SELECT?label?comment
        WHERE {
          ?z rdf:type LoL:Rune_Page.
          ?y rdf:type LoL:Loadout.
          ?x rdf:type LoL:Match_role;
            LoL:playerParticipating LoL:Faker.
            OPTIONAL {?z rdfs:label?label }
            OPTIONAL {?z rdfs:comment?comment }
        }
        GROUP BY?label?comment
        """
        return self.execute_query(query)

    # Method to get available game modes
    def get_game_modes_available(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/gfazor/ontologies/LOL#>
        SELECT?label?comment
        WHERE {
          ?x rdf:type LoL:Modalità.
            OPTIONAL {?x rdfs:label?label }
            OPTIONAL {?x rdfs:comment?comment }
        }
        """
        return self.execute_query(query)

    # Method to get tournaments participated by a specific player
    def get_tournaments_participated_by_player(self):
        query = """
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT?label?time
        WHERE {
            SERVICE <https://query.wikidata.org/sparql>{
                OPTIONAL {
                    wd:Q15618298 wdt:P1344?link
                }
                OPTIONAL {
                  ?link rdfs:label?label;
                    wdt:P585?time.
                }
            }
            FILTER(LANG(?label) = "en")
        }
        ORDER BY?time
        """
        return self.execute_query(query)

    # Method to get teams played by a specific player
    def get_teams_played_by_player(self):
        query = """
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT?label?comment
        WHERE {
            SERVICE <https://query.wikidata.org/sparql>{
            OPTIONAL{
                wd:Q18608567 wdt:P54?team
            }
            OPTIONAL {?team rdfs:label?label }
            OPTIONAL {?team rdfs:comment?comment }
                FILTER(LANG(?label) = "en")
            }
        }
        """
        return self.execute_query(query)
