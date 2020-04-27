# 359. Logger Rate Limiter

"""
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
"""

"""
Approach - Using a HashMap
1. When ever there is an incoming message, check the hash map if the message is already present or not. 
2. If it is not present, add the message as key and timestamp as its value. When ever we are inserting, it means the message was not printed anytime before. So, we can return True.
3. If the message is already present, then it means we would have printed it sometime before. So, check the timestamp of the message recorded. 
4. If the latest timestamp - 10 is greater than or equal to previuosly reocrded time, then we can return True and update the latest timestamp of whn it is printed in the hash map.
5. If the difference between latest timestamp and the timestamp previuosly recorded is not greater than or equal to 10, then return False 
"""

# Time Complexity - O(1)
# Space Complexity - O(N) as we are using hash map

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        # Not present
        if message not in self.hash_map:
            self.hash_map[message] = timestamp
            return True
		# Already present
        else:            
            if timestamp - self.hash_map[message] >= 10:
                self.hash_map[message] = timestamp
                return True
            else:
                return False

        # Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)