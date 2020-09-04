from functools import reduce


class digitConvert:

    def digitConvert(self, num):

        digitMaps = {
            '2': ['A', 'B', 'C'],
            '3': ['D', 'E', 'F'],
            '4': ['G', 'H', 'I'],
            '5': ['J', 'K', 'L'],
            '6': ['M', 'N', 'O'],
            '7': ['P', 'Q', 'R', 'S'],
            '8': ['T', 'U', 'V'],
            '9': ['W', 'X', 'Y', 'Z']
        }
        digits = str(num)
        if len(digits) == 1:
            if digits[0] in digitMaps:
                print(digitMaps[digits[0]])
            elif digits[0] not in digitMaps:
                print("input value out of range")

        elif len(digits) == 2:
            digitMapList = []
            for i in digits:
                if i not in digitMaps:
                    print("input value out of range")
                    break
                else:
                    digitMapList.append(digitMaps[i])

            if digitMapList !=[]:
                code = ''
                fn = lambda x, code='': reduce(lambda x, y: [str(i) + code + str(j) for i in x for j in y], x)
                print(fn(digitMapList, code))

        else:
            print("input value out of range")

        return


if __name__ == '__main__':

    test = digitConvert()
    while True:
        num = input("please input num range from 0 to 99 to be converted:  ")
        if '0' in num or '1' in num:
            print("no mapping letters for the input value")

        else:
            test.digitConvert(num)