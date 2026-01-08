import asyncio

# Способ №1: Прямое ожидание (await task)

async def heavy_computation():
    print("Фоновая задача: Начинаю расчеты...")
    await asyncio.sleep(3)  # Имитация долгой работы
    return 42 # Возвращаем результат

async def main():
    # 1. Запускаем задачу в фоне
    task = asyncio.create_task(heavy_computation())
    
    print("Основной поток: Пока задача считается, я делаю что-то другое...")
    await asyncio.sleep(1)
    print("Основной поток: Все еще жду...")

    # 2. Теперь нам КРИТИЧЕСКИ нужен результат. 
    # В этой точке мы приостановимся, пока задача не доделается.
    result = await task 
    
    print(f"Основной поток: Получен результат из фона -> {result}")

asyncio.run(main())


# Способ №2: Обратный вызов (Callback)
def handle_result(task):
    """Функция-обработчик (callback)"""
    try:
        # Пытаемся забрать результат из завершенной задачи
        result = task.result()
        print(f"Callback: Данные получены и обработаны: {result}")
    except Exception as e:
        print(f"Callback: Упс, в задаче произошла ошибка: {e}")

async def fetch_data():
    await asyncio.sleep(2)
    return {"status": "ok", "data": [1, 2, 3]}

async def main2():
    print("Main: Запускаем задачу...")
    task = asyncio.create_task(fetch_data())
    
    # Регистрируем наш callback
    task.add_done_callback(handle_result)
    
    print("Main: Делаем другие дела, не дожидаясь задачу...")
    await asyncio.sleep(3)
    print("Main: Завершаем работу.")

asyncio.run(main2())