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
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?label ?comment
        WHERE {
            ?x rdf:type LoL:Assassin.
            OPTIONAL { ?x rdfs:label ?label }
            OPTIONAL { ?x rdfs:comment ?comment }
        }

        """
        return self.execute_query(query)

    def get_players_list(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select ?y ?label ?comment
        where {
            ?x rdf:type LoL:Match_role;
            LoL:playerParticipating ?y.
            OPTIONAL { ?x rdfs:label ?label }
            OPTIONAL { ?x rdfs:comment ?comment }
        }
        GROUPBY ?y ?label ?comment

        """
        return self.execute_query(query)

    def get_champion_abilities(self):
        ## di zed 
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select ?x ?label ?comment
        where {
            ?x rdf:type LoL:Abilità;
            LoL:ability_of ?y.
            VALUES ?y {LoL:Zed}.
            OPTIONAL { ?x rdfs:label ?label }
            OPTIONAL { ?x rdfs:comment ?comment }
        }
        """
        return self.execute_query(query)

    def get_tank_champions_count(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select (count(?y) as ?count)
        where {
            ?x rdf:type ?y.
            VALUES ?y {LoL:Tank}.
        }

        """
        return self.execute_query(query)

    def get_dominance_runes(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select  ?label ?comment
        where{
            ?x rdf:type LoL:Rune;
            LoL:in_path LoL:Domination.
            OPTIONAL { ?x rdfs:label ?label }
            OPTIONAL { ?x rdfs:comment ?comment }

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
        PREFIX : <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select  ?label ?comment
        where {
            ?x rdf:type LoL:Oggetto;
            LoL:has_stat ?y.
            ?y rdf:type LoL:Attack.
            OPTIONAL { ?x rdfs:label ?label }
            OPTIONAL { ?x rdfs:comment ?comment }

        }
        """
        return self.execute_query(query)

    def get_ability_power_scaling_champions(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select ?label ?comment
        where {
            ?x rdf:type LoL:Campione;
            LoL:scales_with_stat ?y.
            ?y rdf:type ?z.
            ?z rdfs:subClassOf LoL:Magic.
            OPTIONAL { ?x rdfs:label ?label }
            OPTIONAL { ?x rdfs:comment ?comment }
        }
        """
        return self.execute_query(query)

    def get_players_in_match(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select ?y ?label ?comment
        where {
            ?x rdf:type LoL:Match_role;
            LoL:playerParticipating ?y.
            OPTIONAL { ?x rdfs:label ?label }
            OPTIONAL { ?x rdfs:comment ?comment }
        }
        GROUPBY ?y ?label ?comment
        """
        return self.execute_query(query)

    def get_rune_pages_used_by_player(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        select ?label ?comment
        where {
            ?z rdf:type LoL:Rune_Page.
            ?y rdf:type LoL:Loadout.
            ?x rdf:type LoL:Match_role;
            LoL:playerParticipating LoL:Faker.
            OPTIONAL { ?z rdfs:label ?label }
            OPTIONAL { ?z rdfs:comment ?comment }
            
        }
        GROUPBY  ?label ?comment

        """
        return self.execute_query(query)

    def get_game_modes_available(self):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX LoL: <http://www.semanticweb.org/drunkfazor/ontologies/2024/2/LoL#>
        select ?label ?comment
        where {
            ?x rdf:type LoL:Modalità.
            OPTIONAL { ?x rdfs:label ?label }
            OPTIONAL { ?x rdfs:comment ?comment }
        }

        """
        return self.execute_query(query)

    def get_tournaments_participated_by_player(self):
        query = """
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        SELECT ?label ?time
        WHERE {
            SERVICE <https://query.wikidata.org/sparql>{
                OPTIONAL {
                    wd:Q15618298 wdt:P1344 ?link
                }
                OPTIONAL {
                    ?link rdfs:label ?label;
                    wdt:P585 ?time.
                }
            }
            FILTER(LANG(?label) = "en")
        }
        ORDERBY ?time

        """
        return self.execute_query(query)

    def get_teams_played_by_player(self):
        query = """
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select  ?label  ?comment
        WHERE {
            SERVICE <https://query.wikidata.org/sparql>{
            OPTIONAL{
                wd:Q18608567 wdt:P54 ?team
            }
            OPTIONAL { ?team rdfs:label ?label }
            OPTIONAL { ?team rdfs:comment ?comment }
                FILTER(LANG(?label) = "en")

            }
        }

        """
        return self.execute_query(query)
