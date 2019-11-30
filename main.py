from site_crawler import site_crawler
from reflection_ngram import reflection_post as reflection
from post_process import processor

import os

import errno

# Set limit on max number of entries per category
PRECISION = 30

# Get site data from web crawler
crawler = site_crawler("https://www.facebook.com/groups/2340846329564248/")
crawler.crawl()

process = processor()
process.get_source_from_crawler(crawler) # Get the extracted webpage from the crawler
#process.get_source_from_local_html("./output1.html")
process.process_page()

reflections_dict = process.reflections_dict

for entry in reflections_dict.keys():

    # Write the raw text to output folders first
    prompts, texts = reflections_dict[entry]
    p_filename = "./output/post" + str(entry) + "/prompt.txt"
    t_filename = "./output/post" + str(entry) + "/replies.txt"
    if not os.path.exists(os.path.dirname(p_filename)):
        try:
            os.makedirs(os.path.dirname(p_filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(p_filename, "w") as f:
        f.write(reflections_dict[entry][0].encode("utf-8"))

    with open(t_filename, "w") as f:
        for post in reflections_dict[entry][1]:
            f.write(post.encode("utf-8"))

    reflect = reflection([prompts], texts)
    reflect.process_post()
    reflect.generate_summary(PRECISION)

    n_filename = "./output/post" + str(entry) + "/ngrams.txt"
    reflect.write_HR(n_filename)
