import ecra

def main():
    x= 0
    while x < 1000:
        x=1
        ecra.write_to_display("123456789" + str(x))
        x= x +1

if __name__ == "__main__":
    main()
