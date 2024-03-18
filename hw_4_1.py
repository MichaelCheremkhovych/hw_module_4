from pathlib import Path

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

git_repo_path = Path(__file__).parent #шлях до Github
relative_path = git_repo_path / "hw_4_1.txt" #шлях до файлу в репозиторії

total, average = total_salary(relative_path)

if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
