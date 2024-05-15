from pyvis.network import Network

def mermaid_to_pyvis(mermaid_diagram):
    # Extract nodes and edges from the Mermaid diagram
    nodes = []
    edges = []

    # Split the diagram into lines and process each line
    lines = mermaid_diagram.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith("graph LR"):
            continue
        elif line.startswith("    "):
            if "-->" in line:  # Edge
                parts = line.split("-->")
                source = parts[0].strip()
                target = parts[1].strip()
                edges.append((source, target))
            else:  # Node
                parts = line.split("(")
                node_id = parts[0].strip()
                label = parts[1].split(")")[0].strip()
                nodes.append((node_id, label))

    # Create a Pyvis network
    net = Network(directed=True)
    
    # Add nodes and edges to the network
    for node_id, label in nodes:
        net.add_node(node_id, label=label)
    for source, target in edges:
        net.add_edge(source, target)

    return net

if __name__ == "__main__":
    # Example Mermaid diagram
    mermaid_diagram = """
    graph LR
        B1(Problem Identification and Change Initiation)
        B2(Change Control Record Creation)
        B3(Communication and Risk Assessment)
        B4(Documentation and Evaluation)
        B5(Fulfillment and Closure)

        B1 --> B2
        B2 --> B3
        B3 --> B4
        B4 --> B5
    """

    # Create Pyvis network from Mermaid diagram
    net = mermaid_to_pyvis(mermaid_diagram)

    # Show the network
    net.show("mermaid_network.html")
