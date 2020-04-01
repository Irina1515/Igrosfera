import os

if __name__ == "__main__":

    d = "./data"
    for filename in os.listdir(d):
        print('open ' + filename)
        with open(d + '/' + filename) as f:
            for line in f:
                    print(line)
    f.close()
