import pyrebase
config= {
	
	apiKey: "AIzaSyCVWiMmGgzRvfqwsPtfCGoEEWAK0DONMbA",
    authDomain: "pythonprobe.firebaseapp.com",
    databaseURL: "https://pythonprobe.firebaseio.com",
    projectId: "pythonprobe",
    storageBucket: "pythonprobe.appspot.com",
    messagingSenderId: "914597158982",
    appId: "1:914597158982:web:7817ba9f400616f74b6a47",
    measurementId: "G-CQV7S608W0"
}

firebasep = pyrebase.initialize_app(config)
storage = firebase.storage()