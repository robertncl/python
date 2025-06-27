import unicodedata


def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


Greek = 'Ζέφυρος, Zéfiro'

print(shave_marks(Greek))

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """Return the simplified fraction as a tuple (numerator, denominator)."""
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    g = gcd(numerator, denominator)
    return numerator // g, denominator // g