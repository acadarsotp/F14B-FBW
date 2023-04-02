import csv
import json
import time

last_printed_row = None

while True:
    with open('C:/Users/acada/Documents/F14-FBW/input_output/telemetry.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = list(reader)

        # Get the last row
        last_row = rows[-1]

        # If the last row is the same as the last printed row, skip printing it
        if last_row == last_printed_row:
            time.sleep(0.02)  # Wait 50 ms before checking again
            continue

        # Convert the row to a dictionary
        row_dict = {
            "time": float(last_row[0]),
            "lat": float(last_row[1]),
            "long": float(last_row[2]),
            "heading": float(last_row[3]),
            "baralt": float(last_row[4]),
            "radalt": float(last_row[5]),
            "pitch": float(last_row[6]),
            "bank": float(last_row[7]),
            "yaw": float(last_row[8]),
            "ias": float(last_row[9]),
            "tas": float(last_row[10]),
            "gx": float(last_row[11]),
            "gy": float(last_row[12]),
            "gz": float(last_row[13]),
            "aoa": float(last_row[14]),
            "vs": float(last_row[15])
        }

        # Convert the dictionary to JSON
        row_json = json.dumps(row_dict)

        # Print the JSON
        print(row_json)

        # Set the last printed row to the current row
        last_printed_row = last_row

    time.sleep(0.02)  # Wait 50 ms before checking again

