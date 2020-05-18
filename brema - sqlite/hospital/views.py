from django.shortcuts import render
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
db = firestore.client()


def addRequest(request):
    brid = request.POST.get('brid')
    bgroup = request.POST.get('bgroup')
    brequired = request.POST.get('brequired')
    hname = request.POST.get('hname')
    date = request.POST.get('date')

    try:
        data = {
            u'blood_id': brid,
            u'blood_group': bgroup,
            u'units_required': brequired,
            u'hospital_name': hname,
            u'date': date,
        }
        db.collection('requests').add(data)
    except:
        message = "Request not posted"
        return render(request, 'hospital/manageRequests.html', {"messg": message})

    message = "Request has been added and posted."
    return render(request, 'hospital/hospital.html', {'messg':message})


def donated(request):
    return render(request, 'hospital/donated.html', {})


def manageRequests(request):
    return render(request, 'hospital/manageRequests.html', {})


def showDonated(request):
    # firebase code to display donated where hospital code = hospital code
    return render(request, 'hospital/showDonated.html', {})


def showUsed(request):
    # firebase code to diaplay blood transfused where hospital code = hospital code
    return render(request, 'hospital/showUsed.html', {})


def used(request):
    return render(request, 'hospital/used.html', {})


# request management
def delRequest(request):
    message = "Request" + "request ID " + "been deleted"
    return render(request, 'hospital/manageRequests.html', {"messg": message})


def editRequest(request):
    message = "Request" + " request ID" + " has been posted"
    return render(request, 'hospital/manageRequests.html', {"messg": message})


# add donated blood
def addDonated(request):
    message = "Blood donated entry has been added"
    return render(request, 'hospital/donated.html', {"messg": message})


# add transfused blood
def addUsed(request):
    message = "Blood used entry has been made"
    return render(request, 'hospital/used.html', {"messg": message})
