import asyncio


# // Run functions asynchronously
# // Async functions are non-io blocking

# // First async function
async def my_function(num: int):
  print(num)

  # // You can only use the await keyword if already inside an async function!
  await my_function_2(num)


# // Second async function
async def my_function_2(num: int):
  print(num + 1)


# // Use asyncio to call the async function
asyncio.run(my_function(1))

# // You can only use asyncio.run on ONE function
# // e.g calling asyncio.run(my_function(1)) twice:
# //
# // asyncio.run(my_function(1))
# // asyncio.run(my_function(1))
# //
# // Is not a good practice!
