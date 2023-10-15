from nicegui import ui
from main import run_command
pdf_link="https://arxiv.org/pdf/2310.07753.pdf"
def content() -> None:
    # ui.label('Mini-Elements').classes('text-h3 font-bold text-grey-8')
    # ui.html('This is <strong>HTML</strong>.')
    # with ui.image('https://user-images.githubusercontent.com/5962998/65694309-a825f000-e043-11e9-8382-db0dba0851e3.png'):
    #     ui.label('MiniElements').classes('absolute-bottom text-subtitle2 text-center')
    # ui.button('run', on_click=lambda: run_command('ll')).props('no-caps')
    # ui.markdown("""
    # # MiniElements
    # """
    # )
    ui.html(
    """
    <iframe
    src="https://udify.app/chatbot/91xP3aEFGTj6Mhuz"
    style="width: 100%; height: 100%; min-height: 700px"
    frameborder="0" 
    allow="microphone">
    </iframe>
    """
    ).classes('w-full max-w-3xl mx-auto my-6')
