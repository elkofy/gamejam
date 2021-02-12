import score as s
import fonts
import colors
import globals
import pygame

def show_leaderboard():
    score = globals.SCORE.score
    score = sorted((value, key) for (key,value) in score.items())
    cpt = 1
    title = fonts.pixel_font_title.render("Classement", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 50))
    if globals.LOGS:
        print(score)
    for i in score:
        if cpt > 5:
            break
        key, val = i
        img = fonts.pixel_font_24.render(val + ": " + str(key), True, colors.BLACK)
        globals.WIN.blit(img, ((globals.WIDTH / 2) - 150, (cpt*40) +150))
        cpt += 1
        