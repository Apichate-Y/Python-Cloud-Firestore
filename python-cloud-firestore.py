import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebase/Admin_SDK.json')
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()

smartbins_ref = firestore_db.collection(u'smartbin').document(u'statusbin')

doc = smartbins_ref.get()

print(doc.to_dict())



