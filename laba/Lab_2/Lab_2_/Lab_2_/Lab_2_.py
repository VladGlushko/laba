a = input("Виберіть операцію(1 / 2): ")
if a == "1":
    l = []
    x = input("")
    for i in range(len(x)):
      if x[i] not in l and x[i] not in " ,.":
          l.append(x[i])
          l.append(x.count(x[i]))
    print(l)
if a == "2":
    l = []
    d = input().split(" ")
    for i in d:
        if i not in l and len(i) >= 3:
            l.append(i)
    print(sorted(l))