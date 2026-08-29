from models import Knjiga
from pony import orm

def get_knjige():
    try:
        with orm.db_session:
            db_query = Knjiga.select()[:]
            results_list = []

            for record in db_query:
                results_list.append(record.to_dict())
            response = {"status": "Success", "data": results_list}

            return response
    except Exception as e:
        return {"status": "Fail", "error": str(e)}

def get_book_by_id(book_id):
    try:
        with orm.db_session:
            book = Knjiga.get(id=book_id)
            posudbe = [
                {
                    "id": posudba.id,
                    "knjiga_id": posudba.knjiga.id,
                    "datum_posudbe": posudba.datum_posudbe,
                    "rok_povrata": posudba.rok_povrata,
                    "datum_povrata": posudba.datum_povrata
                }
                for posudba in book.posudbe
                if posudba.datum_povrata is None
            ]



            response = {"status": "Success", "data": {
                                                "book": book.to_dict(),
                                                "posudba": posudbe[0] if posudbe else None
                                              }
            }
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
