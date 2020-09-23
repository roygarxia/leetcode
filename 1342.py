def numberOfSteps(num):
    num_of_steps = 0

    while num > 0:
        if num % 2 == 0 and num > 0:
            num = num // 2
            num_of_steps += 1
            print("even")
        else:
            num = num - 1
            num_of_steps += 1
            print("odd")
    
    return num_of_steps

numberOfSteps(14)