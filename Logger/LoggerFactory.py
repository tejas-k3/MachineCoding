from Logger import Logger
from ConsoleLogSink import ConsoleLogSink
from FileSink import FileSink

class LoggerFactory:
    @staticmethod
    def create_logger(log_type, filename=None):
        if log_type == 'console':
            return Logger()
        elif log_type == 'file':
            if filename:
                return Logger(FileSink(filename))
            else:
                return Logger()
