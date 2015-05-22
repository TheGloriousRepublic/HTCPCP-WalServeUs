import BaseHTTPServer, os, datetime

settings={}
rw={}

def brewCoffee(*args):
    pass

def dictMerge(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

def log(dat): #Print to console and save to log
    o='['+str(datetime.datetime.now())+'] '+str(dat)+'\n'    
    b=open(settings['lgdir']+'/server.log', 'r+').read() #Retrieve current log
    open(settings['lgdir']+'/server.log', 'w+').write(b+o+'\n\n') #Write a concatenation of old log and new log to log
    print(o)

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

    def log_message(*args):
        pass

    def logCommand(self):
        log(self.client_address[0]+' on port '+str(self.client_address[1])+' to '+self.headers.get('host')+': \''+self.command+' '+self.path+'\', interpreted as \''+self.command+' '+self.getPath()+'\'') #Log the time and client address/client port of a request, followed by the request submitted and what it was interpreted to.
        
    def do_BREW(self):
        self.logCommand()
        if self.headers('Content-Type')=='application/coffee-pot-command':
            pass

    def do_POST(self):
        self.do_BREW()

    def do_GET(self):
        self.logCommand()
        pass

    def do_PROPFIND(self):
        pass

    def do_WHEN(self):
        pass

loadConfig()



def serve():
    log('Server starts')
    s = BaseHTTPServer.HTTPServer(('', int(settings['port'])), CoffeePot)
    try:
        s.serve_forever()
    except:
        pass

if __name__ == '__main__':
    serve()
