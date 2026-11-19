# Exercise 2

**Q1. Is your change in the mapper or in the reducer?**
The mapper. Cleaning the words (strip trailing `,` and `.`, lower-case) must happen before the words are grouped, so it belongs in the mapper. The reducer is unchanged.

**Q2. Code:** [mapper.py](mapper.py), [reducer.py](reducer.py)

The only change vs. the original mapper:
```python
word = word.rstrip(',.').lower()
if word:
    print ('%s%s%d' % (word, separator, 1))
```
