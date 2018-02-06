import sqlite3

IME_BAZE = 'podatki.sqlite'


def ustvari_tabele():
    """ Naredi dve tabeli: Users in Scores. """
    povezava = sqlite3.connect(IME_BAZE)
    povezava.execute("CREATE TABLE Users (id int, username varchar(100))")
    povezava.execute(
        "CREATE TABLE Scores (user_id int, napake int, beseda varchar(100))")


def dobi_najboljse():
    """ Najdi 10 iger z najmanj napakami. """
    povezava = sqlite3.connect(IME_BAZE)
    rezultat = povezava.execute("""
        SELECT Users.username, Scores.napake, Scores.beseda
        FROM Scores
        JOIN Users ON Scores.user_id=Users.id
        ORDER BY Scores.napake
        """)
    return rezultat.fetchmany(10)


def vstavi_novo_igro(user_id, napake, beseda):
    """ Vstavi novo igro v tabelo Scores. """
    povezava = sqlite3.connect(IME_BAZE)
    povezava.execute(
        "INSERT INTO Scores VALUES (?, ?, ?)", (user_id, napake, beseda))
