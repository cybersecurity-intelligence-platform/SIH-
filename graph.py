import networkx as nx

# Create criminal investigation network
G = nx.Graph()

# Add persons
G.add_node("Rahul Patil", type="Person")
G.add_node("Amit Sharma", type="Person")
G.add_node("Sneha Joshi", type="Person")
G.add_node("Vikas More", type="Person")

# Add cases
G.add_node("C001", type="Case")
G.add_node("C002", type="Case")

# Add relationships
G.add_edge("Rahul Patil", "C001", relation="INVOLVED_IN")
G.add_edge("Amit Sharma", "C001", relation="INVOLVED_IN")
G.add_edge("Sneha Joshi", "C002", relation="INVOLVED_IN")
G.add_edge("Vikas More", "C002", relation="INVOLVED_IN")

# Display graph information
print("\n=== NETWORKX GRAPH ANALYTICS ===\n")

print("Total Nodes:", G.number_of_nodes())
print("Total Relationships:", G.number_of_edges())

print("\nRelationships:")

for person, case, data in G.edges(data=True):
    print(f"{person} --[{data['relation']}]--> {case}")

print("\nNode Connections:")

for node in G.nodes():
    print(f"{node}: {G.degree(node)} connection(s)")