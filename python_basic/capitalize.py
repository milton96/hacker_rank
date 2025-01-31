def solve(s: str):
    words = s.split(" ")
    res = ""
    for word in words:
        res += word.capitalize() + " "

    return res

if __name__ == '__main__':
    s = "chris alan"
    result = solve(s)
    print(result)