from tinydb import TinyDB, Query

translations = TinyDB("translations.db")
translations.truncate()

translations.insert({"id": "index", 
                     "eng": "This page is not allowed for the request.", "rus": "Эта страница не подходит для запросов.", 
                     "lat": "Haec pagina non permittitur ad petitionem.", "rud": "Эта страница не подходитъ для запросовъ.", 
                     "fin": "Tämä sivu ei ole sallittu pyynnölle."})

translations.insert({"id": "error", 
                     "eng": "Error.", "rus": "Ошибка.", 
                     "lat": "Falsum.", "rud": "Ошибка.", 
                     "fin": "Virhe."})

# lang = Query()
# print(translations.search(lang.id == "index")[0]["rud"])