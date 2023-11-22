"""
# As a user
# So that I can record my experiences
# I want to keep a regular diary

# As a user
# So that I can reflect on my experiences
# I want to read my past diary entries

# As a user
# So that I can reflect on my experiences in my busy day
# I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

# As a user
# So that I can keep track of my contacts
# I want to see a list of all of the mobile phone numbers in all my diary entries
"""

# File: lib/diary.py

class Diary:
    def __init__(self):
        self.newList = []

    def add(self, entry): # Adds an instance of DiaryEntry to the list
        self.newList.append(entry)

    def all(self): # Returns all entries in list form
        return self.newList

    def count_words(self): # Returns amount of words in the whole list
        var = 0
        for i in self.newList:
            var += i.count_words()
        return var

    def reading_time(self, wpm): # Returns amount of time it'll take to read all of the entries in the list
        var = 0
        for i in self.newList:
            var += i.reading_time(wpm)
        return var

    def find_best_entry_for_reading_time(self, wpm, minutes): # Returns the entry which is most convenient to the user based on time
        empty_list = []
        words = minutes * wpm
        for i in self.newList:
            if i.count_words() <= words:
                empty_list.append(i)
        num = float('inf')
        lowest_words = None
        for i in empty_list:
            if i.count_words() < num:
                lowest_words = i
        return lowest_words



class PhoneNumberExtractor:
    def __init__(self, diary):
        self.diary = diary

    def extract(self): # Loops through each word in an entry and finds a number beginning with 0 and has 11 numbers
        empty = []
        for i in self.diary.all():
            formatted = i.format()
            split_text = formatted.split()
            print(split_text)
            for j in split_text:
                if j[0] == "0" and len(j) == 11:
                    empty.append(j)
        return empty