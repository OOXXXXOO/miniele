from nicegui import ui


def menu() -> None:
    ui.link('MiniElements', '/').classes(replace='text-white')
    ui.link('MultiModal', '/a').classes(replace='text-white')
    ui.link('Finical Analysis', '/b').classes(replace='text-white')
    # ui.link('Doc', '/c').classes(replace='text-white')
    ui.link('Auto', '/d').classes(replace='text-white')
