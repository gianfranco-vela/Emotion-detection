import sciter
import src.emotions as es
import threading


class Frame(sciter.Window):

    def __init__(self):
        self.detection_thread = threading.Thread(target=es.start_detection, args=('display',), daemon=True)
        super().__init__(ismain=True, uni_theme=True, debug=False)

    @sciter.script('start')
    def start_script(self):
        self.detection_thread.start()
        print('Starting Emotion-Detection....')

    @sciter.script('stop')
    def stop_script(self):
        es.stop_executing = True
        self.detection_thread.join()
        print('Stopping Emotion-Detection....')


def get_main_window():
    frame = Frame()
    frame.load_file("./gui/minimal.htm")
    frame.expand()
    frame.run_app()
