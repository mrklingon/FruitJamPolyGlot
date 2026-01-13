# Polyglot
Rewrite quotes in "alien" dialects

This project is spun off of an earlier one, "Babel" that generates alien language words based on a rule set. The words *resemble* Wookie, Klingon, Vulcan, Romulan and Mando'a language vocabulary from Star Wars and Star Trek. The words created might actually be words in those languages - but for this program they are created randomly. This version is based on the previous NeoTrinkey version.

When started the program goes into a loop where a Carl Sagan quote (from the "sagan" file) is selected and printed, and each unique word is assigned one of the generated words, then the quote is displayed "translated" into the alien dialect. The progam then pauses for 20 seconds, then one of the five languages is chosen from random and a new quote is displayed.

NOTE: this *absolutely* not a real translation, just a fun exercise in generating alien text. 

FILES:

* polyglot.py - program code
* code.py 
* metadata.json
* polyglot.bmp - Fruit Jam icon
* sagan - set of Carl Sagan quotes. Feel free to replace quotes with any words of wisdom you choose.

OUTPUT:
```
English
-----------
 Imagination will often carry us to worlds that never were. But without
 it we go nowhere. Carl Sagan

Wookie
--------------------------
 OWOUUUW AORA HUW AOHA UROUH OWOAAAW AHAAUAR HUR HOR ORUOUAW RUAOUW
 OUWA WUR OAHO OHOUAAW OWUOAOR OWUOAUR RAOOH



```

