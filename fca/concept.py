# -*- coding: utf-8 -*-
"""
Contains base class for formal concept
"""

class Concept(object):
    """ 
    A formal concept, contains intent and extent 
    
    Examples
    ========

    Create a concept with extent=['Earth', 'Mars', 'Mercury', 'Venus']
    and intent=['Small size', 'Near to the sun'].
    
    >>> extent = ['Earth', 'Mars', 'Mercury', 'Venus']
    >>> intent = ['Small size', 'Near to the sun']
    >>> c = Concept(extent, intent)
    >>> 'Earth' in c.extent
    True
    >>> 'Pluto' in c.extent
    False
    >>> 'Small size' in c.intent
    True

    Print a concept.

    >>> print c
    (['Earth', 'Mars', 'Mercury', 'Venus'], ['Near to the sun', 'Small size'])

    """
    
    def __init__(self, extent, intent):
        """Initialize a concept with given extent and intent """
        self.extent = set(extent)
        self.intent = set(intent)

    def __str__(self):
        """Return a string representation of a concept"""
        if len(self.intent) > 0:
            e = list(self.extent)
            e.sort()
        else:
            e = "G"
        if len(self.extent) > 0:
            i = list(self.intent)
            i.sort()
        else:
            i = "M"
        return "(%s, %s)" % (e, i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()