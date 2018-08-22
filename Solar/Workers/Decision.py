from Workers import worker
class Decision(worker.Worker):
    """appends a description of the state"""
    def start(self, config={
        "night-cloud":0,
        "cloud-sun":0,
        "deviation":0,
        "change-Speed":0
        }): 
        
        self._night_cloud=config.get("night-cloud")
        self._cloud_sun=config.get("cloud-sun")
        self._deviation=config.get("deviation")
        self._change_speed=config.get("change-speed")

    def input(self, data): 
        #to-do training

        
        return data
    def results(self): pass
    def addOutput(sefl, worker): pass

