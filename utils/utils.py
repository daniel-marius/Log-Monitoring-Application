class Utils:
    """Utility class with several methods used in main file"""

    @staticmethod
    def filter_events(events, key, value):
        """Filters list of dictionaries using list comprehension"""
        return [event for event in events if event[key] == value]


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
