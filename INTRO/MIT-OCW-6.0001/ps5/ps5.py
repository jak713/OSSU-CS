# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Julia Kaczmarek
# Collaborators: None
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
        #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
        #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory:
    def __init__(self, guid: str, title: str, description: str, link: str, pubdate: datetime):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase: str):
        if self.is_valid(phrase):
            self.phrase = phrase
        else:
            return f"The phrase '{phrase}' is not valid because it contains punctuation. Try again."
        
    def is_valid(self, phrase):
        return string.punctuation not in phrase
    
    def is_phrase_in(self, text):
        for char in string.punctuation:
            text = text.replace(char, " ")

        words = text.strip().split()
        words = [word.lower().strip(string.punctuation) for word in words if word not in string.punctuation]
        phrase_words = self.phrase.lower().split()

        return any(words[i:i + len(phrase_words)]==phrase_words for i in range(len(words) - len(phrase_words) + 1)) # any checks if any of the i:i+len(phrase_words) == phrase_words is True, e.g. 0:2, 1:3, etc. Cheking for consecutive matches as opposed to using join and searching for substrings
    

# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        title = story.get_title()
        return self.is_phrase_in(title)

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        description = story.get_description()
        return self.is_phrase_in(description)

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, input_time: str):
        format = "%d %b %Y %H:%M:%S"
        self.trigger_datetime = datetime.strptime(input_time, format)



# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.pubdate.tzinfo != None:
            self.trigger_datetime = self.trigger_datetime.replace(tzinfo=pytz.timezone("GMT"))  
        return self.trigger_datetime.timestamp() >= story.pubdate.timestamp()

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.pubdate.tzinfo != None:
            self.trigger_datetime = self.trigger_datetime.replace(tzinfo=pytz.timezone("GMT")) 
        return  self.trigger_datetime.timestamp() <= story.pubdate.timestamp()

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)


# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return (self.trigger1.evaluate(story) and self.trigger2.evaluate(story))


# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return (self.trigger1.evaluate(story) or self.trigger2.evaluate(story))

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories: list, triggerlist: list) -> list:
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    triggered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                triggered_stories.append(story)

    return triggered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11

def read_trigger_config(filename: str) -> list:
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_list = []
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    for line in lines:
        line = line.split(',')
        if line[0] == "ADD":
            for name in line[1:]:
                trigger_list.append(globals()[name])
        else:
            globals()[line[0]] = help_trigger_config(line[1], " ".join(line[2:]))

    return trigger_list

def help_trigger_config(class_type: str, content: str) -> object:
    if class_type == "TITLE":
        return TitleTrigger(content)
    elif class_type == "DESCRIPTION":
        return DescriptionTrigger(content)
    elif class_type == "AFTER":
        return AfterTrigger(content)
    elif class_type == "BEFORE":
        return BeforeTrigger(content)
    elif class_type == "NOT":
        return NotTrigger(content)
    elif class_type == "AND":
        t1, t2 = content.split()
        return AndTrigger(globals()[t1], globals()[t2])
    elif class_type == "OR":
        t1, t2 = content.split()
        return OrTrigger(globals()[t1], globals()[t2])

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Epstein")
        t2 = DescriptionTrigger("Epstein")
        t3 = DescriptionTrigger("Trump")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")
            stories = filter_stories(stories, triggerlist)

            # Note: ran into problems with Yahoo, but equally I don't really like Yahoo news so removed completely

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

