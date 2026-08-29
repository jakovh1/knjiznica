# 📚 Knjižnica

**Knjižnica** je jednostavna aplikacija za upravljanje posudbama knjiga, izrađena u Flasku kao dio fakultetskog projekta.

Projekt prikazuje osnovni full-stack razvoj web aplikacije, server-renderane stranice, modeliranje baze podataka, rad s posudbama knjiga i jednostavne vizualizacije podataka.

## ⚙️ Funkcionalnosti

- **Katalog knjiga**  
  - Pregled svih knjiga dostupnih u knjižnici  
  - Detaljan prikaz knjige s naslovom, autorom, opisom, žanrom, godinom izdanja i naslovnom slikom  

- **Posudba knjiga**  
  - Posudba dostupne knjige
  - Sprječavanje posudbe knjige koja trenutno nije dostupna
  - Praćenje aktivnih posudbi
  - Spremanje datuma posudbe i roka povrata

- **Upravljanje posudbama**  
  - Produženje aktivne posudbe 
  - Ograničenje broja produženja posudbe
  - Vraćanje posuđene knjige
  - Automatsko ažuriranje dostupne količine knjige nakon posudbe ili povrata

- **Statistika i vizualizacije**  
  - Prikaz broja posudbi po autoru (Pie chart)
  - Prikaz broja posudbi po knjizi (Bar chart) 
  - Prikaz broja produljenja po autoru (Bar chart)

## 🛠️ Tehnologije
- **Backend**: Python, Flask, SQLite, ponyORM, Docker
- **Frontend**: npm, Javascript, sass, Jinja, Chart.js 

## 🐳 Pokretanje aplikacije u Docker containeru
Potrebno je imati instaliran docker-engine i docker-cli na lokalnome stroju.

1. Klonirati repozitorij projekta:
```
  git clone https://github.com/jakovh1/knjiznica
  cd knjiznica
  ```

2. Generirati Docker sliku:
```
  docker build -t knjiznica:1.0 .
  ```

3. Pokrenuti Docker container:
```
  docker run -p 5001:8080 knjiznica:1.0
  ```

Aplikacija će biti dostupna na:

http://127.0.0.1:5001

