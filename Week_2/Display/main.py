from nicegui import app, ui
from nicegui.events import KeyEventArguments
from pathlib import Path
import os

def create_ui():
    with ui.card().tight():
        ui.image('https://picsum.photos/id/684/640/360')
        with ui.card_section():
            ui.label('Welcome To Web Design')
            
    with ui.expansion('Expand!', icon='work').classes('w-full'):
        ui.label('inside the expansion')

    # Adjusting the UI
    ui.query('.nicegui-content').classes('p-0')  # remove padding from the main content

    # Function to handle keyboard events
    def handle_key(event: KeyEventArguments) -> None:
        global state
        if event.action.keydown:
            if event.key.arrow_right:
                state['index'] += 1
            if event.key.arrow_left:
                state['index'] -= 1
            state['index'] %= len(files)
            slide.set_source(f'slides/{files[state["index"]]}')

    # Get the directory of the slides
    folder = Path(__file__).parent / 'slides'  

    # Get a sorted list of files in the slides directory
    files = sorted(f.name for f in folder.glob('*.jpg'))

    # Initial state
    state = {'index': 0}

    # Add the files in the 'slides' directory to serve them statically
    app.add_static_files('/slides', folder)  

    # Create the image widget to display the slides
    slide = ui.image(f'slides/{files[state["index"]]}')  

    # Handle keyboard events
    ui.keyboard(on_key=handle_key)  

    # Welcome Message
    welcome_message = """
    <h1>Welcome to NiceGUI!</h1>
    <p>NiceGUI is a Python package designed to simplify the creation of graphical user interfaces (GUIs).</p>
    <p>It offers a variety of widgets and layout managers, enabling you to design intuitive interfaces for your Python applications effortlessly.</p>
    <p>Let's embark on a journey to create amazing GUIs with NiceGUI!</p>
    """

    # Define Widgets and Demos
    # Button with Badge
    with ui.button('Click me!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
        badge = ui.badge('0', color='red').props('floating')

    # Toggles
    toggle_description = """
    <h2>Toggles</h2>
    <p>Toggle options can be specified as a list of values or a dictionary mapping values to labels.</p>
    <p>After modifying the options, use update() to refresh the UI.</p>
    """
    ui.html(toggle_description)
    toggle1 = ui.toggle([1, 2, 3], value=1)
    toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(toggle1, 'value')

    # Radio Buttons
    radio1 = ui.radio([1, 2, 3], value=1).props('inline')
    radio2 = ui.radio({1: 'A', 2: 'B', 3: 'C'}).props('inline').bind_value(radio1, 'value')

    # Additional Widgets
    checkbox = ui.checkbox('Check me')
    ui.label('Check!').bind_visibility_from(checkbox, 'value')

    switch = ui.switch('Switch me')
    ui.label('Switch!').bind_visibility_from(switch, 'value')

    slider = ui.slider(min=0, max=100, value=50)
    ui.label().bind_text_from(slider, 'value')

    min_max_range = ui.range(min=0, max=100, value={'min': 20, 'max': 80})
    ui.label().bind_text_from(min_max_range, 'value',
                            backward=lambda v: f'min: {v["min"]}, max: {v["max"]}')

    ui.joystick(color='blue', size=50,
                on_move=lambda e: coordinates.set_text(f'{e.x:.3f}, {e.y:.3f}'),
                on_end=lambda _: coordinates.set_text('0, 0'))
    coordinates = ui.label('0, 0')

    ui.input(label='Text', placeholder='Start typing',
            on_change=lambda e: result.set_text('You typed: ' + e.value),
            validation={'Input too long': lambda value: len(value) < 20})
    result = ui.label()

    knob = ui.knob(0.3, show_value=True)

    with ui.knob(color='orange', track_color='grey-2').bind_value(knob, 'value'):
        ui.icon('volume_up')

    label = ui.label('Change my color!')
    ui.color_input(label='Color', value='#000000',
                on_change=lambda e: label.style(f'color:{e.value}'))

    ui.date(value='2023-01-01', on_change=lambda e: result.set_text(e.value))
    result = ui.label()

    ui.time(value='12:00', on_change=lambda e: result.set_text(e.value))
    result = ui.label()

    ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')

    # File directory widget
    current_directory = os.getcwd()
    directory_label = ui.label(f'This script is in Directory: {os.getcwd()}')

    # Display Welcome Message
    ui.html(welcome_message)

    # Run the UI
    ui.run()

# Call the function to create the UI
create_ui()
