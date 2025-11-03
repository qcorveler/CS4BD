"""
Utile pour convertir les chiffres écrits en toutes lettres en nombre pour python
"""

class NumberConverter:
    # dictionnaires de conversion langues → nombres
    NUMBERS = {
        "en": {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
               "seven":7, "eight":8, "nine":9},
        "es": {"cero":0, "uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5,
               "seis":6, "siete":7, "ocho":8, "nueve":9},
        "de": {"null":0, "eins":1, "zwei":2, "drei":3, "vier":4, "fünf":5,
               "sechs":6, "sieben":7, "acht":8, "neun":9},
        "ru": {"ноль":0, "один":1, "два":2, "три":3, "четыре":4, "пять":5,
               "шесть":6, "семь":7, "восемь":8, "девять":9},
        "fr": {"zéro":0, "un":1, "deux":2, "trois":3, "quatre":4, "cinq":5, "six":6,
               "sept":7, "huit":8, "neuf":9},
        "cn": {"零":0, "一":1, "二":2, "三":3, "四":4, "五":5, "六":6, "七":7,
               "八":8, "九":9},
    }

    ROMAN_NUMERAL_MAP = {
        'I':1, 'II':2, 'III':3, 'IV':4, 'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9, 'X':10
    }

    # fusionner toutes les valeurs pour lookup
    ALL_NUMBERS = {**NUMBERS["en"], **NUMBERS["es"], **NUMBERS["de"],
                   **NUMBERS["ru"], **NUMBERS["cn"], **ROMAN_NUMERAL_MAP}

    def to_number(self, x):
        """Convert a string (number name, roman, chinese, or digits) to float/int"""
        if isinstance(x, (int, float)):
            return x
        x = x.strip()
        # remplacer les virgules par points pour float
        x_clean = x.replace(",", ".")
        # si c'est un chiffre romain, chinois ou nom
        if x_clean in self.ALL_NUMBERS:
            return self.ALL_NUMBERS[x_clean]
        # sinon essayer de convertir directement en float
        try:
            return float(x_clean)
        except ValueError:
            raise ValueError(f"Cannot convert '{x}' to a number")