import os

print("Started clearing old logs")

def filter_log(input_file, output_file, texts_to_keep):
    try:
        # Read input file and filter lines
        with open(input_file, 'r') as f_input:
            lines = f_input.readlines()

        filtered_lines = [line for line in lines if any(text in line for text in texts_to_keep)]
        print("Writing to file..")
        # Write filtered lines to output file
        with open(output_file, 'w') as f_output:
            f_output.writelines(filtered_lines)

        print(f"Filtered {input_file} and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found")

def process_logs(texts_to_keep):
    print("Processing logs")
    try:
        current_dir = os.getcwd()  # Get current directory
        filtered_logs_dir = os.path.join(current_dir, 'filtered_logs')
        os.makedirs(filtered_logs_dir, exist_ok=True)

        log_files = [filename for filename in os.listdir(current_dir) if filename.endswith('.log')]
        print(f"Found {len(log_files)} log file(s)")

        for i, filename in enumerate(log_files):
            input_file = os.path.join(current_dir, filename)
            output_file = os.path.join(filtered_logs_dir, f"{filename.replace('.log', '')}-filtered.txt")
            filter_log(input_file, output_file, texts_to_keep)
            print(f"File {i + 1} done")

        print("All log files processed")

    except FileNotFoundError:
        print("Error: file(s) not found.")

# Example usage:
texts_to_keep = [
    '[Async Chat Thread',
    '[User Authenticator'
]  # Replace with the list of texts you want to keep

process_logs(texts_to_keep)
input('enter to quit ')