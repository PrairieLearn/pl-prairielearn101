import random, copy
import utilIAP as iap
import datetime, time

SYSTEM_EPOCH = datetime.date(*time.gmtime(0)[0:3])
NTP_EPOCH = datetime.date(1900, 1, 1)
NTP_DELTA = (SYSTEM_EPOCH - NTP_EPOCH).days * 24 * 3600

def ntp_to_system_time(date):
    """convert a NTP time to system time"""
    return date - NTP_DELTA

def system_to_ntp_time(date):
    """convert a system time to a NTP time"""
    return date + NTP_DELTA

def ntp_to_formatted(date):
    ts = datetime.datetime.fromtimestamp(date - NTP_DELTA)
    return ts.strftime('%Y/%m/%d %H:%M:%S')

def ntp_to_formatted_s(date):
    ts = datetime.datetime.fromtimestamp(date - NTP_DELTA)
    return ts.strftime('%H:%M:%S.%f')


def generate(data):

    data['params']['refid'] = random.choice(["50.205.244.28", "129.6.15.28", "50.205.244.29", "97.183.206.88"])
    rootdisp = random.uniform(0.02, 0.002)

    data['params']['rootdelay'] = "{:.6f}".format( 0.8*rootdisp*rootdisp )
    data['params']['rootdisp'] = "{:.6f}".format(rootdisp)    
    data['params']['stratum'] = random.choice([2,3])
    data['params']['hosts'] = iap.hosts_in_subnet("10.0.0.0", 16, 2)
    data['params']['port'] = random.randint(40000, 60000)
    data['params']['id'] = random.sample(range(40000, 90000), k=2)
    data['params']['ttl'] = random.randint(50, 62)
    data['params']['t1'] = system_to_ntp_time(time.time())
    data['params']['t1_s'] = "{:.9f}".format( data['params']['t1'] )
    data['params']['t1_f'] = ntp_to_formatted(data['params']['t1'])
    data['params']['owd'] = random.uniform(0.01, 0.1)
    data['params']['offset'] = random.uniform(-2, 2)
    data['params']['t2'] = system_to_ntp_time( ntp_to_system_time(  data['params']['t1']  ) + data['params']['owd'] + data['params']['offset'] + random.uniform(0.001, 0.0002)  )
    data['params']['t2_s'] = "{:.9f}".format( data['params']['t2'] )
    data['params']['t2_f'] = ntp_to_formatted(data['params']['t2'])
    data['params']['t3'] = system_to_ntp_time( ntp_to_system_time(  data['params']['t2']  ) + random.uniform(0.01, 0.02) ) 
    data['params']['t3_s'] = "{:.9f}".format( data['params']['t3'] )
    data['params']['t3_f'] = ntp_to_formatted(data['params']['t3'])
    data['params']['t4'] = system_to_ntp_time( ntp_to_system_time(  data['params']['t3']  ) + data['params']['owd'] - data['params']['offset'] + random.uniform(0.001, 0.0002)  )
    data['params']['t4_s'] = "{:.9f}".format( data['params']['t4'] )
    data['params']['t4_f'] = ntp_to_formatted(data['params']['t4'])

    data['params']['t1_t2_diff'] = "{:.9f}".format( data['params']['t1'] - data['params']['t2'] )
    data['params']['t1_t3_diff'] = "{:.9f}".format( data['params']['t1'] - data['params']['t3'] )

    data['params']['refts'] =  data['params']['t2'] - random.uniform(800, 1400)
    data['params']['ref_s'] = "{:.9f}".format( data['params']['refts'] )
    data['params']['ref_f'] = ntp_to_formatted(data['params']['refts'])
    
    data['params']['req'] = data['params']['t1']  + random.uniform(0.00001, 0.00002)
    data['params']['req_f'] = "{:.9f}".format( ntp_to_system_time(data['params']['req'])) 

    data['params']['rep_f'] = "{:.9f}".format( ntp_to_system_time(data['params']['t4'])) 
    data['params']['rep_s'] =  datetime.datetime.fromtimestamp( ntp_to_system_time(data['params']['t4']) ).strftime('%Y/%m/%d %H:%M:%S.%f')

    data['params']['opts'] = [ntp_to_formatted_s( ntp_to_system_time(data['params'][k]) ) for k in ['t1', 't2', 't3', 't4'] ]
    
    data['correct_answers']['owd_ans'] = (data['params']['t4'] - data['params']['t1']) - (data['params']['t3'] - data['params']['t2'])
    data['params']['offset'] = ( 0.5*( (data['params']['t2'] - data['params']['t1']) + (data['params']['t3'] - data['params']['t4']) ) )
    data['params']['offset_s'] = "{:.6f}".format(data['params']['offset'] )
    data['params']['offset_mag_s'] = "{:.6f}".format( abs(data['params']['offset'] ))
    data['correct_answers']['offset_ans'] = abs( data['params']['offset'] )

    data['params']['dir'] = [ data['params']['offset']>=0, data['params']['offset']<0]