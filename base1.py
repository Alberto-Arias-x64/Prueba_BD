from firebase import firebase
 
 
firebase = firebase.FirebaseApplication('https://pythonprobe.firebaseio.com/', None)
data =  { 'Name': 'ING.Simio',
          'Comentario': 'Carajo si funciona XD',
          }
result = firebase.post('/python-example-f6d0b/Students/',data)
print(result)