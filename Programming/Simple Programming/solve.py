with open("data.dat", "r") as file: 
  lines = file.readlines()

  count = 0

  for line in lines: 
    noOf0 = 0
    noOf1 = 0

    for bit in line[:-1]:
      if int(bit) == 1: 
        noOf1 += 1
      else:
        noOf0 += 1

    if noOf0 % 3 == 0 or noOf1 % 2 == 0:
      count += 1

  print(count)