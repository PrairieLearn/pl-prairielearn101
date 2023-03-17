import random, copy
import base64
import xml.etree

def grade(data):
    
    data['partial_scores'] = {'file-input': {'score': 0}, 'file-editor': {'score': 0}}

    data['feedback']['file-input'] = '<span class="badge badge-danger">0%</span>'
    data['feedback']['file-editor'] = '<span class="badge badge-danger">0%</span>'
    
    for f in data['submitted_answers']["_files"]:
        
        fname = f['name'].split('.')[0]
        contents = f["contents"]
        contents_text = base64.b64decode(contents).decode('utf-8')
        data['submitted_answers']["file-" + fname] = contents_text.strip()
        flen = len([word.strip() for word in contents_text.split()])

        if  flen>= 12:
            data['partial_scores']["file-" + fname] = {'score': 1}
            data['feedback']['file-' + fname] = '<span class="badge badge-success">100%</span>'
        elif flen > 0:
            data['partial_scores']["file-" + fname] = {'score': flen/12}
            data['feedback']['file-' + fname] = '<span class="badge badge-warning">' + str(int(flen*100/12)) + '%</span>'

    data['score'] = 0.5*data['partial_scores']["file-input"]['score'] + 0.5*data['partial_scores']["file-editor"]['score']
                                                                                                
def generate(data):
    pass