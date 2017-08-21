def square_of_sum(num):
    return (lambda x: x*x)(sum(range(1, num+1)))

def sum_of_squares(num):
    return sum([(lambda x: x*x)(i) for i in range(1,num+1)])

def difference(num):
    return square_of_sum(num) - sum_of_squares(num)
