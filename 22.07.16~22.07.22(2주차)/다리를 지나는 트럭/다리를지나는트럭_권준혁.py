from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    bridge_sum = 0
    while(bridge):
        answer += 1
        bridge_sum -= bridge.pop()
        if truck_weights:
            if bridge_sum + truck_weights[0] <= weight:
                bridge.appendleft(truck_weights.popleft())
                bridge_sum += bridge[0]
            else:
                if truck_weights:
                    bridge.appendleft(0)
    return answer
