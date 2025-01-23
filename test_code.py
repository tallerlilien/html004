import pytest
from bs4 import BeautifulSoup, Comment
import os

def test_html_file_exists():
    """Ellenőrzi, hogy az index.html fájl létezik-e."""
    assert os.path.exists("index.html"), "Az index.html fájl nem létezik."

def test_html_lang_attribute():
    """Ellenőrzi, hogy a HTML dokumentum nyelvi attribútuma 'hu'."""
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        assert soup.html is not None, "A <html> tag hiányzik."
        assert soup.html.get("lang") == "hu", "A nyelvi attribútum nem 'hu'-ra van állítva."

def test_title_element():
    """Ellenőrzi, hogy a title elem 'HP-UX'."""
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        assert soup.title is not None, "A <title> tag hiányzik."
        assert soup.title.text == "HP-UX", "A <title> tartalma nem 'HP-UX'."

def test_h1_element():
    """Ellenőrzi, hogy az h1 elem jelen van és a tartalma "HP-UX"."""
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        assert soup.h1 is not None, "Az <h1> tag hiányzik."
        assert soup.h1.text == "HP-UX", "Az <h1> tartalma nem 'HP-UX'."

def test_h2_and_paragraph_elements():
    """Ellenőrzi a h2 és bekezdések meglétét és tartalmát."""
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        h2_tag = soup.find("h2")
        assert h2_tag is not None, "A <h2> tag hiányzik."
        assert h2_tag.text == "Támogatás", "A <h2> tag tartalma nem 'Támogatás'."

        paragraphs = soup.find_all("p")
        assert len(paragraphs) >= 1, "Legalább egy <p> tagnek kell lennie."

        platforms_paragraph = None
        for p in paragraphs:
            if "Támogatott platformok:" in p.text:
                platforms_paragraph = p
                break

        assert platforms_paragraph is not None, "A 'Támogatott platformok:' szöveget tartalmazó bekezdés nem található."
        assert "HP 9000, HP Integral PC" in platforms_paragraph.text, "A platformok felsorolása nem megfelelő (vesszővel elválasztva kell lenniük)."


def test_abbr_element():
    """Ellenőrzi az abbr elem meglétét és tartalmát."""
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        abbr_tag = soup.find("abbr")
        assert abbr_tag is not None, "Az <abbr> tag hiányzik."
        assert abbr_tag.text == "HP 9000", "Az <abbr> tag tartalma nem 'HP 9000'."
        assert abbr_tag.get("title") == "HP 9000", "Az <abbr> tag 'title' attribútuma nem 'HP 9000'."

def test_em_element():
    """Ellenőrzi az em elem meglétét és tartalmát."""
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        em_tag = soup.find("em")
        assert em_tag is not None, "Az <em> tag hiányzik."
        assert em_tag.text == "HP Integral PC", "Az <em> tag tartalma nem 'HP Integral PC'."

def test_html_comment():
    """Ellenőrzi a megjegyzés meglétét."""
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
        comments = BeautifulSoup(content, "html.parser").find_all(string=lambda text: isinstance(text, Comment))
        assert len(comments) >= 1, "Nem található megjegyzés a kódban."
        #Opcionális: ellenőrizhetjük a megjegyzés tartalmát is, ha szükséges.
        #például: assert "Név - Dátum" in comments[0]