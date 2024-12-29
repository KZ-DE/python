import asyncio
import time


async def async_operation_1():
    print("Mulai async operation 1")
    await asyncio.sleep(10)

    print("Selesai async operation 1", time.time() - start, "detik")
    return 1


async def async_operation_2():
    print("Mulai async operation 2")
    await asyncio.sleep(2)
    print("Selesai async operation 2", time.time() - start, "detik")
    return 2


async def async_operation_3():
    print("Mulai async operation 3")
    await asyncio.sleep(12)
    print("Selesai async operation 3", time.time() - start, "detik")
    return 3


async def main():
    global start
    name = input("masukan input ke 2 : ")
    start = time.time()
    tasks = [async_operation_1(), async_operation_2(), async_operation_3()]
    results = await asyncio.gather(*tasks)
    print("Hasil async operations:", results)
    akhir = time.time() - start
    print(akhir, "detik")

asyncio.run(main())
