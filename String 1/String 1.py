#hello_name
def hello_name(name):
  return 'Hello ' + name + '!'


#make_out_word
def make_out_word(out, word):
  front = out[:2]
  mid = word
  back = out[2:]
  return front + mid + back


#first_half
def first_half(str):
  return str[:len(str)/2]


#non_start
def non_start(a, b):
  return a[1:] + b[1:]


#make_abba
def make_abba(a, b):
  return a + b + b + a


#extra_end
def extra_end(str):
  return 3 * str[len(str) - 2:]


#without_end
def without_end(str):
    result = ""
    for i in range(len(str)):
        if i == 0 or i == len(str) - 1:
            continue
        else:
            result = result + str[i]
    return result


#make_tags
def make_tags(tag, word):
  return '<' + tag + '>' + word + '</' + tag + '>'


#first_two
def first_two(str):
  return str[:2]


#combo_string
def combo_string(a, b):
    short = ""
    large = ""
    if len(a) < len(b):
        short = a
        large = b
    else:
        short = b
        large = a
    return short + large + short




