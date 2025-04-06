from data.LogLevel import LogLevel as lgl

class Logger:
    def __init__(self,timeFormat, sinkType, logLevel:lgl, loggerType, bufferSize):
        self.timeFormat = timeFormat
        self.sinkType = sinkType
        self.logLevel = logLevel
        self.loggerType = loggerType
        self.bufferSize = bufferSize

    def getLogger(self):
        return Logger
        