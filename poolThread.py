from concurrent import futures


class Pool():

    def __init__(self, max_worker = None) -> None:

        self.MAX_WORKERS = 1 if (max_worker == None) else max_worker
        self.work_progress = {}
        self.callback = {}

    def initialize_pool(self):
        self.workers = futures.ThreadPoolExecutor(self.MAX_WORKERS)

    def execute_function(self, name, annotations, callback, function, *kwargs):

        result = self.workers.submit(function, *kwargs)
        result.__annotations__ = annotations
        self.work_progress.setdefault(name, result)
        result.add_done_callback(self.callback[callback])




    