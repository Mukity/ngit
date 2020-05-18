import smtplib
import socket
from email.mime.text import MIMEText

import firebase_admin

from firebase import Firebase
from django.contrib import auth
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import credentials, firestore


config = {
    "apiKey": "AIzaSyCVnG5bxv732Z-wU7UtiWYikIGF1B1Re5U",
    "authDomain": "brema-c7e1b.firebaseapp.com",
    "databaseURL": "https://brema-c7e1b.firebaseio.com",
    "projectId": "brema-c7e1b",
    "storageBucket": "brema-c7e1b.appspot.com",
    "messagingSenderId": "890549524751",
    "appId": "1:890549524751:web:a9f629a22fe7b31e9a867a",
    "measurementId": "G-1TM25J5677"
}
cred = credentials.Certificate('./bremafirebaseadminsdk.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

firebase = Firebase(config)
authe = firebase.auth()


socket.setdefaulttimeout(None)
HOST = 'smtp.gmail.com'
PORT = 587
sender = '20brema20@gmail.com'
password = 'amerb0202'
receiver = ['Aluta@mailinator.com']

@csrf_exempt
def HomePageView(request):
    return render(request, 'Home.html', {})


@csrf_exempt
def Feedback(request):
    fullname = request.POST.get('fullName')
    email = request.POST.get('email')
    comment = request.POST.get('comment')

    msg = MIMEText("comment")
    msg['Subject'] = 'BREMA FEEDBACK by '
    msg['From'] = sender
    msg['To'] = receiver


    server = smtplib.SMTP(HOST, PORT)
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.close()

    Appreciation = "Thank you for the feedback."
    return render(request, 'Home.html', {"messg": Appreciation})


@csrf_exempt
def SignupView(request):
    return render(request, 'signup.html', {})


# sign up for hospital
@csrf_exempt
def Success(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    hname = request.POST.get('hname')
    hid = request.POST.get('hid')
    contact = request.POST.get('contact')
    county = request.POST.get('county')
    scounty = request.POST.get('scounty')
    ward = request.POST.get('ward')
    location = request.POST.get('location')

    try:
        authe.create_user_with_email_and_password(email, passw)
        data = {
            u'email': email,
            u'hospital_name': hname,
            u'hospital_ID': hid,
            u'contact': contact,
            u'county': county,
            u'sub-county': scounty,
            u'ward': ward,
            u'location_Desc': location,
        }
        db.collection('Hospital Profile').add(data)
    except:
        message = "Account Exists"
        return render(request, 'signup.html', {"messg": message})
    return render(request, 'hospital/hospital.html', {})


# signup for donor
@csrf_exempt
def Success(request):
    demail = request.POST.get('demail')
    dpassw = request.POST.get('dpass')
    fname = request.POST.get('fname')
    dob = request.POST.get('dob')
    bgroup = request.POST.get('bgroup')
    dcontact = request.POST.get('dcontact')
    dcounty = request.POST.get('dcounty')
    dscounty = request.POST.get('dscounty')
    dward = request.POST.get('dward')

    try:
        authe.create_user_with_email_and_password(demail, dpassw)
        data = {
            u'email': demail,
            u'full_name': fname,
            u'date_of_birth': dob,
            u'blood_group': bgroup,
            u'contact': dcontact,
            u'county': dcounty,
            u'sub-county': dscounty,
            u'ward': dward,
        }
        db.collection('Donor Profile').add(data)
    except:
        message = "Account Exists"
        return render(request, 'signup.html', {"messg": message})
    return render(request, 'donor/profile.html', {})


@csrf_exempt
def LoginView(request):
    return render(request, 'login.html', {})


def Logout(request):
    auth.logout(request)
    return render(request, 'login.html', {})


def Requests(request):
    request_ref = db.collection('requests')
    docs = request_ref.stream()
    requests = ""
    # initialise the variables
    blood_id = ""
    date = ""
    blood_group = ""
    units_required = ""
    hospital_name = ""
    for doc in docs:
        data = doc.to_dict()
        date += (data['date'])
        date += "\n"
        blood_id += (data['blood_id'])
        blood_id += "\n"
        blood_group += (data['blood_group'])
        blood_group += "\n"
        units_required += (data['units_required'])
        units_required += "\n"
        hospital_name += (data['hospital_name'])
        hospital_name += "\n"
    print(blood_group)
    # requests += "{}".format(data)
    return render(request, 'requests.html',
                  {"date": date, "brid": blood_id, "bgrp": blood_group, "hname": hospital_name,
                   "units": units_required})


@csrf_exempt
def Donor(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid login credentials"
        return render(request, 'login.html', {"messg": message})
    return render(request, 'donor/donor.html', {})


@csrf_exempt
def Hospital(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        authe.sign_in_with_email_and_password(email, passw)

    except:
        message = "invalid login credentials"
        return render(request, 'login.html', {"messg": message})
    return render(request, 'hospital/hospital.html', {})
