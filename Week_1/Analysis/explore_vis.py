import pandas as pd
from pyvis.network import Network

df = pd.read_csv('controls.csv')

# Create an empty graph
G = Network()

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

# Define the layout for the graph (optional)
G.barnes_hut()

# Save the graph as an HTML file
G.save_graph('control_relationships.html')
