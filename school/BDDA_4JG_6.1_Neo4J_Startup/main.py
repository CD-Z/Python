from py2neo import Graph
graph = Graph("bolt://10.115.2.20:7687", auth=("neo4j", "test"))
nodes = graph.run("Match (n) Return n LIMIT 10").data()


def main():
    for node in nodes:
        print(node)


if __name__ == "__main__":
    main()
