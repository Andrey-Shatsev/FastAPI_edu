import asyncio
import time

#Пример плохой функции - где происходит блокировка событийного цикла: 

async def blocking_task():
    print("Я заблокирую всё на 5 секунд...")
    # ОШИБКА: time.sleep — это синхронная остановка всего потока
    time.sleep(5) 
    print("Я закончил, теперь другие могут работать.")

async def simple_job():
    while True:
        print("--- Работаю... ---")
        await asyncio.sleep(1)

async def main():
    # Запускаем фоновую полезную работу
    asyncio.create_task(simple_job())
    # Запускаем блокирующую задачу
    await blocking_task()

asyncio.run(main())