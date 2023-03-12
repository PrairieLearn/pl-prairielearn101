import random, copy

def parse(data):
    data['format_errors'] = {}
    
def generate(data):
    
    bridgeID = random.sample(range(10, 80), 5)
    bridgeID.sort()
    data['params']['bridgeID'] = bridgeID
    
    data['params']['version'] = random.choice([0, 1, 2])
    
    if data['params']['version'] == 0:

        data['params']['bridges'] = [
            {'gvid': "B1", 'name': "photon",    'id': bridgeID[2] },
            {'gvid': "B2", 'name': "catt",      'id': bridgeID[3] },
            {'gvid': "B3", 'name': "utopia",    'id': bridgeID[1] },
            {'gvid': "B4", 'name': "duke",      'id': bridgeID[4] },
            {'gvid': "B5", 'name': "eng",       'id': bridgeID[0] }
        ]
    
        data['params']['menus'] = [
            
            {'bridge': 'utopia', 'port': '2', 'x': 185, 'y': 355, 'status': 'rp'},
            {'bridge': 'utopia', 'port': '1', 'x': 330, 'y': 395, 'status': 'dp'},
          
            
            {'bridge': 'duke',   'port': '2', 'x': 438, 'y': 390, 'status': 'bl'},
            {'bridge': 'catt',   'port': '2', 'x': 348, 'y': 80, 'status': 'rp'},
            {'bridge': 'eng',    'port': '2', 'x': 320, 'y': 170, 'status': 'dp'},
    
            {'bridge': 'eng',    'port': '1', 'x': 250, 'y': 245, 'status': 'dp'}, 
            {'bridge': 'catt',   'port': '1', 'x': 508, 'y': 90, 'status': 'dp'}, 
    
            {'bridge': 'duke',   'port': '1', 'x': 430, 'y': 490, 'status': 'rp'}, 
    
            {'bridge': 'catt',   'port': '3', 'x': 412, 'y': 155, 'status': 'dp'},
    
            {'bridge': 'photon', 'port': '1', 'x': 600, 'y': 195, 'status': 'rp'}, 
            {'bridge': 'photon', 'port': '3', 'x': 658, 'y': 275, 'status': 'dp'}, 
            {'bridge': 'photon', 'port': '4', 'x': 530, 'y': 305, 'status': 'dp'},
            {'bridge': 'photon', 'port': '2', 'x': 480, 'y': 250, 'status': 'bl'} 
            
            ]            

    elif data['params']['version'] == 1:
            
            data['params']['bridges'] = [
                {'gvid': "B1", 'name': "photon",    'id': bridgeID[3] },
                {'gvid': "B2", 'name': "catt",      'id': bridgeID[0] },
                {'gvid': "B3", 'name': "utopia",    'id': bridgeID[1] },
                {'gvid': "B4", 'name': "duke",      'id': bridgeID[2] },
                {'gvid': "B5", 'name': "eng",       'id': bridgeID[4] }
            ]
        
            data['params']['menus'] = [
            
            
            {'bridge': 'utopia', 'port': '2', 'x': 185, 'y': 355, 'status': 'rp'},
            {'bridge': 'utopia', 'port': '1', 'x': 330, 'y': 395, 'status': 'dp'},
           
            
            {'bridge': 'duke',   'port': '2', 'x': 438, 'y': 390, 'status': 'rp'},
            {'bridge': 'catt',   'port': '2', 'x': 348, 'y': 80, 'status': 'dp'},
            {'bridge': 'eng',    'port': '2', 'x': 320, 'y': 170, 'status': 'rp'},
    
            {'bridge': 'eng',    'port': '1', 'x': 250, 'y': 245, 'status': 'dp'}, 
            {'bridge': 'catt',   'port': '1', 'x': 508, 'y': 90, 'status': 'dp'},
    
            {'bridge': 'duke',   'port': '1', 'x': 430, 'y': 490, 'status': 'bl'},
    
            {'bridge': 'catt',   'port': '3', 'x': 412, 'y': 155, 'status': 'dp'},
    
            {'bridge': 'photon', 'port': '1', 'x': 600, 'y': 195, 'status': 'rp'}, 
            {'bridge': 'photon', 'port': '3', 'x': 658, 'y': 275, 'status': 'dp'},
            {'bridge': 'photon', 'port': '4', 'x': 530, 'y': 305, 'status': 'dp'}, 
            {'bridge': 'photon', 'port': '2', 'x': 480, 'y': 250, 'status': 'bl'} 
            ]
                
    elif data['params']['version'] == 2:

        data['params']['bridges'] = [
            {'gvid': "B1", 'name': "photon",    'id': bridgeID[2] },
            {'gvid': "B2", 'name': "catt",      'id': bridgeID[4] },
            {'gvid': "B3", 'name': "utopia",    'id': bridgeID[0] },
            {'gvid': "B4", 'name': "duke",      'id': bridgeID[3] },
            {'gvid': "B5", 'name': "eng",       'id': bridgeID[1] }
        ]
    
        data['params']['menus'] = [

            {'bridge': 'eng',    'port': '2', 'x': 320, 'y': 170, 'status': 'dp'},
            {'bridge': 'eng',    'port': '1', 'x': 250, 'y': 245, 'status': 'rp'},

            {'bridge': 'catt',   'port': '1', 'x': 508, 'y': 90, 'status': 'bl'}, 
            
            
            {'bridge': 'utopia', 'port': '1', 'x': 330, 'y': 395, 'status': 'dp'}, 
            {'bridge': 'catt',   'port': '2', 'x': 348, 'y': 80, 'status': 'rp'}, 


            
            {'bridge': 'utopia', 'port': '2', 'x': 185, 'y': 355, 'status': 'dp'}, 
            {'bridge': 'catt',   'port': '3', 'x': 412, 'y': 254, 'status': 'bl'}, 

            {'bridge': 'photon', 'port': '3', 'x': 658, 'y': 275, 'status': 'dp'},
            {'bridge': 'duke',   'port': '2', 'x': 438, 'y': 390, 'status': 'dp'},
    
    
            {'bridge': 'duke',   'port': '1', 'x': 430, 'y': 490, 'status': 'rp'}, 
            {'bridge': 'photon', 'port': '1', 'x': 600, 'y': 195, 'status': 'dp'}, 
    
            {'bridge': 'photon', 'port': '2', 'x': 480, 'y': 250, 'status': 'dp'},
            {'bridge': 'photon', 'port': '4', 'x': 530, 'y': 305, 'status': 'rp'}
            ]            


        
    for entry in data['params']['menus']:
        entry['dp']=entry['status']=='dp'
        entry['rp']=entry['status']=='rp'
        entry['bl']=entry['status']=='bl'
    