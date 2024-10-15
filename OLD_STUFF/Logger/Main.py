from LogLevel import LogLevel
from LoggerFactory import LoggerFactory

if __name__ == "__main__":
    # console_logger_factory = LoggerFactory.
    console_logger = LoggerFactory.create_logger('console')
    console_logger.log(LogLevel.INFO, "This is an info message")

    file_logger = LoggerFactory.create_logger('file', "log.txt")
    file_logger.log(LogLevel.WARNING, "This is a warning message")
