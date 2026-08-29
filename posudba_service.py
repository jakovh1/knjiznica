from pony.orm.asttranslation import nonexternalizable_types
from pony.orm.core import db_session

from models import Knjiga, Posudba
from pony import orm
from datetime import date, timedelta

def checkout(book_id):
    try:
        with orm.db_session:

            book = Knjiga.get(id=book_id)

            if book is None:
                return {"status": "Fail", "message": "Knjiga koju želite posuditi nije pronađena."}
            elif Posudba.get(knjiga=book, datum_povrata=None) is not None:
                return {"status": "Fail", "message": "Knjigu koju želit eposuditi još niste vratili."}
            elif book.kolicina_dostupno <= 0:
                return {"status": "Fail", "message": "Knjiga koju želite posuditi trenutno nije dostupna."}



            Posudba(knjiga=book, datum_posudbe=date.today(), rok_povrata=date.today() + timedelta(days=30))

            book.kolicina_dostupno -= 1

            return {"status": "Success", "message": "Posudili ste knjigu " + book.naslov}

    except Exception as e:
        return {"status": "Fail", "message": str(e)}

def return_loan_service(loan_id):
    with orm.db_session:
        loan: Posudba = Posudba.get(id=loan_id)

        if loan is None:
            return {
                "status": "error",
                "message": "Posudba koju želite zatvoriti nije pronađena.",
                "book_id": None
            }

        if loan.datum_povrata is not None:
            return {
                "status": "error",
                "message": "Knjiga " + loan.knjiga.naslov +  " je već vraćena.",
                "book_id": loan.knjiga.id
            }

        loan.datum_povrata = date.today()
        loan.knjiga.kolicina_dostupno += 1

        return {
            "status": "success",
            "message": "Knjiga " + loan.knjiga.naslov + " je vraćena.",
            "book_id": loan.knjiga.id
        }

def renew_loan_service(loam_id):
    with orm.db_session:
        loan = Posudba.get(id=loam_id)

        if loan is None:
            return {
                "status": "error",
                "message": "Posudba koju želite produžiti nije pronađena.",
                "book_id": None
            }
        elif loan.datum_povrata is not None:
            return {
                "status": "error",
                "message": "Knjiga " + loan.knjiga.naslov + " je već vraćena.",
                "book_id": loan.knjiga.id
            }
        elif loan.datum_povrata is None and loan.broj_produljenja == 1:
            return {
                "status": "error",
                "message": "Posudba se može produljiti samo jednom.",
                "book_id": loan.knjiga.id
            }

        loan.rok_povrata = date.today() + timedelta(days=30)
        loan.broj_produljenja += 1

        return {
            "status": "success",
            "message": "Posudba je produljena do " + str(loan.rok_povrata.strftime("%d.%m.%Y.")),
            "book_id": loan.knjiga.id
        }



