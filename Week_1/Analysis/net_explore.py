import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('controls.csv')

# Create an empty graph
G = nx.Graph()

# Process the "Control Identifier" and "Related Controls" columns to add edges to the graph
for index, row in df.iterrows():
    control_identifier = row['identifier']
    related_controls = row['related']
    
    if not pd.isna(related_controls):
        related_controls = related_controls.split(', ')

        # Add nodes for the control and related controls
        G.add_node(control_identifier)
        for related_control in related_controls:
            G.add_node(related_control)
            G.add_edge(control_identifier, related_control)

# Define the layout for the graph
pos = nx.spring_layout(G, seed=42)

# Draw nodes and edges
nx.draw_networkx_nodes(G, pos, node_size=200, node_color='skyblue', alpha=0.8)
nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.5, edge_color='#888')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')

plt.title('Control Relationships')
plt.axis('off')

# Save the figure as an image file
plt.savefig("control_relationships.png", format="PNG")
plt.show()
