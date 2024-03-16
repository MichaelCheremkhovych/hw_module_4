def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                surname, salary_str = line.strip().split(',') # Розділяємо рядок на прізвище та зарплату за комою
                salary = int(salary_str) # Перетворюємо зарплату в ціле число
                total += salary # Додаємо зарплату до загальної суми
                count += 1 # Лічильник кількості розробників
            
        average = total / count if count > 0 else 0 # Обчислюємо середню зарплату
        
        return total, average
        
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None, None

# Приклад використання
total, average = total_salary("D:\git_projects\hw_module_4\hw_4_1.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
