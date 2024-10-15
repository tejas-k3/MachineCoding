from LogSink import LogSink
import os

class FileSink(LogSink):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        try:
            with open(self.filename, 'a') as file:
                file.write(message + '\n')
        except IOError as e:
            print("Error writing to file:", e)
