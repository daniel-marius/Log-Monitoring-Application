from file.file import File
from utils.utils import Utils


FILE_NAME = "logs.log"
NEW_FILE_NAME = "warning_error_logs.log"


class LogsMonitoringApplication:
    """Class that implements logs monitoring"""
    def __init__(self):
        self.events = []


    def identify_event_type(self, event_type):
        """Uses helper class method from Utils to filter based on event type"""
        return Utils.filter_events(self.events, "event_type", event_type)


    def print_events(self, events):
        """Uses helper class method from Utils to print events"""
        Utils.print_table(events)


    def read_from_file(self, file_name):
        """Read from file using helper class File"""
        file_content = File.read_from_file(file_name)
        self.events.extend(file_content)


if __name__ == "__main__":
    try: 
        
        # Create class instance
        log_monitoring_application = LogsMonitoringApplication()

        # Read from file
        log_monitoring_application.read_from_file(FILE_NAME)

        # Filter events by "JOB"
        job_events = log_monitoring_application.identify_event_type(event_type="JOB")
        log_monitoring_application.print_events(job_events)

        # Filter events by "TASK"
        task_events = log_monitoring_application.identify_event_type(event_type="TASK")
        log_monitoring_application.print_events(task_events)

    except Exception as ex:
        print(f"Exception found in application: {ex}")