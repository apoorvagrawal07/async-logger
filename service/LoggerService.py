import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import queue
import asyncio
from SinkService import SinkService as sinkService
from datetime import datetime
from data.SinkType import SinkType as stype
from models.Logger import Logger as logger
from data.LogLevel import LogLevel as logLevel

class LoggerService:    
    def __init__(self,logger: logger):
        self.logger = logger
        if logger.loggerType == "ASYNC":
            self.queue = asyncio.Queue()
        self.running = True
        self.sinkSvc = sinkService()
        self.task = asyncio.create_task(self.async_log())
        self.running = True
    
    async def async_log(self):
        while self.running:
            if not self.queue.empty():
                for i in range(0, self.logger.bufferSize if self.logger.bufferSize < self.queue.qsize() else self.queue.qsize()):
                    message =  await self.queue.get()
                    self.sinkSvc.sinkOut(message=message,sinkType=self.logger.sinkType)
                    if(i == self.logger.bufferSize-1):
                        print("Buffer limit reached!")
            else:
                return 

    async def log(self, logLevel : logLevel, message):
      now = datetime.now()
      date_time = now.strftime("%Y-%m-%d %H:%M:%S")

      if logLevel.value >= self.logger.logLevel.value:
        out = f"{date_time} [{logLevel.name}] {message}"

        if self.logger.loggerType == "SYNC":  
            self.sinkSvc.sinkOut(message=out,sinkType=self.logger.sinkType)
            
        else:
           try:
               self.queue.put_nowait(out)
           except asyncio.QueueFull:
               print("Log buffer full, dropping message")

    async def debug(self,message):
       await self.log(logLevel.DEBUG,message)
 
    async def info(self,message):
       await self.log(logLevel.INFO,message)

    async def warn(self,message):
       await self.log(logLevel.WARN,message)
  
    async def error(self,message):
       await self.log(logLevel.ERROR,message)

    async def fatal(self,message):
       await self.log(logLevel.FATAL,message)

    def shutdown(self):
        if self.queue.empty():
            print("Logger Shutdown!")
            self.running = False
            return
            
async def main():
    newLog = logger(timeFormat = "time", sinkType = stype.FILE, logLevel = logLevel.INFO, loggerType = "ASYNC", bufferSize=5)
    log = LoggerService(newLog)
    await log.warn("hello")
    await log.warn("hello")
    await log.warn("hello")
    await log.warn("hello")
    await log.warn("hello")
    await log.warn("hello")
    await log.info("hey there")
    await log.info("hey there")
    await log.info("hey there")
    await log.info("hey there")
    await log.info("hey there")
    await log.info("hey there")
    await log.info("hey there")
    await log.info("hey there")

    log.shutdown()
    
if __name__ == "__main__":
    asyncio.run(main())