from Workers import worker

class Union(worker.Worker):
    """gets a lot of workers and serializes them to work united as one"""

    def __init__(self):
        self._workers=[];

    def start(self,worker=None):
        if worker == None:
            for worker in self._workers:
                worker.start()
        else:
            self._workers.append(worker);

    def input(self,data):
        for w in self._workers:
            w.input(data);

    def results(self):
        for w in self._workers:
            w.results();
                    
    def addOutput(sefl, worker): 
        for w in self._workers:
            w.addOutput(worker)
