from sys import argv, exit

def main():
    n, m = [int(x) for x in input("N, M ").split()]
    print("---------")

    if ((n < 1) or (m < 1)):
        print("invalid input")
        exit(1)
        
    links = []
    for i in range(m):
        a, b = [int(x) for x in input().split()]
        if ((a > n) or (b > n)):
            print("invalid input")
            exit(1)
        link = [a, b]
        links.append(link)
        
    circles = []
    for i in range(n):
        circles.append("g")
        
    for i in range(n):
        color(i, m, circles, links, True)
    
    print("---------")
    for i in range(m):
        if (circles[links[i][0] - 1] == circles[links[i][1] - 1]):
            print("Impossible")
            exit(0)

    for i in range(n):
        print(str(i + 1) + " " + circles[i])

def color(a, b, circles, links, black):
    if (circles[a] != "g"):
        return
    elif black:
        circles[a] = "b"
    else:
        circles[a] = "r"
    black = not black
    for i in range(b):
        if (links[i][0] == (a + 1)):
            color(links[i][1] - 1, b, circles, links, black)
        elif (links[i][1] == (a + 1)):
            color(links[i][0] - 1, b, circles, links, black)
    return

main()