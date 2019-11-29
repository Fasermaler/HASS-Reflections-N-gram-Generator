# HASS Reflections N-gram Generator

Written by: Fasermaler

Partly Referenced from Elucidation's N-gram Generation [Tutorial](https://github.com/Elucidation/Ngram-Tutorial).

## Introduction

This small utility takes in a reflection prompts and the submissions from students and generates N-grams:

- N-grams of prompts
- N-grams of submissions
- N-grams in submissions that are common with prompts
- N-grams in submissions that are new and unprompted

It is also possible to define the word filters for the N-grams within `reflection_ngram.py`.

## Quick Start

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

     