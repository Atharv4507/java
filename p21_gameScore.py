def game():
    return 400
score = game()
with open("S_hiscore.txt") as f:
    hiscore = f.read()
if hiscore == '':
    with open("S_hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiscore)<score:
    with open("S_hiscore.txt", "w") as f:
        f.write(str(score))
