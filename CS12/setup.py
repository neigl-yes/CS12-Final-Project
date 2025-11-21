import cherrypy
from views import FormSubmission
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    config = {
        '/public': {
            'tools.staticdir.on': True,
            'tools.staticdir.root': current_dir,
            'tools.staticdir.dir': 'public'
        }
    }

    cherrypy.quickstart(FormSubmission(), '/', config=config)