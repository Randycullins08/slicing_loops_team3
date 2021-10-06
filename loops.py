from random import randint

def list_generator():
  my_empty_list = []

  for i in range(50, 81):
    if len(my_empty_list) >= 12:
      break
    else:
      num = randint(50, 81)
      my_empty_list.append(num)

  my_empty_list.sort(reverse=True)

  return my_empty_list


def sixty_six(lst):
  sixty_six = 0

  for num in lst:
    if num == 66:
      sixty_six = num
      print(f'Found {sixty_six}')
    else:
      continue
  return lst

def high_low(lst):
  highest_num = lst[0]
  lowest_num = lst[-1]

  for num in lst:
    print(num, end=" ")
  print(f"\nHighest number: {highest_num} Lowest number: {lowest_num}")


def sliced_list(lst):
  sliced = lst[4:9]

  return sliced

def sliced_total(lst):
  total = 0
  for s_num in lst:
    total += s_num
  print(f"\nTotal of the sliced values: {total}\n")

def while_sliced(lst):
  sliced_original = lst
  count = len(lst)
  sixty_six(lst)

  while count > 0:
    for num in lst:
      print(num, end="    ")
      count -= 1

  return sliced_original

sliced_total(while_sliced(sliced_list(list_generator())))