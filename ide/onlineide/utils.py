import uuid
import subprocess


def create_code_file(code, language):
    file_name = str(uuid.uuid4()) + "." + language
    with open("code/" + file_name, "w") as f:
        f.write(code)
    return file_name


def execute_file(file_name, language):
    if language == "cpp":
        subprocess.run(["g++", "code/" + file_name], capture_output=True, text=True)
        subprocess.run(["./a.exe"])
