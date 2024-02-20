from LogSink import LogSink

class ConsoleLogSink(LogSink):
    def log(self, message):
        print(message)
