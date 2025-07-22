class Utils:
    """Utility class with several methods used in main file"""

    @staticmethod
    def extract_seconds_minutes(input_seconds):
        """Returns minutes and seconds from number of seconds as input"""
        minutes, seconds = divmod(input_seconds, 60)
        return [minutes, seconds]
    

    @staticmethod
    def filter_events(events, key, value):
        """Filters list of dictionaries using list comprehension"""
        return [event for event in events if event[key] == value]
    

    @staticmethod
    def format_output_minutes_seconds(input_seconds):
        """
        Uses methods extract_seconds_minutes, then formats an output with minutes and seconds
        e.g. -> 15m 45s
        """
        convert_input = Utils.extract_seconds_minutes(input_seconds)
        return '{:02d}m {:02d}s'.format(convert_input[0], convert_input[1])


    @staticmethod 
    def print_table(input_list):
        """Displays a list of dictionaries as table shape"""

        # Get keys from first dictionary in input list
        headers = [*input_list[0]]

        # Step 1: Calculate column widths based on length of keys and values from input list dictionaries
        col_widths = {
            key: max(len(str(key)), max(len(str(d[key])) for d in input_list)) for key in headers
        }

        # Step 2: Generate header row by adding necessary space (col_widths[key]) between keys
        header_row = " | ".join(f"{key:<{col_widths[key]}}" for key in headers)

        # Step 3: Print table
        print(header_row)
        print("-" * len(header_row))
        for row in input_list:
            # Print every row from input list by adding necessary space (col_widths[key]) between values
            print(" | ".join(f"{str(row[key]):<{col_widths[key]}}" for key in headers))
        print("\n")


    @staticmethod
    def get_seconds_from_time(time):
        """Get seconds from time."""
        h, m, s = str(time).split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    @staticmethod
    def sort_events_by_pid_time(events):
        """Sort ascending list of dictionaries base on two criteria"""
        return sorted(events, key = lambda v: (v["pid"], v["time"]), reverse=False)
