This is a sample of an attendance question. The correct answer changes every minute and expires
five minutes later (but both are configurable in `server.py`). Course staff can see
the current correct answer by clicking `Save only` or `Save & Grade` and 
then expanding the `Show/Hide answer` tree in the  yellow 
`Staff information` panel on the right.

If you use this in your course, we recommend relocating `timehash.py` and 
`wordlist.py` to `serverFilesCourse`. You may also want to modify
the word list or use your own. The existing one is hopefully-inoffensive and based on
Wikipedia's simple word list. However, a small minority of words we kept were reasonable 
to expect students to know and spell in an introductory logic and circuits course and will 
be less so in other course contexts! We also recommend giving two full-credit attempts to
minimize the impact of miscommunication or typos on course staff and so TAs using the question
in student view can still view the correct answer.