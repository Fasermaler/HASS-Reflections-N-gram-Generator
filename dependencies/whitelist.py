#!/usr/bin/python
# -*- coding: utf-8 -*-

# Basic whitelist filter and sentence grabber
# Written by Fasermaler

class whitelist:
    def __init__(self, whitelist_txt):
        self.whitelist_words = []
        self.texts = None
        self.filtered_sentences = []
        self.summary_HR = None

        # Get the whitelisted words
        f = open(whitelist_txt, "r")
        self.whitelist_words = f.read().lower().splitlines()
        self.whitelist_words = [word.strip() for word in self.whitelist_words]
        f.close()

    def filter_whitespace(self, word):
        if word == "":
            return False
        else:
            return True

    def get_texts(self, texts):
        # Convert Prompts into a list of sentences
        self.texts_lower = texts.lower().split(".")
        self.texts_lower = filter(self.filter_whitespace, self.texts_lower)
        self.texts_lower = [word.strip() for word in self.texts_lower]
        self.texts = texts.split(".")
        self.texts = filter(self.filter_whitespace, self.texts)
        self.texts = [word.strip() for word in self.texts]

    # Filer sentences that contain the words of interest
    def filter_sentences(self, max_words=0):

        # Compares every sentence in lowercase to ensure a match
        # Writes the original sentence if there is a match)
        for i in range(len(self.texts)):

            words = self.texts_lower[i].split()
            for word in words:
                if word in self.whitelist_words:

                    self.filtered_sentences.append(self.texts[i])
                    break

            words2 = [words[c] + " " + words[c+1] for c in xrange(len(words)-1)]
            for word in words2:
                if word in self.whitelist_words:
                    if self.texts[i] not in self.filtered_sentences:
                        self.filtered_sentences.append(self.texts[i])
                        break

            words3 = [words[c] + " " + words[c+1] + " " + words[c+2] for c in xrange(len(words)-2)]
            for word in words3:
                print(word)
                print(self.whitelist_words)
                if word in self.whitelist_words:
                    print('yes')
                    if self.texts[i] not in self.filtered_sentences:
                        print(self.texts[i])
                        self.filtered_sentences.append(self.texts[i])
                        break

    # Generate human readable format
    def generate_HR(self):
        print("There are " + str(len(self.filtered_sentences)) + " filtered sentences")
        print("They are as follows: ")
        print(self.filtered_sentences)
        for sentence in self.filtered_sentences:
            print(sentence)

    # Write the HR summary to file
    def write_HR(self, output_file):
        f = open(output_file, "w+")
        f.write("There are " + str(len(self.filtered_sentences)) + " filtered sentences\n\n")
        for sentence in self.filtered_sentences:
            f.write(sentence)
            f.write("\n")
        f.close()

texts = "Lee Gui An With respect to both Ex Machina and Zima Blue, I found that they both highlight something more about the human condition rather than something about super-intelligence. Despite Ava's manipulative nature, we find both a kind of twisted empathy with her and Caleb - she, being trapped within the confines of the institute, has learned to hate humanity for trapping her - expressing a desire to be free, whereas we find empathy for Caleb for being betrayed, for being manipulated, especially after we see how Ava expresses interest in him just to get him to help her escape.Indeed, it would not be hard to imagine that a human-like superintelligence would be a formidable foe at the very least, and an impossible one at worst. And yet, being human-like comes with its own set of positives, as well - we see in Zima Blue a positive expression of human-ness: a desire to find meaning and purpose. Zima, despite his superhuman perception of time, being essentially ageless, finds that his life is devoid of meaning - and chooses a death with purposeful meaning, returning to his original directive, over an eternity in the cosmos. He chooses to return to sub-sapience, to 'revel in the joy of a job well done', rather than face an eternity as a superintelligence without meaning.Indeed, the two works present very different views of superintelligence, or at least of artificial human-equivalent intellect. The elements that cause fear and disgust in Ex Machina are precisely what moves us in Zima Blue - of a machine achieving purpose. I am more and more convinced that rather than worry over what a superintelligence would do, we should worry more what we, as its creators, intend for it to do - for it is we who set up the actions of these machines. We should not worry about superintelligence destroying us all, if we have intended for it to do us good - but rather, we should fear malicious actors who would attempt to construct a superintelligence for selfish gain. The human, rather than the machine, deserves thought.We should not build superintelligence, for humanity as a species is not yet ready to wield such power. And yet, perhaps, it is precisely because no human can be trusted with power, that we should entrust our good future to a machine which is ready to wield absolute power to further the future of our species lest we destroy ourselves.Eldon Lim Yi Duh Ex Machina:I find this story interesting because the AI(Ava) is not “programmed” with the 3 laws of robotics and is allowed to do any action that it deemed right to do this does not artificially limit the possibilities of what an Ava can and will do and we can look into the unrestricted behavior of Ava and see for ourselves if the decisions it makes are ethical. Something that made me sad about the movie is that despite the main protagonist (Caleb) helping the Ava, she did not return the favor and did not help him to escape Nathan’s place. Perhaps Ava have"

texts2 = "Zima Blue is cool. Zima BlUe is a superintelligence."

# Test code
# whitelist = whitelist("whitelist.txt")
# whitelist.get_texts(texts2)
# whitelist.filter_sentences()
# whitelist.generate_HR()
# whitelist.write_HR("white_out.txt")
