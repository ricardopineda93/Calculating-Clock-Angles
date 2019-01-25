def hr_min_input():
    while True:
        try:
            hour = int(input('Enter hour between 1 & 12: '))
            minute = int(input('Enter a minute between 0 & 59: '))
        except:
            print('Invalid input, please use only positive integers.')
            continue
        else:
            if (hour <= 0) or (minute < 0):
                print('Hour or minute inputs cannot be negative.')
                continue
            elif (hour > 12) or (minute > 59):
                print('Hour input must be integer between 1 - 12, minute input must be integer between 0 - 59.')
                continue
            else:
                return hour, minute

def clock_hand_angles(hour, minute):

    hr_hand_p = hour * (360/12)
    min_hand_p = minute * (360/60)
    max_angle = 180

    if hr_hand_p == min_hand_p:
        return 0
    elif hr_hand_p > min_hand_p:
        return hr_hand_p - min_hand_p
    elif hr_hand_p < min_hand_p:
        if (min_hand_p - hr_hand_p) > max_angle:
            return 360 - (min_hand_p - hr_hand_p)
        else:
            return min_hand_p - hr_hand_p

def calc_clock_angle():
    result = clock_hand_angles(*hr_min_input())
    print(result)

calc_clock_angle()


