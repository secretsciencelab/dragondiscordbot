import firebase_admin

FIREBASE_TOKEN = os.environ["FIREBASE_TOKEN"]

from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('keys/dragonbot-discord-6b52efb7624a.json')
firebase_admin.initialize_app(cred)

_db = firestore.client()

def set(key, data, collection="default"):
  doc_ref = _db.collection(collection).document(key)
  doc_ref.set(data)

def get(key, collection="default"):
  try:
    if not key:
      if collection != "default":
        # return many
        doc_ref = _db.collection(collection)
        docs = doc_ref.get()
        records = []
        for doc in docs:
          docs.append(doc.to_dict())
        return records
      else:
        # don't allow this
        return None

    # return one
    doc_ref = _db.collection(collection).document(key)
    doc = doc_ref.get()
    return doc.to_dict()
  except:
    pass

  return None
