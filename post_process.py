from site_crawler import site_crawler
from bs4 import BeautifulSoup

import urllib2

import os

import errno
# Class to process the webpage source and extract text data
# Written by Fasermaler


class processor:
    def __init__(self):
        self.webpage_soup = None
        self.posts = None
        self.reflections_list = [] # list to store which posts are reflections
        self.reflections_dict = {} # Full reflections dict with all text data

    # Method to get the webpage source from a crawler
    def get_source_from_crawler(self, crawler):
        self.webpage_soup = BeautifulSoup(crawler.driver.page_source, 'html.parser')
        self.posts = self.webpage_soup.findAll('div', id=lambda x: x and x.startswith('mall_post'))

        # Also save the webpage for debugging purposes
        filename = "./output/webpage/output.html"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(filename, "w") as file:
             file.write(str(self.webpage_soup))
    # Method to get the webpage source locally
    def get_source_from_local_html(self, file):
        self.webpage_soup = BeautifulSoup(open(file), "html.parser")
        self.posts = self.webpage_soup.findAll('div', id=lambda x: x and x.startswith('mall_post'))

    def get_reflections_list(self):
        # Check for reflection posts
        nazry_count = 0
        reflection_count = 0
        self.reflection_list = [] # reset the list
        for i in range(len(self.posts)):
            # debug print to get the names of every poster in every post
            #print(post.div.div.find_next_sibling().div.div.find_next_sibling().div.div.a.find_next_sibling().div.find_next_sibling().div.div.div.find_next_sibling().h5.span.span.a.string)

            if str(self.posts[i].div.div.find_next_sibling().div.div.find_next_sibling().div.div.a.find_next_sibling().div.find_next_sibling().div.div.div.find_next_sibling().h5.span.span.a.string) == "Nazry Bahrawi":
                nazry_count += 1
                # Check if there are many comments on the post which would indicate it is a reflection
                if len(self.posts[i].div.findAll('div')[1].div.find_next_sibling().form.div.div.find_next_siblings()[1].ul.li.find_next_siblings()) > 15:
                    reflection_count += 1
                    self.reflection_list.append(i)


        print("There are " + str(nazry_count) + " posts by Nazry")
        print("Of which " + str(reflection_count) + " are reflection prompts")

    def get_full_text_data(self):
        for num in self.reflection_list:
            texts = []
            text_count = len(self.posts[num].div.div.find_next_sibling().div.find_next_sibling().div.div.find_next_sibling().find_next_sibling().ul.li.find_next_siblings())
            prompt = self.posts[num].div.div.find_next_sibling().div.div.find_next_sibling().div.find_next_sibling().getText()
            # Append the first text before it's siblings
            texts.append(self.posts[num].div.div.find_next_sibling().div.find_next_sibling().div.div.find_next_sibling().find_next_sibling().ul.li.div.div.div.find_next_sibling().div.div.div.div.getText())
            for t in range(text_count):
                texts.append(self.posts[num].div.div.find_next_sibling().div.find_next_sibling().div.div.find_next_sibling().find_next_sibling().ul.li.find_next_siblings()[t].div.div.div.find_next_sibling().div.div.div.div.getText())
            self.reflections_dict[num] = (prompt, texts)

    def process_page(self):
        self.get_reflections_list()
        self.get_full_text_data()

# # Test CODE
#
# url = "./output1.html"
#
# process = processor()
# process.get_source_from_local_html(url)
# process.process_page()
# print(process.reflections_dict)


# OLD CODE ===============================


# crawler = site_crawler("https://www.facebook.com/groups/2340846329564248/")
# crawler.crawl()
#
# webpage_soup = BeautifulSoup(crawler.driver.page_source, 'html.parser')

# with open("output1.html", "w") as file:
#     file.write(str(webpage_soup))


# url = "./output1.html"
#
# webpage_soup = BeautifulSoup(open(url), "html.parser")
#
# posts = webpage_soup.findAll('div', id=lambda x: x and x.startswith('mall_post'))
#print(posts)

# Get name
#print(posts[0].div.div.find_next_sibling().div.div.find_next_sibling().div.div.a.find_next_sibling().div.find_next_sibling().div.div.div.find_next_sibling().h5.span.span.a.string)

# Check for reflection posts
# nazry_count = 0
# reflection_count = 0
# reflection_list = [] # list to store which posts are reflections
# for i in range(len(posts)):
#
#     # debug print to get the names of every poster in every post
#     #print(post.div.div.find_next_sibling().div.div.find_next_sibling().div.div.a.find_next_sibling().div.find_next_sibling().div.div.div.find_next_sibling().h5.span.span.a.string)
#     if str(posts[i].div.div.find_next_sibling().div.div.find_next_sibling().div.div.a.find_next_sibling().div.find_next_sibling().div.div.div.find_next_sibling().h5.span.span.a.string) == "Nazry Bahrawi":
#         nazry_count += 1
#         # Check if there are many comments on the post which would indicate it is a reflection
#         if len(posts[i].div.findAll('div')[1].div.find_next_sibling().form.div.div.find_next_siblings()[1].ul.li.find_next_siblings()) > 15:
#             reflection_count += 1
#             reflection_list.append(i)
#
#
# print("There are " + str(nazry_count) + " posts by Nazry")
# print("Of which " + str(reflection_count) + " are reflection prompts")
# Debug print for the reflections list
# print(reflection_list)

# Debug print for the post text
# print(posts[30].div.div.find_next_sibling().div.div.find_next_sibling().div.find_next_sibling().getText())
# debug print for reflection submissions
# print(len(posts[30].div.div.find_next_sibling().div.find_next_sibling().div.div.find_next_sibling().find_next_sibling().ul.li.find_next_siblings()))
#reflections_dict = {}
# for num in reflection_list:
#     texts = []
#     text_count = len(posts[num].div.div.find_next_sibling().div.find_next_sibling().div.div.find_next_sibling().find_next_sibling().ul.li.find_next_siblings())
#     prompt = posts[num].div.div.find_next_sibling().div.div.find_next_sibling().div.find_next_sibling().getText()
#     # Append the first text before it's siblings
#     texts.append(posts[num].div.div.find_next_sibling().div.div.find_next_sibling().div.find_next_sibling().getText())
#     for t in range(text_count):
#         texts.append(posts[num].div.div.find_next_sibling().div.find_next_sibling().div.div.find_next_sibling().find_next_sibling().ul.li.find_next_siblings()[t].div.div.div.find_next_sibling().div.div.div.div.getText())
#     reflections_dict[num] = (prompt, texts)


#print(posts[0].div.findAll('div')[1].div.prettify())
#print(len(posts[0].div.findAll('div')[1].div.find_next_sibling().form.div.div.find_next_siblings()[1].ul.li.find_next_siblings()))
