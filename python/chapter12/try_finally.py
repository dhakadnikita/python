def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return



    except Exception as e:
        print(e)


    finally:
      print('Hey I am an inside of finally')