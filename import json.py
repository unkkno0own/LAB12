import json

# Функція для зчитування даних з JSON файлу
def read_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Помилка: Файл {file_path} не знайдено.")
    except json.JSONDecodeError:
        print("Помилка: Невірний формат JSON.")
    return []

# Функція для запису даних у JSON файл
def write_json(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Дані успішно збережено у файл {file_path}.")
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")

# Функція для виведення вмісту JSON файлу
def display_json(file_path):
    data = read_json(file_path)
    if data:
        print("Вміст JSON файлу:")
        for employee in data:
            print(f"Прізвище: {employee['Прізвище']}, Адреса: {employee['Адреса']}, Посада: {employee['Посада']}")
    else:
        print("Файл порожній або не знайдено.")

# Функція для додавання нового співробітника
def add_employee(file_path):
    data = read_json(file_path)
    
    # Введення нового співробітника
    last_name = input("Введіть прізвище співробітника: ")
    address = input("Введіть адресу співробітника: ")
    position = input("Введіть посаду співробітника: ")
    
    # Додавання нового запису
    new_employee = {"Прізвище": last_name, "Адреса": address, "Посада": position}
    data.append(new_employee)
    
    # Запис оновлених даних в JSON файл
    write_json(file_path, data)

# Функція для видалення співробітника
def delete_employee(file_path):
    data = read_json(file_path)
    
    # Введення прізвища для видалення
    last_name_to_delete = input("Введіть прізвище співробітника для видалення: ")
    
    # Пошук і видалення співробітника
    new_data = [employee for employee in data if employee['Прізвище'] != last_name_to_delete]
    
    # Якщо зміни були, збережемо файл
    if len(new_data) != len(data):
        write_json(file_path, new_data)
        print(f"Співробітник з прізвищем {last_name_to_delete} успішно видалений.")
    else:
        print(f"Співробітник з прізвищем {last_name_to_delete} не знайдений.")

# Функція для пошуку співробітників за літерою прізвища
def search_by_letter(file_path):
    data = read_json(file_path)
    
    # Введення літери для пошуку
    letter = input("Введіть літеру для пошуку співробітників за прізвищем: ").lower()
    
    # Пошук співробітників, чиє прізвище починається на введену літеру
    found = [employee for employee in data if employee['Прізвище'][0].lower() == letter]
    
    if found:
        print(f"Співробітники, чиє прізвище починається на '{letter.upper()}':")
        for employee in found:
            print(f"Прізвище: {employee['Прізвище']}, Адреса: {employee['Адреса']}, Посада: {employee['Посада']}")
    else:
        print(f"Немає співробітників, чиє прізвище починається на '{letter.upper()}'.")
    
# Функція для виконання завдання за варіантом
def task_solution(file_path):
    data = read_json(file_path)
    
    # Пошук співробітників, чиє прізвище починається на введену літеру
    letter = input("Введіть літеру для пошуку співробітників за прізвищем: ").lower()
    
    # Пошук співробітників, чиє прізвище починається на введену літеру
    found = [employee for employee in data if employee['Прізвище'][0].lower() == letter]
    
    if found:
        print(f"Співробітники, чиє прізвище починається на '{letter.upper()}':")
        for employee in found:
            print(f"Прізвище: {employee['Прізвище']}, Адреса: {employee['Адреса']}, Посада: {employee['Посада']}")
        
        # Збереження результату в новий файл
        output_file = "search_results.json"
        write_json(output_file, found)
    else:
        print(f"Немає співробітників, чиє прізвище починається на '{letter.upper()}'.")
        
# Функція для пошуку співробітників за полем (Прізвище, Адреса, Посада)
def search_by_field(file_path):
    data = read_json(file_path)
    
    # Якщо дані не знайдені
    if not data:
        print("Немає даних для пошуку.")
        return

    # Запит на вибір поля для пошуку
    print("Виберіть поле для пошуку:")
    print("1. Прізвище")
    print("2. Адреса")
    print("3. Посада")
    field_choice = input("Введіть номер вибраного поля: ")

    # Запит для введення значення для пошуку
    search_value = input("Введіть значення для пошуку: ").lower()

    found = []

    # Виконання пошуку за вибраним полем
    if field_choice == "1":
        # Пошук за прізвищем
        found = [employee for employee in data if search_value in employee['Прізвище'].lower()]
    elif field_choice == "2":
        # Пошук за адресою
        found = [employee for employee in data if search_value in employee['Адреса'].lower()]
    elif field_choice == "3":
        # Пошук за посадою
        found = [employee for employee in data if search_value in employee['Посада'].lower()]
    else:
        print("Невірний вибір.")
        return

    # Виведення результатів пошуку
    if found:
        print(f"Знайдені результати за значенням '{search_value}':")
        for employee in found:
            print(f"Прізвище: {employee['Прізвище']}, Адреса: {employee['Адреса']}, Посада: {employee['Посада']}")
    else:
        print(f"Нічого не знайдено для '{search_value}'.")

# Головна функція для взаємодії з користувачем
def main():
    file_path = "employees.json"
    
    while True:
        print("\nМеню:")
        print("1. Вивести вміст JSON файлу")
        print("2. Додати нового співробітника")
        print("3. Видалити співробітника")
        print("4. Пошук співробітників за літерою прізвища")
        print("5. Виконати завдання та записати результат у новий файл")
        print("6. Пошук співробітників за полем")
        print("7. Вийти")
        
        choice = input("Виберіть дію: ")
        
        if choice == "1":
            display_json(file_path)
        elif choice == "2":
            add_employee(file_path)
        elif choice == "3":
            delete_employee(file_path)
        elif choice == "4":
            search_by_letter(file_path)
        elif choice == "5":
            task_solution(file_path)
        elif choice == "6":
            search_by_field(file_path)
        elif choice == "7":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
