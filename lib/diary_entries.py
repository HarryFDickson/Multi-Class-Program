class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        string = f"{self.title} {self.contents}"
        if type(string) is not str:
            raise Exception("NOT A STRING!!!")
        split_string = string.split(" ")
        count = len(split_string)
        return count

    def reading_time(self, wpm):
        string = self.title + self.contents
        split_string = string.split()
        word_count = len(split_string)
        return word_count / wpm

    def reading_chunk(self, wpm, minutes):
        string = f"{self.title} {self.contents}"
        split_string = string.split()
        words = wpm / minutes
        joined_text = " ".join(split_string[0:int(words)])
        return joined_text