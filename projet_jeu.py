import pyxel as px

px.init(160, 120)

x: int = 10
y:int = 55
def update():
    global x,y
    if px.btnp(px.KEY_Q):
        px.quit()
    if px.btnp(px.KEY_DOWN)and y+30 < 100:
        y = y + 30
    if px.btnp(px.KEY_UP) and y-30 > 20 :
       y = y - 30
    

def draw():
    px.cls(0)
    px.rect(0, 15,160, 90, 13) #route
    px.line(0,45 ,160,45,9) 
    px.line(0,75 ,160,75,9)
    px.rect(x, y, 15, 10, 7) #voiture
    px.rect(x+5, y-5,5, 20, 7) #voiture
 


px.run(update, draw)