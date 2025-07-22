from datetime import datetime
from enum import Enum


class EventType(Enum):
    """ Class representing an event type"""
    JOB = 1
    TASK = 2


class Event:
    """ Class representing an event with several proprties
        timestamp -> datetime 
        description -> string
        event_type -> Enum
        time -> string
        pid -> int
    """
    def __init__(self, str_args):
        args = str_args.split(',')
        event_type = args[1].split(' ')[1] 
        self.timestamp = datetime.strptime(args[0], '%H:%M:%S').time()
        self.description = args[1]
        self.event_type = EventType.JOB.name if event_type == 'job' else EventType.TASK.name
        self.time = args[2]
        self.pid = int(args[3])


    @staticmethod
    def select_properties(event):
        """Returns less properties from a given event"""
        return {
            "timestamp": event["timestamp"],
            "description": event["description"],
            "time": event["time"],
            "pid": event["pid"],
        }
