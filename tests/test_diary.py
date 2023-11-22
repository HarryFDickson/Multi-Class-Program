from lib.diary import *
from lib.diary_entries import *


def test_returns_empty_list():
    myDiary = Diary()
    assert myDiary.all() == []

def test_add_adds_entry_to_diary_list():
    myDiary = Diary()
    entry1 = DiaryEntry("Nick", "Torkupine")
    myDiary.add(entry1)
    assert myDiary.all() == [entry1]

def test_count_words_returns_0():
    myDiary = Diary()
    assert myDiary.count_words() == 0

def test_count_words_returns_correct_result():
    myDiary = Diary()
    entry1 = DiaryEntry("Nick", "Torkupine")
    myDiary.add(entry1)
    assert myDiary.count_words() == 2

def test_phone_number_extractor_returns_a_number():
    myDiary = Diary()
    entry1 = DiaryEntry("Nick", "07894654198")
    entry2 = DiaryEntry("Nick1", "07894554393")
    entry3 = DiaryEntry("Nick2", "Contents")
    entry4 = DiaryEntry("Nick3", "07894674189")
    myDiary.add(entry1)
    myDiary.add(entry2)
    myDiary.add(entry3)
    myDiary.add(entry4)
    extractor = PhoneNumberExtractor(myDiary)
    assert extractor.extract() == ["07894654198", "07894554393", "07894674189"]

def test_best_entry_correct_result():
    myDiary = Diary()
    entry1 = DiaryEntry("Nick", "Torkupine and a bunch of other words")
    myDiary.add(entry1)
    assert myDiary.find_best_entry_for_reading_time(1, 9) == entry1

