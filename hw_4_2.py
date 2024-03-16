def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_info = line.strip().split(',') # Розділяємо рядок на частини по комі
                cat_dict = {"id": cat_info[0], "name": cat_info[1], "age": cat_info[2]} # Створюємо словник з інформацією про кота та додаємо його до списку
                cats_list.append(cat_dict)
        
        return cats_list
        
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

# Приклад використання
cats_info = get_cats_info("D:\git_projects\hw_module_4\hw_4_2.txt")
if cats_info is not None:
    print(cats_info)
