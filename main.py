from file.file import File


FILE_NAME = "logs.log"
NEW_FILE_NAME = "warning_error_logs.log"


class LogsMonitoringApplication:
    """Class that implements logs monitoring"""
    def __init__(self):
        self.events = []


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
    except Exception as ex:
        print(f"Exception found in application: {ex}")