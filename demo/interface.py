import weakref

import numpy as np

from demo import app
import webbrowser


class Interface:
    instances = weakref.WeakSet()

    def __init__(self, fn, model, input_components, output_components, pen_size):
        if isinstance(input_components, list):
            self.inputs = list(input_components)
        else:
            self.inputs = [input_components]

        if isinstance(output_components, list):
            self.outputs = list(output_components)
        else:
            self.outputs = [output_components]
        self.model = model
        self.prediction_fn = fn
        self.pen_size = pen_size
        self.server = None
        self.port = None
        self.host = None
        Interface.instances.add(self)

    def run_prediction(self, input):
        input = [self.inputs[i].preprocess(elem) for i, elem in enumerate(input)]
        prediction = self.prediction_fn(input, self.model)
        prediction = [prediction]
        return [self.outputs[i].postprocess(elem) for i, elem in enumerate(prediction)]

    def launch(self):
        config = self.get_config_file()
        self.config = config

        app_dict = app.start_server(self)
        self.server = app_dict['app']
        thread = app_dict['thread']
        self.host = app_dict['host']
        self.port = app_dict['port']
        link = f'http://{self.host}:{self.port}/'
        webbrowser.open(link)
        self.run_until_interrupted(thread)
        return app, link

    def run_until_interrupted(self, thread):
        try:
            while True:
                pass
        except (KeyboardInterrupt, OSError):
            thread.keep_running = False

    def get_config_file(self):
        return {
            "input_interfaces": [
                (comp.__class__.__name__.lower(), comp.get_context())
                for comp in self.inputs
            ],
            "output_interfaces": [
                (comp.__class__.__name__.lower(), comp.get_context())
                for comp in self.outputs
            ],
            "pen_size": self.pen_size,
        }
