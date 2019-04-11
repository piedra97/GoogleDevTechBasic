#double_char
def double_char(str):
  result = ""
  for letter in str:
    result += 2*letter
  return result

#count_hi
def count_hi(str):
  count = 0
  for i in range(len(str) -1):
    if str[i:i+2] == 'hi':
      count += 1
  return count

#cat_dog
def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str)):
        if str[i:i + 3] == 'dog':
            count_dog += 1
        elif str[i:i + 3] == 'cat':
            count_cat += 1

    return count_cat == count_dog

#count_code
def count_code(str):
  count = 0
  for i in range(0 , len(str) - 3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count

#end_other
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  #return (b.endswith(a) or a.endswith(b))
  return a[-(len(b)):] == b or a == b[-(len(a)):]

#xyz_there
def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
    if str[0:3] == 'xyz':
      return True
  return False

