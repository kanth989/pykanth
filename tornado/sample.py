import tornado.ioloop
import tornado.web
import sqlite3

import json

def _execute(query):
    """Function to execute queries against a local sqlite database"""
    dbPath = 'database.db'
    connection = sqlite3.connect(dbPath)
    cursorobj = connection.cursor()
    try:
            cursorobj.execute(query)
            result = cursorobj.fetchall()
            connection.commit()
    except Exception:
            raise
    connection.close()
    return result
        
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/rest", ServiceHandler)
        ]
        super(Application, self).__init__(handlers)


class ServiceHandler(tornado.web.RequestHandler):
    """ In tornado we need a class which is our service handler""" 
    
    def get(self):
        """Get HTTP verb which our service returns a list of rows from
        database"""
        rows = _execute('SELECT * FROM data')
        data_list = []
        for row in rows:
            data_list.append(row)
        self.write(json.dumps(data_list))
            
        
    def post(self):
        """Post new data to our rest service as a JSON"""
        data = json.loads(self.request.body)
        for row in data:
            name = data.get('name')
            lname = data.get('lname')
            _execute("""insert into data (name, lname) values ("{0}", "{1}");
            """.format(name,lname))
        self.write(json.dumps(dict(result='Ok')))
        


if __name__ == "__main__":
    Application().listen(8888)
    tornado.ioloop.IOLoop.instance().start()