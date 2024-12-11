"""Get delayed"""
from random import choice

def message() -> None:
    """Get a message."""

    text_list=[ "In a minute.", 
                "Just a moment.",
                "One moment please.",
                "Hold your horses.",
                "Wow there, sparky."]

    return choice(text_list)
