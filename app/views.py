from flask import render_template
from app import app

@app.route('/', methods=['GET', 'POST'])
def home():
    # Assessments are fetched from database
    # Then processed and passed to template
    #   in the format {title, module, description, dueDate, dueTime, completed}
    
    assessments = [
        { 
            "title":"Coursework 1", 
            "module":"COMP2011", 
            "description":"web app dev coursework 1", 
            "date":"31/10/24", 
            "time":"15:00", 
            "completed": False
        }, {
            "title":"Coursework 2", 
            "module":"COMP1921", 
            "description":"module from last year's coursework", 
            "date":"15/2/24", 
            "time":"14:00", 
            "completed": True
        }, {
            "title":"Formative Coursework 1", 
            "module":"COMP2421", 
            "description":"Made up coursework", 
            "date":"25/10/24", 
            "time":"16:00", 
            "completed": False
        }
    ]
    
    return render_template("home.html", assessments = assessments)