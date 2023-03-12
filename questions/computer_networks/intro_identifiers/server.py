import random, copy
import utilIAP as iap

def generate(data):

    data['params']['mac'] = iap.macs(1)[0]
    data['params']['name'] = "%s.nyu.edu" % iap.hostnames(1)[0]
    x = random.sample(range(11,99), 4)
    data['params']['ip'] = "%d.%d.%d.%d" % (x[0], x[1], x[2], x[3])