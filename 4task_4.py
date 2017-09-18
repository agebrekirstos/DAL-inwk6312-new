def multiple_of_5():
    number_list = range (1,100)
    multiple = list(filter(lambda x:x%5==0, number_list))
    print(multiple)

multiple_of_5()
