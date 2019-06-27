import numpy as np
import pyautogui as pag
import keyboard

# TODO:
gameregion = (520, 260, 415, 695)

# -----
start = False
columndistance = int(gameregion[2]/4)
offset = int(columndistance/2)

if __name__ == '__main__':
    while True:
        if keyboard.is_pressed('q'):
            start = True
        if start:
            while True:
                if (gameregion[0] < pag.position()[0] < gameregion[0]+gameregion[2]) and (gameregion[1] < pag.position()[1] < gameregion[1]+gameregion[3]):
                    img = pag.screenshot(region=gameregion)
                    img = np.asarray(img)
                    for i in range(4):
                        firstcol = [np.sum(x) for x in img[:, offset + i*columndistance]]
                        clickhere = np.where(np.array(firstcol) < 100)  # 100 = sum of rgb (find dark pixel)
                        if clickhere[0].shape[0] > 0:
                            pag.click(x=gameregion[0] + offset + i*columndistance, y=gameregion[1] + (clickhere[0])[-1])
