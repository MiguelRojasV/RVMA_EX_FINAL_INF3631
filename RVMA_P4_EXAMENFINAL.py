import re
from typing import Optional

dir = ["home", "var", "user", "Documents", "compi"]
extension = ["txt", "docx"]

def parse_file(s: str) -> bool:
    
    if '.' in s:
        path_part, ext_part = s.rsplit('.', 1)
        return parse_path(path_part) and ext_part in extension
    return parse_path(s)

def parse_path(s: str) -> bool:
   
    for dir_name in dir:
        if s.startswith(dir_name):
            return parse_path_p(s[len(dir_name):])
    return False

def parse_path_p(s: str) -> bool:
    if not s:
        return True
    if s.startswith('/'):
        for dir_name in dir:
            if s[1:].startswith(dir_name):
                return parse_path_p(s[1 + len(dir_name):])
    return False

def main():
    user_input = input("Ingrese texto a validar : ")
    is_valid = parse_file(user_input)
    print(f"El texto '{user_input}' es {'valido' if is_valid else 'no es valido'}.")

if __name__ == "__main__":
    main()
