from nicegui import ui
import os
import re

# Function to read the content of a Markdown file
def read_markdown_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

# File path of the Markdown file to be displayed
markdown_file_path = os.path.join(os.path.dirname(__file__), 'Markdown', 'playbook.md')

# Read the content of the Markdown file
markdown_content = read_markdown_file(markdown_file_path)

# Extract Mermaid content from Markdown content
mermaid_content_match = re.search(r'```mermaid([\s\S]+?)```', markdown_content)
if mermaid_content_match:
    mermaid_content = mermaid_content_match.group(1).strip()
else:
    mermaid_content = None

with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.tabs() as tabs:
        ui.tab('A')
        ui.tab('B')
        ui.tab('C')
        ui.tab('D')  # Add a new tab 'D'

with ui.footer(value=False) as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Side menu')

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

with ui.tab_panels(tabs, value='A').classes('w-full'):
    with ui.tab_panel('A'):
        ui.input(placeholder='Enter text here')
    with ui.tab_panel('B'):
        ui.checkbox('Check me')
    with ui.tab_panel('C'):
        ui.button('Click me', on_click=lambda: ui.notify('Button clicked'))
    with ui.tab_panel('D'):  # Add a new tab panel for 'D'
        if mermaid_content:
            ui.mermaid(mermaid_content).props('class=mermaid-container')  # Apply custom class
        else:
            ui.label('No Mermaid content found in the Markdown file')

# Add custom CSS to increase the size of the Mermaid diagram
ui.add_css('''
.mermaid-container {
    width: 100%;
    height: 100%; /* Adjust height as needed */
}
''')

ui.run()
