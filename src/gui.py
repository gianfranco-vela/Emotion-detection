import sciter
import os



def get_main_window():
    frame = sciter.Window(ismain=True, uni_theme=True)
    frame.load_file("./gui/minimal.htm")
    frame.expand()
    frame.run_app()


def start_script():
    ## Start Recognition
    os.system('python emotions.py --mode display')