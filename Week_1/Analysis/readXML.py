import xml.etree.ElementTree as ET

def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None

def analyze_controls(xml_file):
    root = parse_xml(xml_file)
    if root is None:
        print("Error parsing XML file.")
        return

    # Define namespaces
    namespaces = {
        'controls': 'http://scap.nist.gov/schema/sp800-53/feed/2.0'
    }

    # Analyze control information
    controls = root.findall('.//controls:control', namespaces)
    control_data = []
    for control in controls:
        control_info = {
            'family': control.find('family', namespaces).text,
            'number': control.find('number', namespaces).text,
            'title': control.find('title', namespaces).text,
            'statements': []
        }
        statements = control.findall('.//controls:statement', namespaces)
        for statement in statements:
            statement_info = {
                'number': statement.find('number', namespaces).text,
                'description': statement.find('description', namespaces).text
            }
            control_info['statements'].append(statement_info)
        control_data.append(control_info)

    # Print analysis
    for control in control_data:
        print(f"Control Family: {control['family']}")
        print(f"Control Number: {control['number']}")
        print(f"Control Title: {control['title']}")
        print("Statements:")
        for statement in control['statements']:
            print(f" - {statement['number']}: {statement['description']}")
        print()

# Example usage
xml_file = "controls.xml"
analyze_controls(xml_file)
