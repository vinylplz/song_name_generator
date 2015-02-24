# song_name_generator
simple python script that generates dub song name ideas.  if present, it will pull words from the ./wordlist.txt file, and templates from the ./template.txt file.  
```
$ ./sng.py 
 QUICK AND MASH DUB 
 CHILDREN UNDERSTANDING DUB 
 HOLD AND MOUTH DUB 
 DUB MOUTH 
 JAMDOWN AND MOUTH DUB 
 DUB VAMPIRE 
 MOUTH AND LOVE DUB 
 DESTRUCTION TO EYE DUB 
 DUB LOCK 
 TIME SPACE DUB 
 CALIFORNIA AND BOB DUB 
 DUB DESTRUCTION 
 DUB FROM 
 KNOWLEDGE TO EASY DUB 
 LIFE AND NAH DUB 
$ 
```
You can change the number of results with the -n option, and override the wordlist file with the -W option:
```
$ ./sng.py -n 1 -W /usr/share/dict/words
 GOOGOLPLEX TO RETROCOSTAL DUB 
$ 
```
Wordlist file format is simply one word per line.  If you use vim, you can sort and remove duplicates using
```
:%sort u
```
Template file format is also one per line, in string.format() sytax.  The examples in templates.txt should 
be pretty self-explanatory, but feel free to read the full docs here:

https://docs.python.org/2/library/string.html#format-string-syntax
