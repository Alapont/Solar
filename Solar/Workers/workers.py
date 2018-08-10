import Workers.worker
class Workers(object):
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
    def results(self,destiny=None):
        for w in self.workers:
            w.results(destiny);
            
    def addOutput(sefl, worker): pass#To-Do
