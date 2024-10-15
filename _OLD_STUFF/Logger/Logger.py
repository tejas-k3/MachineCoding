from LogLevel import LogLevel

class Logger:
    _instance = None

    def __new__(cls, log_sink=None):  # Accept log_sink as an argument
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_level = LogLevel.INFO
            cls._instance.log_sink = log_sink  # Assign log_sink
        return cls._instance

    def set_log_level(self, log_level):
        self.log_level = log_level

    def set_log_sink(self, log_sink):
        self.log_sink = log_sink

    def log(self, log_level, message):
        if log_level.value >= self.log_level.value:
            log_message = f"[{log_level.name}] {message}"
            if self.log_sink:
                self.log_sink.log(log_message)
            else:
                print(log_message)  # Fallback to printing if log_sink is not set
