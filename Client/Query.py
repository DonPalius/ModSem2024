from SPARQLWrapper import SPARQLWrapper, JSON

class LoLQueries:
    def __init__(self, endpoint_url):
        self.sparql = SPARQLWrapper(endpoint_url)
        self.sparql.setReturnFormat(JSON)

    def execute_query(self, query):
        self.sparql.setQuery(query)
        results = self.sparql.query().convert()
        return results

    def get_assassin_champions(self):
        query = """
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?x WHERE {?x rdf:type LoL:Assassin.}
        """
        return self.execute_query(query)

    def get_players_list(self):
        query = """
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?x WHERE {?x rdf:type LoL:Player}
        """
        return self.execute_query(query)

    def get_champion_abilities(self, champion_name):
        query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?x WHERE {{
            ?x rdf:type LoL:Abilità;
               LoL:ability_of LoL:{champion_name}.
        }}
        """
        return self.execute_query(query)

    def get_tank_champions_count(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT (COUNT(?y) as ?count) WHERE {
            ?x rdf:type ?y.
            VALUES ?y {LoL:Tank}.
        }
        """
        return self.execute_query(query)

    def get_dominance_runes(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        SELECT ?x WHERE {
            ?x rdf:type LoL:Rune;
               LoL:in_path LoL:Domination.
        }
        """
        return self.execute_query(query)

    def get_loadout_for_player_in_match(self, player_name):
        query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        SELECT ?loadout WHERE {{
            ?player rdf:type LoL:Player;
                    LoL:hasLoadout ?loadout.
            ?match_role rdf:type LoL:Match_role;
                        LoL:playerParticipating ?player.
            FILTER (?player = LoL:{player_name})
        }}
        """
        return self.execute_query(query)

    def get_attack_stat_objects(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        SELECT ?object WHERE {
            ?object rdf:type LoL:Oggetto;
                    LoL:has_stat ?stat.
            ?stat rdf:type LoL:Attack.
        }
        """
        return self.execute_query(query)

    def get_ability_power_scaling_champions(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?champion WHERE {
            ?champion rdf:type LoL:Campione;
                      LoL:scales_with_stat ?stat.
            ?stat rdf:type ?type.
            ?type rdfs:subClassOf LoL:Magic.
        }
        """
        return self.execute_query(query)

    def get_players_in_match(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        SELECT ?player WHERE {
            ?match_role rdf:type LoL:Match_role;
                        LoL:playerParticipating ?player.
        }
        GROUP BY ?player
        """
        return self.execute_query(query)

    def get_rune_pages_used_by_player(self, player_name):
        query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        SELECT ?rune_page WHERE {{
            ?match_role rdf:type LoL:Match_role;
                        LoL:playerParticipating LoL:{player_name}.
            ?loadout rdf:type LoL:Loadout;
                     LoL:hasRunePage ?rune_page.
        }}
        GROUP BY ?rune_page
        """
        return self.execute_query(query)

    def get_game_modes_available(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        SELECT ?mode WHERE {
            ?mode rdf:type LoL:Modalità.
        }
        """
        return self.execute_query(query)

    def get_tournaments_participated_by_player(self, player_name):
        query = f"""
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        SELECT ?label ?time WHERE {{
            SERVICE <https://query.wikidata.org/sparql> {{
                OPTIONAL {{
                    wd:Q15618298 wdt:P1344 ?link.
                }}
                OPTIONAL {{
                    ?link rdfs:label ?label;
                          wdt:P585 ?time.
                }}
            }}
            FILTER(LANG(?label) = "en")
            BIND(wd:{player_name} AS ?player)
        }}
        ORDER BY ?time
        """
        return self.execute_query(query)

    def get_teams_played_by_player(self, player_name):
        query = f"""
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        SELECT ?team WHERE {{
            SERVICE <https://query.wikidata.org/sparql> {{
                OPTIONAL {{
                    wd:{player_name} wdt:P54 ?team.
                }}
            }}
        }}
        """
        return self.execute_query(query)
