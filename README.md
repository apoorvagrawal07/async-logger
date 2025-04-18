async-logger

A basic logging library that can be used by applications to log messages. The library can handle message logging efficiently and reliably, offering basic configuration options.
Key Features:
Initialize the Library and log messages to the desired sink.
Logger has the following capabilities-
Accepts messages from client(s)
A logger can have one or more sinks associated with it. 
Supports defined message levels.
Enriches message with current timestamp while directing message to a sink
Logger is initialized with a configuration eg:logger name, sink(s), buffer size, etc.
Logger support both sync and async logging. 
For Async logger buffer size would determine the maximum inflight messages.
Messages are ordered. Messages reach the sink in the order of they were sent.
Support writes from multiple-threads.
Not any data loss.

Sink:
There can be various types of sink (file, stdout, database).  
Sink has a destination.
For this round you may create STDOUT sink, which would print the message to the console. 
Sink has an associated log level. Any message with the level lower than the sink level should be discarded. 
Message
has content which is of type string
has a level associated with it
has a timestamp

Log Level
DEBUG, INFO, WARN, ERROR, FATAL ; in order of priority. ERROR has higher priority than INFO.
Add test cases to demonstrate sync logging, async logging and concurrent logging requests

Sending messages
Sink need not be mentioned while sending a message to the logger library. 
You specify message content and level while sending a message
Logger configuration (see sample below)
Specifies all the details required to use the logger library.
Example:
time format
logging level
sink type
Logger type sync/async
details required for sink (eg file location)); this depends on sink type.

Sample Config:
Ts_format: any format
log_level:INFO
logger_type:ASYNC
buffer_size:25
sink_type:STDOUT
 
Sample Output Log Entry
03-01-2024-09-30-00 [INFO] This is a sample log message. 

Sample test case:

Input:
Configuration of the logger is console logging with Info level.
log.info(“Info message”)
log.warn(“Warn message”)
log.debug(“Debug message”)
log.error(“Error message”)

Output:
03-01-2024-09-30-00 [INFO] Info message   
03-01-2024-09-30-00 [WARN] Warn message   
03-01-2024-09-30-02 [ERROR] Error message

