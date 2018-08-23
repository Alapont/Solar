from Workers import worker
class Decision(worker.Worker):
    """appends a description of the state"""
    def start(self, config={}):   
        self._night_cloud=config.get("night-cloud",100.0)
        self._cloud_sun=config.get("cloud-sun",600.0)
        self._deviation=config.get("deviation",100.0)
        self._change_speed=config.get("change-speed",0.0)

    def input(self, data): 
        #to-do training
        if data.get("sigma")>self._deviation:
            decision="outcast"
        else:
            if data.get("mean")<self._night_cloud:
                decision="Night"
            elif data.get("mean")>self._cloud_sun:
                decision="sunny"
            else:
                decision="cloudy"
        data.add([["decision",decision]])
        return data
    def results(self): pass
    def addOutput(sefl, worker): pass

