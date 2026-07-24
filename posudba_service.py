from pony.orm.asttranslation import nonexternalizable_types
from pony.orm.core import db_session

from models import Knjiga, Posudba
from pony import orm
from datetime import date, timedelta

@db_session
def add_posudba(json_request):
    try:
        knjiga_id = json_request["knjiga_id"]
        try:
            rok = date.today() + timedelta(days=30)
        except ValueError:
            rok = None

        with orm.db_session:
            Posudba(knjiga_id=knjiga_id, rok=rok)
            response = {"response": "Success"}
            return response

    except Exception as e:
        return {"response": "Fail", "error": str(e)}

def patch_posudba(posudba_id, json_request):
    try:
        with orm.db_session:
            to_patch = Posudba[posudba_id]
            if 'rok_povrata' in json_request:
                to_patch.rok_povrata = json_request["rok_povrata"]

            if 'datum_povrata' in json_request:
                to_patch.datum_povrata = json_request["datum_povrata"]

            response = {"response": "Success"}
            return response

    except Exception as e:
        return {"response": "Fail", "error": str(e)}




