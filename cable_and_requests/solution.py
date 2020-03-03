import sys
from collections import deque, defaultdict

starts = []
ends = []
lines = []

for i, line in enumerate(sys.stdin):
    if i == 0:
        nb_cables, requests = tuple(map(int, line.split()))
    else:
        lines.append(line.rstrip('\n'))

if requests <= nb_cables:
    print(" ".join(range(1, nb_cables+1)))
else:
    available_cables = deque(maxlen=nb_cables)
    busy_cables = []
    ending_requests = []
    for n in range(nb_cables):
        available_cables.appendleft(n+1)

    program = defaultdict(list)
    for l in lines:
        program[int(l.split()[0])].append(int(l.split()[1]))

    for start in sorted(program.keys()):
        for end in program[start]:
            starts.append(start)
            ends.append(end)

    answer = ""
    for req in range(requests):
        if len(available_cables) > 0: #cables are available
            chosen_cable = available_cables.pop()
            answer = answer + " " + str(chosen_cable)
            busy_cables.append(chosen_cable)
            ending_requests.append(ends[req])
        else:
            soon_ended_request = min(ending_requests)
            if starts[req] < soon_ended_request: # next request starts before the
                print("pas possible")
                break
            else:
                chosen_cable = busy_cables.pop(ending_requests.index(soon_ended_request))
                del ending_requests[ending_requests.index(soon_ended_request)]
                answer = answer + " " + str(chosen_cable)
                ending_requests.append(ends[req])
                busy_cables.append(chosen_cable)


    print(answer)
