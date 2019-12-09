# HASS Reflections N-gram Generator

Written by: Fasermaler

N-gram generation was partly Referenced from Elucidation's N-gram Generation [Tutorial](https://github.com/Elucidation/Ngram-Tutorial).

## Introduction

This small utility takes in crawls a specific facebook group for instructor's reflection and the submissions from students. It then generates N-grams from the retrieved text data.

- N-grams of prompts
- N-grams of submissions
- N-grams in submissions that are common with prompts
- N-grams in submissions that are new and unprompted

It is also possible to define the word filters for the N-grams within `filter_words.txt`.

## Quick Start 

### Full Start (Crawler + N-gram Generation)

1. Install the required dependencies:

   - Selenium: 

     ```bash
     $ pip install selenium
     ```

   - BeautifulSoup 4

     ```bash
     $ pip install beautifulsoup4
     ```

     or

     ```bash
     $ apt-get install python-bs4 
     ```

2. Download the gecko driver for Firefox from here: https://github.com/mozilla/geckodriver/releases and place it in the `/usr/bin/` folder:

   ```bash
   $ sudo mv geckodriver /usr/bin/geckodriver 
   ```

   Also install Firefox if you have not already:

   ```bash
   $ sudo apt-get -y install firefox
   ```

3. Create a new file called `login_credentials.txt` and put your Facebook login details as follows:

   ```
   <login email>
   <login password>
   ```
   
   Yes it's in plain-text but I've spent enough time coding for a **humanities** project already.
   
4. Run the main script:

   ```bash
   $ python main.py
   ```

### N-gram Generation Demo

1. Put the reflection prompts inside the text file `prompts.txt`

2. Put all reflection submission into the text file `texts.txt`

3. Run the the `reflection_demo.py` script:

   ```bash
   $ python reflection_demo
   ```

4. The results will be shown in the output file, `output.txt`

5. By default, the top 50 entries will be generated for each category, but it is possible the change the precision within `reflection_demo.py`

   - Edit the following line at the top of the script:

     ```python
     # Simple demo script to process reflections manually
     # Written by Fasermaler
     
     PRECISION = 50 # sets the limit on entries shown
     ```

6. The output will also be shown on the console

7. To change the filter words, edit the file `filter_words.txt`

### Sample Generation

`prompts.txt`:

```
This comes a little late. Before this week is over, make one observation about the viability of Asimov's Three Laws of Robotics either in 'The Evitable Conflict' (short story) or 'Three Robots' (from Love, Death +Robots) by engaging with one science fiction 'icon' and what it represents -- robots, mad scientist, damsel in distress, computers, the city, habitats, etc. Is the use of the icon typical? If not, what changed from the usual understanding of that icon?
```

`texts.txt`:

```
‘The Evitable Conflict’ is a short story written by Isaac Asimov himself, so it comes as no surprise that ‘The Machines’, the omniscient robots that govern that world’s economic systems, follow Asimov’s laws of robotics in full. The scientists and researchers take the laws as fact, basing their deductions ...

I will first talk about the evil characterization of the cat portrayed in the film ‘Three Robots’ (from Love, Death +Robots), and then try to weave in my explanation on why I think the Isaac Asimov’s Three Laws of Robotics ...

...
```

`output.txt`:

```
[SUMMARY]
Showing 30 most popular entries per category

[N-grams from the reflection prompt]
robots 3
icon 3
one 2
three 2
conflict short 1
over 1
damsel 1
typical changed usual 1
scientist 1
mad scientist damsel 1
before 1
etc use 1
death 1
death robots 1
changed usual 1
use icon typical 1
make one observation 1
late 1
represents robots mad 1
fiction icon represents 1
one science fiction 1
scientist damsel distress 1
robots engaging with 1
damsel distress computers 1
short story or 1
observation about viability 1
about viability 1
robotics evitable 1
laws robotics evitable 1
represents 1

[N-grams from the reflection submissions]
robots 329
humans 214
three 153
laws 142
human 138
we 113
have 104
with 102
humanity 96
film 94
robot 91
which 85
asimov 81
three robots 78
robotics 78
machines 73
law 73
three laws 69
or 65
laws robotics 61
on 58
them 54
where 53
icon 52
cats 51
being 49
harm 49
story 47
world 46
first 43

[N-grams from prompt that appeared in submissions]
robots 329
three 153
laws 142
with 102
asimov 81
robotics 78
three robots 78
three laws 69
or 65
laws robotics 61
icon 52
story 47
three laws robotics 41
one 39
about 34
asimov three 34
asimov three laws 33
make 32
short 32
conflict 29
evitable 24
science 24
evitable conflict 23
city 22
science fiction 21
fiction 21
typical 18
use 16
death 12
love 11

[N-grams that were not from prompt]
humans 214
human 138
we 113
have 104
humanity 96
film 94
robot 91
which 85
machines 73
law 73
on 58
them 54
where 53
cats 51
being 49
harm 49
world 46
first 43
all 42
own 41
us 37
see 35
these 35
there 34
machine 32
such 32
like 32
out 32
more 31
do 31
```

## To-Do

- Blacklist first
  - Cherry pick useful words
    - Concepts important
      - Author's name 
      - Synonyms
    - Concepts people though are important
  - Include these words in a whole Blacklist
- Whitelist words + Phrases
  - Include synonyms
- Get sentences that included whitelisted words/phrases
  - Word count limit (?)
    - Get sentence
    - If it's too long then cut the length (?)