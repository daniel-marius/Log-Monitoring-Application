from event.event import Event
from file.file import File
from utils.utils import Utils


FILE_NAME = "logs.log"
NEW_FILE_NAME = "warning_error_logs.log"
ERROR_MINUTES_THRESHOLD = 10
WARNING_MINUTES_THRESHOLD = 5


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


    def reorder_events_by_pid_time(self, events):
        """Uses methods from Utils to sort events"""
        return Utils.sort_events_by_pid_time(events)
    

    def select_events(self, events):
        """Selects events based on total duration"""

        # Used to check against duplicate pids
        seen = set()
        # Add warning + error events 
        warning_events = []

        for i in range(0, len(events), 2):
            # Get difference (endtime - starttime) for adjacents jobs with different timestamps
            diff = Utils.get_seconds_from_time(events[i]["timestamp"]) - Utils.get_seconds_from_time(events[i + 1]["timestamp"])
            
            # Calculate diff in minutes
            timestamp_in_minutes = Utils.extract_seconds_minutes(diff)[0]

            # Total duration for a job event
            total_duration = Utils.format_output_minutes_seconds(diff)
            print(f"Total duration: {total_duration} for event: {events[i]["event_type"]} with pid: {events[i]["pid"]}")
            
            # Select jobs with duration greater than a threshold
            if (timestamp_in_minutes >= WARNING_MINUTES_THRESHOLD or timestamp_in_minutes >= ERROR_MINUTES_THRESHOLD) and (events[i]["pid"] not in seen):
                seen.add(events[i]["pid"])
                warning_events.append(events[i])

        print('\n')

        # Transform list of event
        warning_events = [Event.select_properties(event) for event in warning_events]
        # Write job report
        self.write_job_report(warning_events)
        print('\n')


    def write_job_report(self, events):
        """Uses helper class File to write content to file"""
        File.write_to_file(NEW_FILE_NAME, events)


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

        # Reorder job events
        reorder_job_events = log_monitoring_application.reorder_events_by_pid_time(job_events)

        # Calculate job events duration
        # Select job events based duration
        log_monitoring_application.select_events(reorder_job_events)

    except Exception as ex:
        print(f"Exception found in application: {ex}")