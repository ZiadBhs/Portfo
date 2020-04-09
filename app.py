from flask import Flask, render_template, send_from_directory, request, redirect
import csv



app = Flask(__name__)
print(__name__)


@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_database(data)
            return redirect("/Thanks.html")
        except :
            return "Couldnt save to database 1 "
    else : 
        return "nope :("
    


def write_to_database(data):
    with open("database.csv",mode="a", newline="") as database2 :
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter =",", quotechar ="'", quoting=csv.QUOTE_MINIMAL) 
        csv_writer.writerow([email,subject,message])
       

if __name__ == "__main__":
    app.run(debug=True)

