from bird import Bird, alert, alert_duck, alert_bird

woody = Bird()
alert(woody)
alert_duck(woody)
alert_bird(woody)

def woody(text: str) -> str:
    """Return the input string with all 'r' replaced by 'w'."""
    return text.replace('r', 'w')