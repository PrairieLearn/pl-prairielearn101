import random, copy

def generate(data):
    
    data['params']['cport'] = random.randint(49152,65535)
    data['params']['sport'] = random.randint(1000,4000)
    data['params']['client'] = "10.%d.%d.%d" % (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)) 
    data['params']['server'] = "10.%d.%d.%d" % (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)) 
    data['params']['isn1'] = random.randint(1e9, 4294967295)
    data['params']['isn2'] = random.randint(1e9, 4294967295)
    data['params']['l1'] = len("Hello ECE-GY 6353")
    data['params']['ack1'] = data['params']['isn1']+1
    data['params']['ack2'] = data['params']['isn2']+1
    data['params']['seq3'] = data['params']['ack1']
    data['params']['ack3'] = data['params']['ack2']
    data['params']['ack4'] = data['params']['seq3']+ data['params']['l1']
    data['params']['seq5'] = data['params']['ack4']
    data['params']['ack5'] = data['params']['ack2']
    data['params']['seq6'] = data['params']['ack5']
    data['params']['ack6'] = data['params']['seq5']+1
    data['params']['ack7'] = data['params']['seq6']+1
    
    
    opts = random.choice([0,1, 2])
    
    if opts==0:

        states_client_close = ['CLOSED', 'SYN_SENT', 'ESTABLISHED', 'FIN_WAIT_1', 'FIN_WAIT_2', 'TIME_WAIT', 'CLOSED']
        
        trans_client_close = [
            'sends the following TCP packet: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [S], ' + '\n' + '\t' + 
            'seq ' + str(data['params']['isn1']) + ', win 64240, options [mss 1460,sackOK,wscale 7], length 0</pl-code>',
    
            'receives the following TCP packet: <pl-code language="text">' + data['params']['server'] + '.' + str(data['params']['sport']) + 
            ' > ' + data['params']['client'] + '.' + str(data['params']['cport'])  + ': Flags [S.], ' + '\n' + '\t' + 
            'seq ' + str(data['params']['isn2']) + ', ack ' + str(data['params']['ack1']) + ', win 65160, '  + '\n' + '\t' + 'options [mss 1460,sackOK,wscale 7], length 0</pl-code>' + '\n' +
            'and sends this one: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [.],'  + '\n' + '\t' + 
            'ack ' + str(data['params']['ack2']) + ', win 502, length 0</pl-code>',
    
            'sends the following TCP packet: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [F.],  ' + '\n' + '\t' + 
            'seq ' + str(data['params']['seq5']) + ', ack ' + str(data['params']['ack5']) + ', win 502, length 0</pl-code>',
            
            'receives the following TCP packet, which ACKs its FIN: <pl-code language="text">' + data['params']['server'] + '.' + str(data['params']['sport']) + 
            ' > ' + data['params']['client'] + '.' + str(data['params']['cport'])  + ': Flags [.], ' + '\n' + '\t' + 
            'ack ' + str(data['params']['ack6']) + ', win 510, length 0</pl-code>',
            
            'receives the following TCP packet: <pl-code language="text">' + data['params']['server'] + '.' + str(data['params']['sport']) + 
            ' > ' + data['params']['client'] + '.' + str(data['params']['cport'])  + ': Flags [F.], ' + '\n' + '\t' + 
            'seq ' + str(data['params']['seq6']) + ', ack ' + str(data['params']['ack4']) + ', win 510, length 0</pl-code>' + '\n' +
            'and sends this one: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [.],'  + '\n' + '\t' + 
            'ack ' + str(data['params']['ack7']) + ', win 502, length 0</pl-code>',
    
            'a timer equal to 2 times the maximum segment lifetime elapses.'
    
                    ]
    
        init = random.randint(0, 5)
        data['params']['endpoint'] = "client"
        data['params']['starting'] = states_client_close[init]
        data['params']['next'] = trans_client_close[init]
        
        data['params']['mc'] = [{'tag': state, 'ans': "true"} if i==init else {'tag': state, 'ans': "false"} for i, state in enumerate(states_client_close[1:]) ]

    elif opts==1:
                
        states_client_simul = ['CLOSED', 'SYN_SENT', 'ESTABLISHED', 'FIN_WAIT_1', 'TIME_WAIT', 'CLOSED']
    
        trans_client_simul = [
            'sends the following TCP packet: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [S], ' + '\n' + '\t' + 
            'seq ' + str(data['params']['isn1']) + ', win 64240, options [mss 1460,sackOK,wscale 7], length 0</pl-code>',
    
            'receives the following TCP packet: <pl-code language="text">' + data['params']['server'] + '.' + str(data['params']['sport']) + 
            ' > ' + data['params']['client'] + '.' + str(data['params']['cport'])  + ': Flags [S.], ' + '\n' + '\t' + 
            'seq ' + str(data['params']['isn2']) + ', ack ' + str(data['params']['ack1']) + ', win 65160, '  + '\n' + '\t' + 'options [mss 1460,sackOK,wscale 7], length 0</pl-code>' + '\n' +
            'and sends this one: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [.],'  + '\n' + '\t' + 
            'ack ' + str(data['params']['ack2']) + ', win 502, length 0</pl-code>',
    
            'sends the following TCP packet: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [F.],  ' + '\n' + '\t' + 
            'seq ' + str(data['params']['seq5']) + ', ack ' + str(data['params']['ack5']) + ', win 502, length 0</pl-code>',
            
            'receives the following TCP packet, which ACKs its FIN: <pl-code language="text">' + data['params']['server'] + '.' + str(data['params']['sport']) + 
            ' > ' + data['params']['client'] + '.' + str(data['params']['cport'])  + ': Flags [F.], ' + '\n' + '\t' + 
            'seq ' + str(data['params']['seq6']) + ', ack ' + str(data['params']['ack4']) + ', win 510, length 0</pl-code>' + '\n' +
            'and sends this one: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [.],'  + '\n' + '\t' + 
            'ack ' + str(data['params']['ack7']) + ', win 502, length 0</pl-code>',
    
            'a timer equal to 2 times the maximum segment lifetime elapses.'
    
                    ]
    
    
        init = random.randint(0, 4)
        data['params']['endpoint'] = "client"
        data['params']['starting'] = states_client_simul[init]
        data['params']['next'] = trans_client_simul[init]
        
        data['params']['mc'] = [{'tag': state, 'ans': "true"} if i==init else {'tag': state, 'ans': "false"} for i, state in enumerate(states_client_simul[1:]) ]

    elif opts==2:


        states_server = ['CLOSED', 'LISTEN', 'SYN_RCVD', 'ESTABLISHED', 'CLOSE_WAIT', 'LAST_ACK', 'CLOSED']
        trans_server = [
            'binds a TCP socket to an address and port, and calls <code>listen()</code> on the socket.',
            
            'receives the following TCP packet: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [S], ' + '\n' + '\t' + 
            'seq ' + str(data['params']['isn1']) + ', win 64240, options [mss 1460,sackOK,wscale 7], length 0</pl-code>' + 'n' + 
            'and sends this one: <pl-code language="text">' + data['params']['server'] + '.' + str(data['params']['sport']) + 
            ' > ' + data['params']['client'] + '.' + str(data['params']['cport'])  + ': Flags [S.], ' + '\n' + '\t' + 
            'seq ' + str(data['params']['isn2']) + ', ack ' + str(data['params']['ack1']) + ', win 65160, '  + '\n' + '\t' + 'options [mss 1460,sackOK,wscale 7], length 0</pl-code>',


            'receives this TCP packet, which ACKs its SYN: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [.],'  + '\n' + '\t' + 
            'ack ' + str(data['params']['ack2']) + ', win 502, length 0</pl-code>',
            
            'receives the following TCP packet: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [F.],  ' + '\n' + '\t' + 
            'seq ' + str(data['params']['seq5']) + ', ack ' + str(data['params']['ack5']) + ', win 502, length 0</pl-code>' +
            'and sends this one: <pl-code language="text">' + data['params']['server'] + '.' + str(data['params']['sport']) + 
            ' > ' + data['params']['client'] + '.' + str(data['params']['cport'])  + ': Flags [.], ' + '\n' + '\t' + 
            'ack ' + str(data['params']['ack6']) + ', win 510, length 0</pl-code>',

            'sends the following TCP packet: <pl-code language="text">' + data['params']['server'] + '.' + str(data['params']['sport']) + 
            ' > ' + data['params']['client'] + '.' + str(data['params']['cport'])  + ': Flags [F.], ' + '\n' + '\t' + 
            'seq ' + str(data['params']['seq6']) + ', ack ' + str(data['params']['ack4']) + ', win 510, length 0</pl-code>',

            'receives this TCP packet, which ACKs its FIN: <pl-code language="text">' + data['params']['client'] + '.' + str(data['params']['cport']) + 
            ' > ' + data['params']['server'] + '.' + str(data['params']['sport']) + ': Flags [.],'  + '\n' + '\t' + 
            'ack ' + str(data['params']['ack7']) + ', win 502, length 0</pl-code>'


        ]
        
        init = random.randint(0, 5)
        data['params']['endpoint'] = "server"
        data['params']['starting'] = states_server[init]
        data['params']['next'] = trans_server[init]
        
        data['params']['mc'] = [{'tag': state, 'ans': "true"} if i==init else {'tag': state, 'ans': "false"} for i, state in enumerate(states_server[1:]) ]
