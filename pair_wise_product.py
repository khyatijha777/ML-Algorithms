#python3
def max_pairwise_product(n):
    max1 = max(n)
    n.remove(max1)
    max2 = max(n)
    return max1*max2



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split(" ")]
    print(max_pairwise_product(input_numbers))
