class Worker(object):
    """Worker mashup recieves data as multiple inputs and does something"""
    def start(self, config): pass
    def input(self, data): return data
    def results(self, destiny): pass
    def addOutput(sefl, worker): pass

    #good ol ASCII-UML
    """
    [<<abstract>>]
    [   worker   ]
    [------------]----------->[minMax]
    [+start      ]----------->[PNGMaker]
    [+input(data)]              \/
    [+results    ]----------->[GifMaker]
    """