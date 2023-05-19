class Player:
    def __init__(self, database):
        self.db = database

    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name

    def create_player(self, nome, id):
        query = "CREATE (:Player {nome: $nome},{id: $id)"
        parameters = {"nome": nome, "id":id}
        self.db.execute_query(query, parameters)

    def get_player(self):
        query = "MATCH (p:Player) RETURN p.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {nome: $old_name}) SET p.nome = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, nome):
        query = "MATCH (p:Player {nome: $nome}) DETACH DELETE p"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)
