import BaseHTTPServer

def loadConfig(): #Open configuration files and save their options to settings
    print('Loading configuration files')
    print('\tLoading settings...')                
    
    for root, dirs, files in os.walk('config/settings/'): #Open all files in config directory
        for f in files:
            if f.endswith('.cfg'):
                for x in open('config/settings/'+f).read().split('\n'): #Separate lines in file and iterate
                    if not x[0]=='#':
                        settings[x.split('=')[0]]=x.split('=')[1] #Set the option before the equal sign in the config file line to the value in the settings dict

    print('\tLoading rewrite...')    
    for root, dirs, files in os.walk('config/rewriter/'):
        for f in files:
            if f.endswith('.cfg'):
                for x in open('config/rewriter/'+f).read().split('\n'):
                    if not x[0]=='#':
                        rw[x.split('=')[0]]=x.split('=')[1]

    print('\tConfiguration loaded\n\n')

class CoffeePot(BaseHTTPServer.BaseHTTPRequestHandler):
    pass

def serve():
    log('Server starts')
    s = BaseHTTPServer.HTTPServer(('', int(settings['port'])), CoffeePot)
    try:
        s.serve_forever()
    except:
        pass

if __name__ == '__main__':
    serve()
