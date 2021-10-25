from backpack_review import comprehensive_review
from random import randint
import time

def main():
    n = 25
    w = [randint(1, 10) for _ in range(n)]
    W = 9
    p = [randint(1, 10) for _ in range(n)]
    start = time.time()
    comprehensive_review(w, W, p)
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()
