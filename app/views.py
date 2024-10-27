from flask import flash, render_template, redirect
from app import app, db
from app.models import Assessment
from .forms import AssessmentForm

import datetime

# Assessments are fetched from database
# Then formatted and passed to template
#   the below array is an example of a the renderable format
# 
# assessments = [
#     { 
#         "id": 0,
#         "title":"Coursework 1", 
#         "module":"COMP2011", 
#         "description":"web app dev coursework 1", 
#         "dueDate":"31/10/24", 
#         "dueTime":"15:00", 
#         "completed": False
#     }, {
#         "id": 1,
#         "title":"Coursework 2", 
#         "module":"COMP1921", 
#         "description":"module from last year's coursework", 
#         "dueDate":"15/2/24", 
#         "dueTime":"14:00", 
#         "completed": True
#     }
# ]

# Convert a database assessment to the renderable format
def formatAssessment(assessment):
    return {
            "id": assessment.id,
            "title": assessment.title,
            "module": assessment.module,
            "description": assessment.description,
            "dueDate": assessment.deadline.strftime("%D/%m/%Y"),
            "dueTime": assessment.deadline.strftime("%H:%M"),
            "completed": assessment.completed
        }

@app.route('/', methods=['GET', 'POST'])
def home():
    # Get all assessments from database ordered by not completed first
    data = db.session.execute(db.select(Assessment).order_by(Assessment.completed)).all()

    # Format data ready for rendering
    assessments = []
    for assessment in data:
        assessments.append(formatAssessment(assessment[0]))

    if not assessments:
        flash("No assessments to display")

    return render_template("home.html", title="Home", assessments=assessments)

@app.route('/completed', methods=['GET', 'POST'])
def completed():
    data = db.session.execute(db.select(Assessment).filter_by(completed=True)).all()

    assessments = []
    for assessment in data:
        assessments.append(formatAssessment(assessment[0]))

    if not assessments:
        flash("No completed assessments to display")

    return render_template("home.html", title="Completed Assessments", assessments=assessments)

@app.route('/current', methods=['GET', 'POST'])
def current():
    data = db.session.execute(db.select(Assessment).filter_by(completed=False)).all()

    assessments = []
    for assessment in data:
        assessments.append(formatAssessment(assessment[0]))

    if not assessments:
        flash("No current assessments to display")

    return render_template("home.html", title="Current Assessments", assessments=assessments)

@app.route('/create', methods=['GET', 'POST'])
def createAssessment():
    form = AssessmentForm()

    if form.validate_on_submit():

        title = form.title.data
        module = form.module.data
        description = form.description.data
        deadline = datetime.datetime.combine(form.dueDate.data, form.dueTime.data)
        completed = form.completed.data

        flash("Successfully created %s %s" % (module, title))


        newAssessment = Assessment(title=title, module=module, description=description, deadline=deadline, completed=completed)
        db.session.add(newAssessment)
        db.session.commit()

        return redirect("/current")

    return render_template("assessmentForm.html", 
                           title="Create Assessment", 
                           action="create", # can be (create, edit)
                           form=form
                           )


@app.route('/edit', methods=['GET', 'POST'])
@app.route('/edit/<int:assessmentId>', methods=['GET', 'POST'])
def editAssessment(assessmentId=None):
    # if the user tries to go to the edit route without passing an id
    #   they are redirected back to the home page
    if assessmentId == None: 
        return redirect("/")


    form = AssessmentForm()
    return render_template("assessmentForm.html", 
                           title="Edit Assessment", 
                           action="edit", # can be (create, edit)
                           form=form
                           )

@app.route("/toggle-completed", methods=['GET', 'POST'])
@app.route("/toggle-completed/<int:assessmentId>", methods=['GET', 'POST'])
def markAsComplete(assessmentId=None):
    if assessmentId == None:
        return redirect("/")
    
    assessment = db.session.execute(db.select(Assessment).filter_by(id=assessmentId)).scalar()

    assessment.completed = not assessment.completed
    db.session.commit()

    return redirect("/")


