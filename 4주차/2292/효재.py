n = int(input())

room = 1 
max_room = 1 
while n > max_room:
    max_room += 6 * room
    room += 1

print(room)