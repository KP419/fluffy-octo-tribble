from flask import Flask       
app = Flask(__name__)         

@app.get("about")
@app. get("/")                
def index():                  
    me={                      
        "first_nanme": "Kory",
        "last_nanme": "PLOTTS",
        "hobbies": "hunting",
        "is_online": True
    }
    return me                  



