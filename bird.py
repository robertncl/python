class Bird:
    """A base class for birds."""
    pass

class Duck(Bird):
    """A duck, which is a kind of bird."""
    def quack(self) -> None:
        """Print the sound a duck makes."""
        print('Quack!')

def alert(birdie: Bird) -> None:
    """Call quack on any bird-like object."""
    birdie.quack()

def alert_duck(birdie: Duck) -> None:
    """Call quack on a Duck object."""
    birdie.quack()

def alert_bird(birdie: Bird) -> None:
    """Call quack on a Bird object."""
    birdie.quack()

def bird_sound(bird: str) -> str:
    """Return the sound made by the given bird."""
    sounds = {'duck': 'quack', 'chicken': 'cluck', 'crow': 'caw'}
    return sounds.get(bird.lower(), 'unknown')