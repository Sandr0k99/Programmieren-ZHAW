import rpyc  # install on anaconda console with: pip install rpyc
ev3 = rpyc.connect('ev3-032', port=8401).root