from database import Database
from player import Player


# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.91.207.90:7687", "neo4j", "park-handles-pitches")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
playerDatabase = Player(db)

# Criando alguns professores
db.create_player("Alice", "player1")
db.create_player("Bob", "player2")
db.create_player("Charlie", "player3")

db.update_player("player2", "Bobby")

players = ["player1", "player2"]
result = "player1_win"  # Exemplo de resultado da partida
db.create_match("match1", players, result)

players = db.get_players()
print("Lista de jogadores:")
for player in players:
    print(f"ID: {player[0]}, Nome: {player[1]}")

# Fechando a conexão
db.close()