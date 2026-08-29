
from models import Posudba
from pony import orm
from collections import defaultdict

def get_loaned_books_qty_by_author():
    try:
        with orm.db_session:
            loans_by_author = defaultdict(int)

            for loan in Posudba.select():
                loans_by_author[loan.knjiga.autor] += 1

            return {
                "status": "Success",
                "data": {
                    "title": "Broj posuđenih knjiga po autoru",
                    "type": "pie",
                    "labels": list(loans_by_author.keys()),
                    "values": list(loans_by_author.values())
                }
            }


    except Exception as e:
        return {"status": "Fail", "message": str(e)}

def get_loaned_books_qty():
    try:
        with orm.db_session:
            loaned_books = defaultdict(int)

            for loan in Posudba.select():
                loaned_books[loan.knjiga.naslov] += 1

            return {
                "status": "Success",
                "data": {
                    "title": "Broj posudbi po naslovu",
                    "type": "bar",
                    "labels": list(loaned_books.keys()),
                    "values": list(loaned_books.values())
                }
            }

    except Exception as e:
        return {"status": "Fail", "message": str(e)}

def get_renewals_by_author():
    try:
        with orm.db_session:
            renewals_by_author = defaultdict(int)

            for loan in Posudba.select():
                if loan.broj_produljenja == 1:
                    renewals_by_author[loan.knjiga.autor] += 1

            return {
                "status": "Success",
                "data": {
                    "title": "Broj produljenja po autoru",
                    "type": "bar",
                    "labels": list(renewals_by_author.keys()),
                    "values": list(renewals_by_author.values())
                }
            }

    except Exception as e:
        return {"status": "Fail", "message": str(e)}
