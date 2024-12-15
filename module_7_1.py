class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        """Считывает данные из файла и возвращает их в виде одной строки."""
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""  # Если файл не существует, возвращаем пустую строку.

    def add(self, *products):
        """Добавляет продукты в файл, если их там ещё нет."""
        current_products = self.get_products()
        current_names = set()  # Собираем имена текущих продуктов для проверки.

        if current_products:
            for line in current_products.split('\n'):
                name = line.split(', ')[0]  # Извлекаем имя из строки.
                current_names.add(name)

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name in current_names:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(str(product) + '\n')
                    current_names.add(product.name)  # Добавляем новое имя в набор.
# Пример работы программы
s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Вывод: Spaghetti, 3.4, Groceries

s1.add(p1, p2, p3)

print(s1.get_products())
