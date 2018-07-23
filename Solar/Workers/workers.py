import Workers.worker
class Workers(worker):
    #gets a lot of workers and serializes them to work united as one
    def __init__(self):
        self.workers=[];
    def start(self,worker=None):
        if worker == None:
            for worker in self.workers:
                worker.start()
        else:
            self.workers.append(worker);
    def input(self,data):
        for w in self.workers:
            w.input(data);
    def results(self):
        for w in self.workers:
            w.results();
