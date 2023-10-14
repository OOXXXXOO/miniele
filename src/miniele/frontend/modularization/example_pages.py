import theme

from nicegui import ui


def create() -> None:

    @ui.page('/a')
    def example_page_a():
        with theme.frame('MultiModal Parse'):
            ui.label('MultiModal Parse').classes('text-h4 text-grey-8')












    @ui.page('/b')
    def example_page_b():
        with theme.frame('Finical Analysis'):
            ui.label('Finical Analysis').classes('text-h4 text-grey-8')












    @ui.page('/d')
    def example_page_b():
        with theme.frame('Auto'):
            ui.label('Auto').classes('text-h4 text-grey-8')
