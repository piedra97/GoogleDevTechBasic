#sleep_in
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


def diff21(n):
  if n < 21:
    return abs(n-21)
  else:
    return 2 *abs(n-21)


def near_hundred(n):
  if abs(n-100) <= 10 or abs(n-200) <= 10:
    return True
  else:
    return False


def missing_char(str, n):
    front = str[:n]
    back = str[n + 1:]
    return front + back


def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile or (not a_smile and not b_smile):
    return True
  else:
    return False


def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False



def pos_neg(a, b, negative):
  if ((a > 0 and b < 0) or (a < 0 and b > 0)) and not negative:
    return True
  elif (a < 0 and b < 0) and negative:
    return True
  else:
    return False


def front_back(str):
    if len(str) <= 1:
        return str

    else:
        result = ""
        for i in range(len(str)):
            if i == 0:
                result = result + str[len(str) - 1]
            elif i == len(str) - 1:
                result = result + str[0]
            else:
                result = result + str[i]
    return result


def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  else:
    return a+b


def makes10(a, b):
  if (a == 10 or b == 10) or a + b == 10:
    return True
  else:
    return False


def not_string(str):
  if str[0:3] == 'not':
    return str
  else:
    return 'not ' + str


def front3(str):
  return 3*str[0:3]



