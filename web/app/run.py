import os
import sys
from views import app
import views

path = os.path.dirname(os.path.abspath(__file__))
if __name__ == "__main__":
    #views.setPort(int(sys.argv[1]))
    app.run(host='0.0.0.0',port=int(sys.argv[1]),threaded=True,use_reloader=False,debug=True)
