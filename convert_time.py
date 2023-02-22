import re
def convert_to_24_hour_time(time_str):
    """Converts a time string to 24-hour time format."""
    time_parts = time_str.split(":")
    hour = int(time_parts[0])
    minute = int(time_parts[1][:2])
    am_pm = time_parts[1][2:].strip().lower()
    if am_pm == "pm" and hour != 12:
        hour += 12
    elif am_pm == "am" and hour == 12:
        hour = 0
    return f"{hour:02d}:{minute:02d}"

with open("nova_all_old.txt", "r", encoding="utf-8") as input_file:
    with open("nova_all.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            print(line)
            # Define the pattern to search for times in the line
            time_pattern = re.compile(r"\b(\d{1,2}):(\d{2})\s*([ap]m)\b", re.IGNORECASE)

            # Replace every occurrence of a time in the line with the 24-hour time format
            line = time_pattern.sub(lambda m: convert_to_24_hour_time(m.group(0)), line)
            output_file.write(line)

