import os

CSV_FILE_NAME = "csv_file.csv"
TXT_FILE_NAME = "txt_file.txt"
JSON_FILE_NAME = "json_file.json"

DATA_FOLDER = "data"
main_path = os.getcwd()

csv_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), CSV_FILE_NAME)
text_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), TXT_FILE_NAME)
json_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), JSON_FILE_NAME)