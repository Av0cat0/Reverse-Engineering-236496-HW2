def to_char(val):
    return chr(val + ord('A'))

def main():
    #insert = "A" * 28
    check = ["A"] * 28
    result = ["A"] * 27 + ["J"]
    expected_result = "JLFPJPGKLJOFKLNICJLMBBCPODJA"
    for i in range(26, -1, -1):
        result[i] = to_char((ord(result[i + 1])-ord('A')) ^ (ord(expected_result[i])-ord('A')))
    result = ''.join(result)
    shiftinsert = ["A"] * 28
    for i in range(28):
        shiftinsert[i] = result[(i + 1) % 28]
    for i in range(27):
        check[i] = to_char((ord(result[i])-ord('A')) ^ (ord(shiftinsert[i])-ord('A')))
    if ''.join(check) == expected_result:
        print(result)

if __name__ == "__main__":
    main()
