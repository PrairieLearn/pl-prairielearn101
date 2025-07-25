# This module was developed by Steven Wolfman at UBC, 2025.
# It is available for use via a CC-BY-4.0 license: https://creativecommons.org/licenses/by/4.0/.
"""
Provides the TimeHasher class. For documentation, please see that class's documentation.
"""
import hashlib
import datetime
from typing import Iterable
from collections.abc import Sequence


# I've cut the generic type parameter from TimeHasher. Not sure if PL has 
# a recent enough Python to use it.
class TimeHasher:
    """
    An object that produces consistent but securely-hashed outputs for given times.

    Time is treated in units of the "granularitySeconds" parameter. E.g. if 
    granularitySeconds is 60 then time is measured in integral minutes (since the epoch).

    The securely-hashed output is a non-negative integer by default in the range
    [0, MAX_INDEX] (a convenient power of 16 minus 1). If a non-empty items list 
    is provided to the constructor, then that integer mod the list length is used
    as an index to return one of the items. (If using the default behaviour, the
    result type for get will be an int.)

    Two TimeHashers with the same salt, granularitySeconds, and items will consistently
    produce the same outputs at the same times. Changing the salt will change the 
    outputs unpredictably (up to the limits of the portion of the secure hash in use).
    Changing the others will change the outputs, although in a predictable fashion.
    """
    NUM_HEX_DIGITS_TO_USE = 6
    MAX_INDEX = 2**(NUM_HEX_DIGITS_TO_USE-1) - 1 + 2**(NUM_HEX_DIGITS_TO_USE-1)

    def __strToBytes(self, s: str) -> bytes:
        """canonical internal way to transform a string to bytes"""
        return s.encode()
    
    def __intToBytes(self, i: int) -> bytes:
        """canonical internal way to transform an int to bytes"""
        return self.__strToBytes(f"{i}")
    
    def __getGranularTime(self, time: datetime.datetime) -> int:
        """internal transformation from a time to a time in grain sizes"""
        if time is None:
            time = datetime.datetime.now()
        timeSeconds = int(time.timestamp())
        return timeSeconds // self.granularitySeconds
    
    def __getIndex(self, granularTime: int) -> int:
        """internal way to transform a granularTime to a hashed index
        
        copies the salted index but does NOT change it.
        
        The granular time is a natural number 0 or more."""
        hasher = self.saltedHash.copy()
        hasher.update(self.__intToBytes(granularTime))
        result = hasher.hexdigest()
        return int(result[:self.NUM_HEX_DIGITS_TO_USE], base=16)

    def __init__(self, salt: str, granularitySeconds: int, items: Sequence = []):
        """create a hasher with the given salt, grain size for time, and optional items
        
        The salt distinguishes this hasher from others. Two created
        with the same salt produce the same underlying indexes (though
        if they have different item lists/granularitySeconds, the results
        will be predictably different).

        The granularitySeconds is a positive integer number of seconds
        to treat as the "grain size". Time is measured in integral units
        of that number of seconds.
        
        With no items provided (or None or an empty list of items),
        this hasher produced integers that are "indexes", numbers 0 or
        larger, up to TimeHasher.MAX_INDEX.
        
        With a non-empty items provided, produces the corresponding item,
        i.e., `items[index % len(items)]` for each index that would be 
        produced."""
        self.salt = salt
        self.granularitySeconds = granularitySeconds
        self.saltedHash = hashlib.sha256()
        self.saltedHash.update(self.__strToBytes(salt))
        self.items = items

    def get(self, time: datetime.datetime = None):
        """return a hashed item per the class documentation for the given time or now if none is given"""
        index = self.__getIndex(self.__getGranularTime(time))
        if self.items:
            return self.items[index % len(self.items)]
        else:
            return index
        
    def generate(self, time: datetime.datetime = None) -> Iterable:
        """return an iterable of hashed items per the class documentation counting down from the given time or now if none is given"""
        granularTime = self.__getGranularTime(time)
        while granularTime > 0:
            index = self.__getIndex(granularTime)
            if self.items:
                yield self.items[index % len(self.items)]
            else:
                yield index
            granularTime -= 1

    def matchesWithLeeway(self, item, leeway: int, time: datetime.datetime = None) -> bool:
        """return true if word matches one of the last leeway items leading up to and including the given time 
        (or now if no time is given)
        
        I.e., test if any of the leeway most recent results from self.generate(time) is equal to item via ==.
        
        leeway must be >= 0. A leeway of 0 means the item must be the one for time, specifically."""
        count = 0
        for correct in self.generate(time):
            if item == correct:
                return True
            count += 1
            if count > leeway:
                break
        return False
