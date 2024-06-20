import os
import csv

# Function to read data from CSV
def read_data_from_csv(file_name):
    data = []
    file_path = os.path.join('Data', file_name)  # Constructing the file path
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header
        for row in reader:
            data.append(row)
    return header, data

# Import CSV Test Data
if __name__ == "__main__":
    csv_file = 'LineData.csv'
    header, data = read_data_from_csv(csv_file)


# Summarize adjacent rows
def summarize_adjacent_rows(file_name):
    data = []
    summarized_data = []
    file_path = os.path.join('Data', file_name)  # Constructing the file path
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
        current_color = None
        current_gallons = 0
        for row in reader:
            color = row['COLOR']
            gallons = int(row['GALLONS'])

            if color != current_color:
                # Append the summarized row for the previous color group
                if current_color is not None:
                    summarized_data.append({'COLOR': current_color, 'GALLONS': current_gallons})
                # Start new group for current color
                current_color = color
                current_gallons = gallons
            else:
                # Add gallons to current group
                current_gallons += gallons

        # Append the last summarized row
        if current_color is not None:
            summarized_data.append({'COLOR': current_color, 'GALLONS': current_gallons})

    return summarized_data

# Test Use
if __name__ == "__main__":
    csv_file = 'LineData.csv'
    summarized_data = summarize_adjacent_rows(csv_file)

    # Print summarized data
    print("Summarized Data:")
    for row in summarized_data:
        print(row['COLOR'], row['GALLONS'])