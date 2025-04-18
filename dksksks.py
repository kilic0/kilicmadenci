a = random.randint(1,3)

b = input("Taş / Kağıt / Makas")

if a == 1:
  c = ("Taş")
if a == 2:
  c = ("Kağıt")
if a == 3:
  c = ("Makas")
 
if b == ("Taş"):
  if c == ("Taş"):
    print(" Berabere", "Bot:", c)
  if c == ("Kağıt"):
    print(" Kaybettin", "Bot:", c)
  if c == ("Makas"):
    print(" Kazandın", "Bot:", c)
   
if b == ("Kağıt"):
  if c == ("Taş"):
    print(" Kazandın", "Bot:", c)
  if c == ("Kağıt"):
    print(" Berabere", "Bot:", c)
  if c == ("Makas"):
    print(" Kaybettin", "Bot:", c)

if b == ("Makas"):
  if c == ("Taş"):
    print(" Kaybettin", "Bot:", c)
  if c == ("Kağıt"):
    print(" Kazandın", "Bot:", c)
  if c == ("Makas"):
    print(" Berabere", "Bot:", c)
