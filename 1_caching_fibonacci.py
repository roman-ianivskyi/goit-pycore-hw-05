def caching_fibonacci():

    cache = {} # Створити порожній словник cache

    def fibonacci(n):
        
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        from_cache = cache.get(n)
        if from_cache: # Якщо n у cache, повернути cache[n]
            return from_cache
        else: # Інакше обрахувати значення якого немає у кеші та додати до нього
            calculated = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = calculated
            return calculated
        
    # Повернути функцію fibonacci
    return fibonacci
    
def main():
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
    print(fib(0)) 
    print(fib(1))
    print(fib(-1))
    print(fib(100)) # 354 224 848 179 261 915 075


if __name__ == "__main__":
    main()