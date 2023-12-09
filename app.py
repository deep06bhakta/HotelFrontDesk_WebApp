from flask import Flask, render_template, request, redirect, url_for, session
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask import Flask
from models import db
from models import Guest
from models import Room

import boto3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer_info.db'
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            return redirect(url_for('front_desk'))
        elif username == "deep06bhakta" and password == "iamthebest":
            return redirect(url_for('front_desk'))
        elif username == "Brian" and password == "blud":
            return redirect(url_for('front_desk'))
        elif username == "gago" and password == "steven":
            return redirect(url_for('front_desk'))
        elif username == "gago" and password == "steven":
            return redirect(url_for('front_desk'))
        else:
            return render_template('login.html', error=True)
    return render_template('login.html', error=False)

# routes 
@app.route('/front_desk')
def front_desk():
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rooms_left = calculate_rooms_left() # Implement this function
    rooms_vacant = calculate_rooms_vacant() # Implement this function
    rooms_to_clean = calculate_rooms_to_clean() # Implement this function

    return render_template('front_desk.html', 
                           current_date_time=current_date_time,
                           rooms_left=rooms_left,
                           rooms_vacant=rooms_vacant,
                           rooms_to_clean=rooms_to_clean
                        )



@app.route('/guest_list')
def guest_list():
    guests = Guest.query.all()  # Fetch all guest records from the database
    return render_template('guest_list.html', guests=guests)

@app.route('/hotel_content')
def hotel_content():
    return render_template('hotel_content.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/check_in', methods=['GET', 'POST'])
def check_in():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        room_number = request.form['room_number']
        phone_number = request.form.get('phone_number', '')
        room_type = request.form.get('room__type', 'default-value')
        num_days = request.form['num_days']
        pymt_type = request.form.get('pymt_type', 'default-value')
        # Assuming other fields are being captured

        # Create a new Guest object
        new_guest = Guest(
            name=name, 
            room_number=room_number,
            phone_number=phone_number,
            pymt_type=pymt_type,
            room_type=room_type,
            num_days=num_days
            # Set other fields as needed
        )

        # Add to the database and commit
        db.session.add(new_guest)
        db.session.commit()

        return redirect(url_for('guest_list'))
    return render_template('check_in.html')

@app.route('/check_out', methods=['GET', 'POST'])
def check_out():
    if request.method == 'POST':
        room_number = request.form.get('room_number', '')

        # Query the database for the guest with the given room number
        guest = Guest.query.filter_by(room_number=room_number).first()

        if guest:
            # Perform check-out logic here
            db.session.delete(guest)
            db.session.commit()
            return redirect(url_for('guest_list'))
        else:
            # No guest found
            return render_template('check_out.html', error="No guest found with the provided room number.")

    # For a GET request, just render the check-out page
    return render_template('check_out.html')



def calculate_rooms_left():
    # Assuming a Room model with a boolean 'is_booked' field
    return Room.query.filter_by(is_booked=False).count()

def calculate_rooms_vacant():
    # Assuming a Room model with a boolean 'is_occupied' field
    return Room.query.filter_by(is_occupied=False).count()

def calculate_rooms_to_clean():
    # Assuming additional fields in Room model to track cleaning status
    return Room.query.filter_by(is_occupied=False, needs_cleaning=True).count()


#sqs.models
def send_sqs_message(queue_url, message_body):
    sqs = boto3.client('sqs')
    response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
    return response

def receive_sqs_message(queue_url):
    sqs = boto3.client('sqs')
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1, WaitTimeSeconds=10)
    return response.get('Messages', [])

def delete_sqs_message(queue_url, receipt_handle):
    sqs = boto3.client('sqs')
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)




if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer_info.db'
    app.run(debug=True)
