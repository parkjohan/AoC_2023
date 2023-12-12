# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

with open("/Users/johanpark/Desktop/AoC_2023/Day1/input.txt", "r") as file:

    num_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    calibration_list = []
    calibration_total = 0
    
    # split input into an a list
    input_list = file.read().splitlines()

    # read through the list of lines and get the calibration numbers
    for i in input_list:
        calibration = ""
        for j in range(0, len(i)):
            # # if an index in the line is an integer value, extract it
            # if i[j] in num_values:
            #     # if there are already 2 values in array, pop the last one and replace with new one
            #     if len(calibration) == 2:
            #         calibration.pop()
            #     calibration.append(i[j])

            # go from beginning and find first element
            if i[j] in num_values:
                calibration += i[j]
                break
        for k in range(len(i)-1, -1, -1):
            # go from the end and find first element
            if i[k] in num_values:
                calibration += i[k]
                break
        
        calibration_list.append(calibration)
        calibration = ""

    print(calibration_list)

    # add up the calibration values
    for i in calibration_list:
        calibration_total += int(i)

    print(calibration_total)
            
    # dont forget to close the file after
    file.close()