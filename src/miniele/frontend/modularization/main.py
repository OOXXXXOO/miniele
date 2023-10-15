#!/usr/bin/env python3
# import example_c
import example_pages
import home_page
import theme

from nicegui import app, ui

import asyncio
import os.path
import platform
import shlex
import sys


async def run_command(command: str) -> None:
    """Run a command in the background and display the output in the pre-created dialog."""
    dialog.open()
    result.content = ''
    command = command.replace('python3', sys.executable)  # NOTE replace with machine-independent Python path (#1240)
    process = await asyncio.create_subprocess_exec(
        *shlex.split(command, posix="win" not in sys.platform.lower()),
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT,
        cwd=os.path.dirname(os.path.abspath(__file__))
    )
    # NOTE we need to read the output in chunks, otherwise the process will block
    output = ''
    while True:
        new = await process.stdout.read(4096)
        if not new:
            break
        output += new.decode()
        # NOTE the content of the markdown element is replaced every time we have new output
        result.content = f'```\n{output}\n```'
        
        
with ui.dialog() as dialog, ui.card():
    result = ui.markdown()


# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame('HOME'):
        home_page.content()



# this call shows that you can also move the whole page creation into a separate file
example_pages.create()

# we can also use the APIRouter as described in https://nicegui.io/documentation/page#modularize_with_apirouter
# app.include_router(example_c.router)

ui.run(title='Elements.AI',port=8999,reload=platform.system() != 'Windows')
