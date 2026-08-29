from pony import orm
from datetime import date

DB = orm.Database()

class Knjiga(DB.Entity):
  id = orm.PrimaryKey(int, auto=True)
  naslov = orm.Required(str)
  autor = orm.Required(str)
  isbn = orm.Required(str)
  godina_izdanja = orm.Required(str)
  zanr = orm.Optional(str)
  broj_stranica = orm.Optional(int)
  zemlja = orm.Optional(str)
  opis = orm.Optional(str)
  naslovna_slika_path = orm.Optional(str)
  kolicina_ukupno = orm.Required(int)
  kolicina_dostupno = orm.Required(int)

  posudbe = orm.Set("Posudba", reverse="knjiga")

class Posudba(DB.Entity):
  id = orm.PrimaryKey(int, auto=True)
  knjiga = orm.Required(Knjiga)
  datum_posudbe = orm.Required(date)
  rok_povrata = orm.Required(date)
  datum_povrata = orm.Optional(date)
  broj_produljenja = orm.Required(int, default=0)

DB.bind(provider="sqlite", filename="knjiznica.sqlite", create_db=True)
DB.generate_mapping(create_tables=True)
