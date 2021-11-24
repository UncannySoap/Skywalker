import sys

numCheckpoints = int(input())
checkpoints = []
for i in range(numCheckpoints):
    checkpoint = [int(j) for j in input().split()]
    checkpoints.append(checkpoint)

while True:
    checkpoint_index, x, y, vx, vy, angle = [int(i) for i in input().split()]
    thrust = 100
    print(str(checkpoints[checkpoint_index][0]) + " " + str(checkpoints[checkpoint_index][1]) + " " + str(thrust) + "message")