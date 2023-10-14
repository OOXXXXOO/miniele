import theme

from nicegui import APIRouter, ui

router = APIRouter(prefix='/c')


@router.page('/')
def example_page():
    with theme.frame('Docs Interaction'):
        ui.label('Page').classes('text-h4 text-grey-8')
