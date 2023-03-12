import random, copy
import utilIAP as iap

def parse(data):
    if 'static-mac' in data['submitted_answers']:
        data['submitted_answers']['static-mac'] = data['submitted_answers']['static-mac'].replace(":", "-").upper()
        
def grade(data):
    
    # specifying the port is also OK
    if ('url-external-ip' in data['submitted_answers'] and data['submitted_answers']['url-external-ip'] == "67.80.124.24:80"):
        data["partial_scores"]["url-external-ip"]['score'] = 1

    
    # check static IP assignment
    if ('static-ip' in data['submitted_answers'] 
        and iap.is_dotdec(data['submitted_answers']['static-ip'])
        and iap.ip_dotdec_to_int("192.168.0.1") < iap.ip_dotdec_to_int(data['submitted_answers']['static-ip']) < iap.ip_dotdec_to_int("192.168.0.255") ):
            data["partial_scores"]["static-ip"]['score'] = 1
    else:
            data["partial_scores"]["static-ip"]['score'] = 0

    # check static IP assignment matches internal IP
    if ('nat-internal-ip' in data['submitted_answers'] 
        and 'static-ip' in data['submitted_answers'] 
        and data["partial_scores"]["static-ip"]['score'] == 1
        and data['submitted_answers']['static-ip']==data['submitted_answers']['nat-internal-ip']):
            data["partial_scores"]["nat-internal-ip"]['score'] = 1
    else:
            data["partial_scores"]["nat-internal-ip"]['score'] = 0

    # check port if it's not 80
    if ('nat-external-port' in data['submitted_answers'] 
        and 'url-external-ip' in data['submitted_answers'] 
        and data['submitted_answers']['nat-external-port']!=80 
        and 1 <= data['submitted_answers']['nat-external-port'] <= 65535):
            if data['submitted_answers']['url-external-ip'] == "67.80.124.24:%d" % data['submitted_answers']['nat-external-port']:
                data["partial_scores"]["nat-external-port"]['score'] = 1
                data["partial_scores"]["url-external-ip"]['score'] = 1
            else:
                data["partial_scores"]["url-external-ip"]['score'] = 0
                
    data['score'] = sum([data["partial_scores"][c]['weight']*data["partial_scores"][c]['score'] for c in data["partial_scores"].keys()])/sum([data["partial_scores"][c]['weight'] for c in data["partial_scores"].keys()])


def generate(data):

    data['params']['host'] = iap.hosts_in_subnet("192.168.0.128", 28, 1)[0]
    data['correct_answers']['static-mac'] = data['params']['host']['mac'].replace(":", "-").upper()
    data['correct_answers']['static-ip'] = data['params']['host']['ip']
    data['correct_answers']['nat-external-port'] = 80
    data['correct_answers']['nat-internal-port'] = 80
    data['correct_answers']['nat-internal-ip'] = data['params']['host']['ip']
    data['correct_answers']['url-external-ip'] = "67.80.124.24"
    