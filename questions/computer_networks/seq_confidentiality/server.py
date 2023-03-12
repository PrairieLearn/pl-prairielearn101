import random, copy

def generate(data):
    
    
    data['params']['sender'] = "alice"
    data['params']['recv'] = "bob"


    activities = [
        {"type": "file transfer", "insecure": "uses FTP to retrieve a file from", "secure": "uses SCP to retrieve a file from", 
            "data": [data['params']['sender'] + "'s username and password", "name of the file that was transferred", "contents of the file that was transferred"], 
            "connInsecure": "port 21 (well-known FTP port)",
            "connSecure": "port 22 (well-known SSH/SCP port)" 
        },
        {"type": "remote login", "insecure": "uses telnet to log in and execute commands on", "secure": "uses SSH to log in and execute commands on", 
            "data": [data['params']['sender'] + "'s username and password", "commands that " + data['params']['sender'] + " runs on " + data['params']['recv'], "output of commands that " + data['params']['sender'] + " runs on " + data['params']['recv']],
            "connInsecure": "port 23 (well-known telnet port)",
            "connSecure": "port 22 (well-known SSH/SCP port)" 
        },
        {"type": "web", "insecure": "uses HTTP to fill in an HTML form on a web page at", "secure": "uses HTTPS to fill in an HTML form on a web page at", 
            "data": [data['params']['sender'] + "'s form data", "HTTP request and response headers", "contents of the HTML file that was transferred"],
            "connInsecure": "port 80 (well-known HTTP port)",
            "connSecure": "port 443 (well-known HTTPS port)" 
        }
        ]

    act = random.choice(activities)

    data['params']['descS'] = act['secure']
    data['params']['desc'] = act['insecure']
    data['params']['item'] = random.choice(act['data'])
    data['params']['connInsecure'] = act['connInsecure']
    data['params']['connSecure'] = act['connSecure']
    data['params']['names'] = ["evelyn", "eve", "evelina", "evangeline", "evie", "everly", "evita"]
    # random.shuffle(data['params']['names'])
    data['params']['conn-insecure'] = ['true', 'false', 'true', 'true', 'true', 'true', 'false']
    data['params']['item-insecure'] = ['true', 'false', 'true', 'true', 'true', 'true', 'false']
    data['params']['conn-vpn'] =    ['false', 'false', 'false', 'false', 'false', 'false', 'true']
    data['params']['item-vpn']     = ['false', 'false', 'false', 'true', 'true', 'true', 'true']
    data['params']['item-secure']   = ['false', 'false', 'false', 'false', 'false', 'true', 'false']

    data['params']['opts'] = [{'ans': 'eve-1', 'tag': 'true'}, {'ans': 'eve-2', 'tag': 'true'}, {'ans': 'eve-3', 'tag': 'false'}]
    
    
    # maybe ask reasons too? "because the packet does not traverse this network" "because the data is encrypted" "because this data was never in the packet"
    # ask about what if a malicious user can manipulate network protocols, e.g. advertise BGP routes that cause the packet to go through an ISP, flood bridge to turn off MAC learning, etc.