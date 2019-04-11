#cigar_party
def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >= 40:
    return True
  elif cigars >= 40 and cigars <= 60:
    return True
  else:
    return False

#date_fashion
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0

  elif you >= 8 or date >= 8:
    return 2

  else:
    return 1

#squirrel_play
def squirrel_play(temp, is_summer):
  if is_summer:
    return (60 <= temp <= 100)
  else:
    return (60 <= temp <= 90)

#caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
  if speed <= 60:
    return 0
  elif  61  <=  speed <= 80:
    return 1
  else:
    return 2

#sorta_sum
def sorta_sum(a, b):
  sum = a +b
  return 20 if 10 <= sum <= 19 else sum

#alarm_clock
def alarm_clock(day, vacation):
  if vacation:
    return '10:00' if 1 <= day <= 5 else 'off'

  else:
    return '7:00' if 1 <= day <= 5 else '10:00'

#love6
def love6(a, b):
  return a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6

#in1to10
def in1to10(n, outside_mode):
  if outside_mode:
    return (n <= 1 or n >= 10)
  else:
    return (1 <= n <= 10)

#near_ten
def near_ten(num):
  mod = num % 10
  if mod == 0 or mod == 1 or mod == 2 or mod == 8 or mod  == 9:
    return True
  else:
    return False