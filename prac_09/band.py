"""
Band for musicians
Estimate: 60 mins
Actual: 65 mins
"""
import keyword

from tomlkit import string


class Band:
    """Band Class"""

    def __init__(self, band_name: str):
        """Construct Band class"""
        self.band_members = []
        self.band_name = band_name

    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        members_string = ','.join(str(member) for member in self.band_members)
        return f'{self.band_name}({members_string})'

    def add(self, musician):
        """Add musician to band"""
        self.band_members.append(musician)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        players_playing = []
        for musician in self.band_members:
            # the my_band program imports musician class, so I can call this method .play on a musician object
            # when running my_band
            players_playing.append(str(musician.play()))
        return "\n".join(players_playing)


