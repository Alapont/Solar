class Worker(object):
    """Worker mashup recieves data as multiple inputs and does something"""
    def start(): None;
    def input(data): None;
    def results(): None;

    #good ol ASCII-UML
    """
    [<<abstract>>]
    [   worker   ]
    [------------]----------->[minMax]
    [+start      ]----------->[PNGMaker]
    [+input(data)]              \/
    [+results    ]----------->[GifMaker]
    """