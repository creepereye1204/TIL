import asyncio

async def my_task(delay):
    try:
        print(f"Task started, sleeping for {delay} seconds...")
        await asyncio.sleep(delay)
        print("Task completed!")
        return "Task Result"
    except asyncio.CancelledError:
        print("Task was cancelled.")
        return None

async def main():
    task = asyncio.create_task(my_task(5))
    await asyncio.sleep(2) # 2초 후 작업 취소
    print("Cancelling the task...")
    task.cancel()
    try:
        result = await task
        print(f"Task result: {result}") # 취소된 작업은 이 부분을 건너뜀
    except asyncio.CancelledError:
        print("Main program caught cancellation error.") # 이 예외를 처리할 수도 있음

if __name__ == "__main__":
    asyncio.run(main())
