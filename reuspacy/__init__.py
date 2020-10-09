import spacy
from spacy.pipeline import EntityRuler
nlp=spacy.load('en_core_web_sm',disable=['ner'])

def reuspacy():
    rulerLocations = EntityRuler(nlp, overrite_ents=True)
    locations = ['Mount Kenya','Maasai Mara',
             'Nyeri','Lake Naivasha','Mombasa',
             'Nairobi','Lake Victoria',
             'Mount Elgon',
             'Nakuru','Kiambu',
             'Olduvai Gorge',
             'Zanzibar'
            ]
    for l in locations:
        rulerLocations.add_patterns([{'label':'LOC','pattern':l}])

    rulerLocations.name = 'rulerLocations'
    nlp.add_pipe(rulerLocations)
