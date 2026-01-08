import asyncio

async def monitor():
    while True:
        print("--- [Мониторинг] Система работает нормально ---")
        await asyncio.sleep(0.5)

async def main():
    # Запускаем мониторинг в фоне и как только будет выполнена основная задача - то и в фоне прекратиться.
    task = asyncio.create_task(monitor())
    
    print("Основная логика: Начинаем загрузку данных...")
    await asyncio.sleep(2) # Имитация долгой работы
    print("Основная логика: Загрузка завершена!")
    
    # Что произойдет с задачей monitor здесь? 
    # Она просто исчезнет вместе с завершением main.

async def main2():
    # а если нам нужно чтобы фоновая задача отработала и затем что-то сделать.
    task = asyncio.create_task(monitor())
    
    await asyncio.sleep(2)
    
    # Сигнализируем задаче, что пора остановиться
    task.cancel()
    
    try:
        # Ждем, пока задача подтвердит отмену
        await task
    except asyncio.CancelledError:
        print("Главная функция: Фоновая задача успешно отменена.")


asyncio.run(main2())