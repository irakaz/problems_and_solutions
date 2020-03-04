stones = []
powders = []
stones_nb, powders_nb, max_weight = tuple(map(int, input().split()))
for _ in range(stones_nb):
    stones.append(tuple(map(int, input().split())))
for _ in range(powders_nb):
    powders.append(tuple(map(int, input().split())))

def calculate_max_value(rates, stones, powders, rates_it, leftovers, available_weight = max_weight):
    value_per_available_weight = 0
    while available_weight > 0:
        # take the highest rate
        try:
            highest_rate, i = next(rates_it)
        except StopIteration:
            break
        if i < len(stones): # A stone takes the highest rate
            value = stones[i][0]
            weight = stones[i][1]
            if weight > available_weight:
                leftovers.append((highest_rate, i))
                continue
            else:
                value_per_available_weight = value_per_available_weight + value
                available_weight = available_weight - weight
        else:# A powder takes the highest rate
            weight = powders[i-len(stones)][1]
            value = powders[i-len(stones)][0]
            if weight > available_weight:
                value_per_available_weight = value_per_available_weight + value*available_weight
                available_weight = 0
                #lamp_content.append(())
            else:
                value_per_available_weight = value_per_available_weight + value*weight
                available_weight = available_weight - weight

    return (value_per_available_weight, available_weight)

def optimize_content(stones, powders, max_weight):

    # Calculate the value/weight to determine the highest rate
    rates = [ (t[0]/t[1],i) for i,t in enumerate(stones) ]
    # TODO : when rates are equal?
    rates.extend([ (t[0],i+len(stones)) for i,t in enumerate(powders) ])
    rates = sorted(rates, reverse = True)

    total_value = 0
    committed_weight = 0
    available_weight = max_weight
    still_can_be_optimized = True
    
    while still_can_be_optimized:
        it = iter(rates)
        leftovers = []
        value_per_used_weight, remaining_weight = calculate_max_value(rates, stones, powders, it, leftovers, available_weight)
        if remaining_weight > 0: # There is still some spare space in our lamp
            try:
                if leftovers:
                    rate_tuple = leftovers[0]
                else:
                    rate_tuple = next(it)
                rate, i = rate_tuple # this rate is surely related to a stone
                if value_per_used_weight/available_weight < rate and stones[i][1] <= max_weight-committed_weight: # This stone has higher rate than all what we have put in the lamp, so we should put it first
                    available_weight = available_weight - stones[i][1]
                    committed_weight = committed_weight + stones[i][1]
                    total_value = total_value + stones[i][0]
                    del stones[i]
                else:
                    total_value = total_value + value_per_used_weight
                    still_can_be_optimized = False
            except StopIteration:
                total_value = total_value + value_per_used_weight
                still_can_be_optimized = False
        else:
            total_value = total_value + value_per_used_weight
            still_can_be_optimized = False
    return total_value

print(optimize_content(stones, powders, max_weight))