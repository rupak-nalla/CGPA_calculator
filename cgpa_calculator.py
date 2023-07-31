
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)
app.app_context().push()

s=0

@app.route('/', methods=["GET","POST"])
def home():
  if (request.method == "GET"):
    return (render_template("index.html", selected=0))
  elif(request.method=="POST"):
    s=request.form["sem"]
    return(render_template("input.html",sem_value=int(s),selecteds=int(s)))

@app.route("/calculate/<int:sems>" ,methods=["POST"])
def CGPA_calculate(sems):
  if(request.method=="POST"):
    print("In post")
    sum=0.0
    form_values = {}
    for i in range(sems):
      field_name = f'field{i}'
      
      field_value = request.form[field_name]
      
      form_values[field_name] = field_value
      
      sum=sum+float(field_value)
    result=sum/sems
    

    return(render_template("CGPA.html",sem_value=sems,semesters=form_values,cgpa=round(result, 2)))


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)
