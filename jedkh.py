import string, numpy as np, random, time

input_string = input("So what do you have to say?\n\n")
assert 0 < len(input_string) < 1000, "Don't take the piss"

baselines = [[74, 69, 84, 32, 70, 85, 69, 76, 32, 67, 65, 78, 39, 84, 32, 77, 69, 76, 84, 32, 83, 84, 69, 69, 76, 32, 66, 69, 65, 77, 83, 46],
             [74,69,70,70,82,69,89,32,69,80,83,84,69,73,78,32,68,73,68,78,39,84,32,75,73,76,76,32,72,73,77,83,69,76,70,46]]
baseline = random.choice(baselines)
baseline = "".join([chr(i) for i in baseline])
mask = np.zeros(shape=(len(baseline),))
possible = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'. "

count = 0
for i, j in zip(input_string, baseline):
    if i==j:
        mask[count] = 1
    count+=1
        
done = False
while not done:
    if len(input_string) > len(baseline) and random.random() >= 0.97:
        temp = list(input_string)
        temp.pop()
        input_string = "".join(temp)
    elif len(input_string) < len(baseline) and random.random() >= 0.97:
        input_string += random.choice(possible)
    
    #actually makes changes to string
    all_to_change = [i for i,j in enumerate(mask) if j==0 and i < len(input_string)]
    if len(all_to_change) != 0:
        to_change = random.choice(all_to_change)
        temp = list(input_string)
        temp[to_change] = random.choice(possible)
        input_string = "".join(temp)
    
    #updates mask
    count = 0
    for i, j in zip(input_string, baseline):
        if i==j:
            mask[count] = 1
        count+=1
        
    print(input_string)
    time.sleep(0.005)
    
    if np.all(mask) and len(mask)==len(input_string):
        done = True