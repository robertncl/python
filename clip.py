TEXT = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?"""
}

import sys
import pyperclip

def main() -> None:
    """Copy a phrase to the clipboard based on a keyphrase argument."""
    if len(sys.argv) < 2:
        print('Usage: py mclip.py [keyphrase] - copy phrase text')
        sys.exit()

    keyphrase = sys.argv[1]    # first command line arg is the keyphrase

    if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print('Text for ' + keyphrase + ' copied to clipboard.')
    else:
        print('There is no text for ' + keyphrase)

def clip(text: str, max_len: int = 80) -> str:
    """Return text clipped at the last space before or at max_len."""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            end = max_len
    return text[:end].rstrip() if end else text

if __name__ == '__main__':
    main()