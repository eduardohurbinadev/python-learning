from datetime import datetime

wait_until = datetime.now().second + 1

while datetime.now().second != wait_until:
    pass

print(f'We are at {wait_until} seconds!')