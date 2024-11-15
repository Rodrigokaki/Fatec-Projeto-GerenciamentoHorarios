from bson import ObjectId
from datetime import datetime


def jsonify_plain(document, id_key="id"):
    plain_document = {}
    
    for k, v in document.items():
        if k == "_id" and isinstance(v, ObjectId):
            plain_document[id_key] = str(v)
        elif isinstance(v, ObjectId):
            plain_document[k] = str(v)
        elif isinstance(v, datetime):
            plain_document[k] = v.isoformat()
        else:
            plain_document[k] = v

    return plain_document

def convert_to_datetime(d):
    new_date_obj = datetime.strptime(d, "%H:%M")
    
    return new_date_obj