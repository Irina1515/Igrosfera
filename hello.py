import sys
import os

if __name__ == "__main__":
    st = 'error'
    if len(sys.argv) == 2:
        st = sys.argv[1]
    if len(sys.argv) > 2:
        print("Incorrect number of params!")
        sys.exit(1)
    data = []
    d = "./data"
    for filename in os.listdir(d):
        print('open ' + filename)
        with open(d + '/' + filename) as f:
            for line in f:
                if line.find(st) != -1:
                    data.append(line)
                    print(line)
    f = open('output.txt', 'w')
    for d in data:
        f.write(d)
    f.close()
