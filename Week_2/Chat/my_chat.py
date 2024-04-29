#!/usr/bin/env python3
from datetime import datetime
from typing import List, Tuple, Union
from uuid import uuid4

from nicegui import ui

messages: List[Tuple[str, str, Union[str, List[str]], str]] = []


@ui.refreshable
def chat_messages(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        if isinstance(text, list):
            for part in text:
                ui.chat_message(text=part.replace('\n', '<br>'), stamp=stamp, avatar=avatar, sent=own_id == user_id)
        else:
            ui.chat_message(text=text.replace('\n', '<br>'), stamp=stamp, avatar=avatar, sent=own_id == user_id)
    ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')



def send(user_id: str, avatar: str, text_input: ui.element) -> None:
    stamp = datetime.utcnow().strftime('%X')
    messages.append((user_id, avatar, text_input.value, stamp))
    text_input.value = ''
    chat_messages.refresh()


@ui.page('/')
async def main():
    user_id = str(uuid4())
    avatar = f'https://robohash.org/{user_id}?bgset=bg2'

    ui.add_css(r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}')
    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
        with ui.row().classes('w-full no-wrap items-center'):
            with ui.avatar().on('click', lambda: ui.navigate.to(main)):
                ui.image(avatar)
            text_input = ui.input(placeholder='message').on('keydown.enter', lambda: send(user_id, avatar, text_input)) \
                .props('rounded outlined input-class=mx-3').classes('flex-grow')
        ui.markdown('simple chat app built with [NiceGUI](https://nicegui.io)') \
            .classes('text-xs self-end mr-8 m-[-1em] text-primary')

    with ui.column().classes('w-full max-w-2xl mx-auto items-stretch'):
        chat_messages(user_id)

ui.run()
