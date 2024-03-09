def mark_ruler(length, mark_height):
  marks = [0] * (length + 1)
  for i in range(1, length + 1):
    if i % (2 ** mark_height) == 0:
      marks[i] = mark_height
    elif i % (2 ** (mark_height - 1)) == 0:
      marks[i] = mark_height - 1
    elif i % (2 ** (mark_height - 2)) == 0:
      marks[i] = mark_height - 2
  for i in range(1, length + 1):
    if marks[i] == 0:
      print(i)
    else:
      print(i, "-" * marks[i])

length = 32
mark_height = 3
mark_ruler(length, mark_height)