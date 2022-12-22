from googlesheets.sheets import get_values

def main():
    values = get_values()
    print(values)
    return

if __name__ == '__main__':
    main()