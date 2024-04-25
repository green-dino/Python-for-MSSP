import pandas as pd
import networkx as nx
import plotly.graph_objects as go

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

# Create a Plotly figure for the graph
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=False,
        colorscale='YlGnBu',
        size=10,
        line_width=2))

node_trace.text = list(G.nodes())

fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Control Relationships',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[dict(
                        text="",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002)],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

# Save the Plotly figure as an HTML file
fig.write_html("control_relationships.html")
