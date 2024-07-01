import os
import time

start_time = time.time()

print("Started clearing old logs")

def filter_log(input_file, output_file, texts_to_keep):
    try:
        # Read input file and filter lines
        with open(input_file, 'r', encoding='utf-8') as f_input:
            lines = f_input.readlines()

        filtered_lines = [line for line in lines if any(text in line for text in texts_to_keep)]
        chatresult = []  # Create an empty list to store the filtered lines without "Async Chat Thread" string
        for string in filtered_lines:
            chatresult.append(string.replace("[Async Chat Thread -", '').replace("/INFO]", '').replace(" - InteractiveChat: [Not Secure]", '').replace("[Craft Scheduler Thread - ", ''))

        print("Writing to file..")
        with open(output_file, 'w', encoding='utf-8') as f_output:
            f_output.writelines(chatresult)

        print(f"Filtered {input_file}")

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
    '[User Authenticator',
    'InteractiveChat/INFO'
]  # Replace with the list of texts you want to keep

process_logs(texts_to_keep)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"done in: {elapsed_time} seconds")


input('enter to quit ')
