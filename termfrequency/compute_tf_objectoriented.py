"""Compute term frequencies for an input file using a object-oriented style"""

import sys
import re
import operator
import string
from abc import ABCMeta


# pylint: disable=too-few-public-methods
class TFExercise:
    """ Defines the base class for all other defined classes """

    # pylint: disable=metaclass-assignment
    __metaclass__ = ABCMeta

    def info(self):
        """ Set the name of the abstract base class """
        return self.__class__.__name__


class DataStorageManager(TFExercise):
    """ Models the contents of the file """

    def __init__(self, path_to_file):
        """ Define the constructor for the DataStorageManager """
        with open(path_to_file) as f:
            self._data = f.read()
        pattern = re.compile(r"[\W_]+")
        self._data = pattern.sub(" ", self._data).lower()

    def words(self):
        """ Returns the list words in storage """
        return self._data.split()

    def info(self):
        """ Display a textual representation of the DataStorageManager """
        return (
            super(DataStorageManager, self).info()
            + ": My major data structure is a "
            + self._data.__class__.__name__
        )


class StopWordManager(TFExercise):
    """ Models the stop word filter """

    def __init__(self):
        """ Define the constructor for the StopWordManager """
        with open("stopwords/stop_words.txt") as f:
            self._stop_words = f.read().split(",")
        # add single-letter words
        self._stop_words.extend(list(string.ascii_lowercase))

    def is_stop_word(self, word):
        """ Determine if the provided word is a stop word """
        return word in self._stop_words

    def info(self):
        """ Return a textual representation of the StopWordManager """
        return (
            super(StopWordManager, self).info()
            + ": My major data structure is a "
            + self._stop_words.__class__.__name__
        )


class WordFrequencyManager(TFExercise):
    """ Keeps the word frequency data """

    def __init__(self):
        """ Define the constructor for the WordFrequencyManager """
        self._word_freqs = {}

    def increment_count(self, word):
        """ Keep track of the count for each one of the words """
        if word in self._word_freqs:
            self._word_freqs[word] += 1
        else:
            self._word_freqs[word] = 1

    def sorted(self):
        """ Return a sorted list of the word frequencies under management """
        return sorted(
            self._word_freqs.items(), key=operator.itemgetter(1), reverse=True
        )

    def info(self):
        """ Return a textual representation of the WordFrequencyManager"""
        return (
            super(WordFrequencyManager, self).info()
            + ": My major data structure is a "
            + self._word_freqs.__class__.__name__
        )


class WordFrequencyController(TFExercise):
    """ Controls the process of collecting word frequency data """

    def __init__(self, path_to_file):
        """ Define the constructor for the WordFrequencyManager """
        self._storage_manager = DataStorageManager(path_to_file)
        self._stop_word_manager = StopWordManager()
        self._word_freq_manager = WordFrequencyManager()

    def run(self):
        """ Run the process of collecting word frequency data """
        for w in self._storage_manager.words():
            if not self._stop_word_manager.is_stop_word(w):
                self._word_freq_manager.increment_count(w)

        word_freqs = self._word_freq_manager.sorted()
        for (w, c) in word_freqs[0:25]:
            print(w, " - ", c)


if __name__ == "__main__":
    WordFrequencyController(sys.argv[1]).run()
