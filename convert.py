# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

#def mph_input(mph):
    
   # return mph = float(input("Input speed in mph: "))


print('\nThis program performs speed conversions from miles per hour.\n')

#menu
opt = input('Please choose one of the following options:\n\n    [1] Miles per hour to kilometers per hour.\n\n    [2] Miles per hour to meters per second.\n\n    [3] Miles per hour to feet per second.\n\n')

#I was not thinking when I made the input line and didn't think to seperate them out into print lines and follow that with an input.... Please excuse the mess

#outputs

if opt == '1':
    mph = float(input("Input speed in mph: "))

    print("Speed in kph is", mph_to_kph(mph))

elif opt == '2':
    mph = float(input("Input speed in mph: "))

    print("Speed in m/s is", mph_to_ms(mph))
    
elif opt == '3':
    mph = float(input("Input speed in mph: "))

    print("Speed in ft/s is", mph_to_fts(mph))

else:
    mph = float(input("Input speed in mph: "))

    print('Error: Invalid option. Program will close.')