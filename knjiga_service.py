from pip._internal.utils import retry
from pony.orm.core import db_session

from models import Knjiga
from pony import orm

@db_session
def get_knjige():
    try:
        with orm.db_session:
            db_query = orm.select(x for x in Knjiga)[:]
            results_list = []

            for record in db_query:
                results_list.append(record.to_dict())
            response = {"status": "Success", "data": results_list}

            return response
    except Exception as e:
        return {"status": "Fail", "error": str(e)}

def add_knjiga(data):
    try:
        with orm.db_session:
            Knjiga(**data)
            response = {"status": "Success"}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}
