def palavra(n):
    return len(n)
def main():
    n = str(input('Digite uma palavra: '))
    print(f'{palavra(n)}')
if __name__ == "__main__":
    main()