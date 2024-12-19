import re
pattern = r"(h(ma)*|ma|mh(a)*|hmh(a)*)"
user_input = input("Ingresa una cadena para validar: ")
if re.fullmatch(pattern, user_input):
    print(f"'{user_input}' es válido según la expresión regular.")
else:
    print(f"'{user_input}' NO es válido según la expresión regular.")
