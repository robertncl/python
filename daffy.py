from bird import Duck, alert, alert_duck, alert_bird

daffy = Duck()
alert(daffy)       
alert_duck(daffy)  
alert_bird(daffy)  

def daffy(text: str) -> str:
    """Return the input string with all 's' replaced by 'th'."""
    return text.replace('s', 'th')