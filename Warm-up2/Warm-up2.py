#string_times
def string_times(str, n):
  return n*str

#front_times
def front_times(str, n):
  return n*str[:3]

#string_bits
def string_bits(str):
  return str[::2]

#array_count9
def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count+= 1
  return count