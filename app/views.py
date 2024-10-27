from flask import render_template
from app import app
from .forms import AssessmentForm

@app.route('/', methods=['GET', 'POST'])
def home():
    # Assessments are fetched from database
    # Then processed and passed to template
    #   in the format seen below
    
    assessments = [
        { 
            "id": 1,
            "title":"Coursework 1", 
            "module":"COMP2011", 
            "description":"web app dev coursework 1", 
            "dueDate":"31/10/24", 
            "dueTime":"15:00", 
            "completed": False
        }, {
            "id": 2,
            "title":"Coursework 2", 
            "module":"COMP1921", 
            "description":"module from last year's coursework", 
            "dueDate":"15/2/24", 
            "dueTime":"14:00", 
            "completed": True
        }, {
            "id": 3,
            "title":"Formative Coursework 1", 
            "module":"COMP2421", 
            "description":"Made up coursework", 
            "dueDate":"25/10/24", 
            "dueTime":"16:00", 
            "completed": False
        }
    ]
    
    return render_template("home.html", title="Home", assessments=assessments)

@app.route('/create', methods=['GET', 'POST'])
def createAssessment():
    form = AssessmentForm()
    return render_template("assessmentForm.html", 
                           title="Create Assessment", 
                           action="Create",
                           form=form
                           )