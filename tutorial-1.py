import numpy as np
import matplotlib.pyplot as plt

def random1():
    result = np.random.random(1000)

    return result

def random2():
    result = np.random.random(1000)
    result *= 10
    result += 5

    return result

def random3():
    result = np.random.normal(5, 2, 1000)
    newresult = []
    for result_value in result:
        if(result_value <= 10 and result_value >= 0):
            newresult.append(result_value)

    return newresult

def piCalculate():
    results = []
    sum = 0
    run_times = 1000
    k = 0
    for k in range(0, run_times): 
        num_of_points = 1000
        
        x_axis = np.random.random(num_of_points)
        x_axis -= 1/2
        y_axis = np.random.random(num_of_points)
        y_axis -= 1/2

        accepted_points = 0
        i = 0
        for i in range(0, num_of_points):
            if(x_axis[i] ** 2 + y_axis[i] ** 2 <= 1/4):
                accepted_points += 1
            i += 1

        results.append(4 * accepted_points / num_of_points)
        sum += 4 * accepted_points / num_of_points
        k += 1

    print(sum / run_times), print(np.std(results))
    return results

def ranmdomExp():
    result = np.random.exponential(1, 1000)

    newresult = []
    for result_value in result:
        if(result_value <= 5 and result_value >= 0):
            newresult.append(result_value)

    print(len(newresult)/len(result))
    plt.hist(result)
    plt.show()
    return newresult

def showGraph(result = []):
    plt.title("Random Numbers")
    plt.xlabel("Values")
    plt.ylabel("Counts")
    plt.hist(result)
    plt.show()

showGraph(ranmdomExp())