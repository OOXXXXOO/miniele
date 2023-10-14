from nicegui import ui
from main import run_command

def content() -> None:
    ui.label('This is the home page.').classes('text-h4 font-bold text-grey-8')
    # ui.button('run', on_click=lambda: run_command('ll')).props('no-caps')
