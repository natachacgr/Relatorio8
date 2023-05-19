class Match:
    def __init__(self, database):
        self.db = database

    def __init__(self, match_id, resultado):
        self.match_id = match_id
        self.resultado = resultado
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def _create_match(self, match_id, players, resultado):
        query = "CREATE (:Match {id: $match_id, resultado: $resultado})"
        parameters = {"id": match_id, "resultado": resultado}
        for player_id in players:
            query2 = ("MATCH (p:Player {id: $player_id}) "
                   "CREATE (m:Match {id: $match_id}) "
                   "MERGE (p)-[:PARTICIPATED_IN]->(m)")
            parameters2 = {"player_id": player_id, "match_id": match_id }
        self.db.execute_query(query,query2,parameters, parameters2)

