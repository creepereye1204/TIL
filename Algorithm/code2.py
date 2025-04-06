import asyncio


async def greet(name):
    """비동기적으로 인사를 출력하는 함수"""
    await asyncio.sleep(0.1)  # 1초 동안 대기 (I/O 작업 시뮬레이션)
    print(f"Hello, {name}!")


async def print_numbers():
    """비동기적으로 숫자를 출력하는 함수"""
    for i in range(5):
        await asyncio.sleep(0.2)  # 0.2초 동안 대기
        print(f"Number: {i}")


async def main():
    """메인 함수"""
    task1 = asyncio.create_task(greet("World"))  # greet 코루틴을 태스크로 생성
    task2 = asyncio.create_task(print_numbers())  # print_numbers 코루틴을 태스크로 생성

    await asyncio.gather(task1, task2)  # 두 태스크가 모두 완료될 때까지 기다림


if __name__ == "__main__":
    asyncio.run(main())
