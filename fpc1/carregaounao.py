def soma_mofiz(number1, number2):
  print(number1^number2)
  
while True:
    try:
        number1, number2 = map(int, input().split())
    except EOFError:
        break
    soma_mofiz(number1, number2)