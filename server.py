from flask import Flask, render_template, request, redirect
import csv # built-in with Python
app = Flask(__name__) # instance of a flask app or set up our flask app 
print(__name__) #__main__

#anytime we hit slash or route, I want you to define a function
@app.route('/') 
def my_home():
    #render_template: allows us to send the HTML file.
    return render_template('index.html') 

# render in the template the data that was entered in the URL
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# save data to database.txt
def write_to_file(data):
    with open('database.txt', mode='a') as database: #mode: append
        email = data["email"] #extract email from the dictionary
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

# save data to database.csv
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2: #mode: append
        email = data["email"] #extract email from the dictionary
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data) #{'email': 'test@test.com', 'subject': 'test', 'message': 'test!'}
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again.'