import pygame
import random
import sys
import pg8000
import pickle

pygame.init()

TILE_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30
SCREEN = pygame.display.set_mode((GRID_WIDTH * TILE_SIZE, GRID_HEIGHT * TILE_SIZE))
pygame.display.set_caption("Snake Game with Locations and Save")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
font = pygame.font.SysFont(None, 36)

DB_NAME = "snake_db"
DB_USER = "postgres"
DB_PASSWORD = "123"
DB_HOST = "localhost"
DB_PORT = 5432

# generate static obstacles, avoid spawn area
def get_walls_for_location(loc):
    if loc <= 1:
        return []
    random.seed(loc)
    obstacles = []
    tries = 0
    center = (GRID_WIDTH//2, GRID_HEIGHT//2)
    # define spawn zone around center (3x3) to keep free
    spawn_zone = {center, (center[0]-2, center[1]), (center[0]+2, center[1]), (center[0], center[1]-2), (center[0], center[1]+2)}
    while len(obstacles) < loc * 3 and tries < loc * 10:
        size = random.randint(1, 3)
        orientation = 'h' if tries % 2 == 0 else 'v'
        if orientation == 'h':
            y = random.randint(1, GRID_HEIGHT - 2)
            x_start = random.randint(0, GRID_WIDTH - size)
            coords = [(x_start + i, y) for i in range(size)]
        else:
            x = random.randint(1, GRID_WIDTH - 2)
            y_start = random.randint(0, GRID_HEIGHT - size)
            coords = [(x, y_start + i) for i in range(size)]
        if any(c in obstacles or c in spawn_zone for c in coords):
            tries += 1
            continue
        obstacles.extend(coords)
        tries += 1
    return obstacles

# input username
def get_username():
    text, clock = "", pygame.time.Clock()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN and text:
                    return text
                elif e.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif len(text) < 20:
                    text += e.unicode
        SCREEN.fill(BLACK)
        SCREEN.blit(font.render("Enter username and press ENTER", True, WHITE),(10, GRID_HEIGHT*TILE_SIZE//2-30))
        SCREEN.blit(font.render(text, True, WHITE),(10, GRID_HEIGHT*TILE_SIZE//2+10))
        pygame.display.flip(); clock.tick(30)

# DB helpers
def ensure_database(db, user, pw, host, port):
    conn = pg8000.connect(user=user,password=pw,database="postgres",host=host,port=port)
    conn.autocommit=True; cur=conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname=%s",(db,))
    if not cur.fetchone(): cur.execute(f"CREATE DATABASE {db}")
    cur.close(); conn.close()

def db_connect():
    conn=pg8000.connect(user=DB_USER,password=DB_PASSWORD,database=DB_NAME,host=DB_HOST,port=DB_PORT)
    return conn, conn.cursor()

def ensure_tables():
    conn,cur=db_connect()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,username VARCHAR(50) UNIQUE NOT NULL);")
    cur.execute("""CREATE TABLE IF NOT EXISTS user_scores(id SERIAL PRIMARY KEY,user_id INTEGER REFERENCES users(id),location INT NOT NULL,state BYTEA,saved_at TIMESTAMP NOT NULL DEFAULT NOW());""")
    conn.commit(); cur.close(); conn.close()

# Game over UI
def game_over_screen(score, level, location):
    btn_retry=pygame.Rect(50,GRID_HEIGHT*TILE_SIZE//2,100,40)
    btn_exit=pygame.Rect(200,GRID_HEIGHT*TILE_SIZE//2,100,40)
    clock=pygame.time.Clock()
    while True:
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()
            if e.type==pygame.MOUSEBUTTONDOWN:
                if btn_retry.collidepoint(e.pos): return True
                if btn_exit.collidepoint(e.pos): return False
        SCREEN.fill(BLACK)
        SCREEN.blit(font.render("Game Over",True,RED),(SCREEN.get_width()//2-80,100))
        SCREEN.blit(font.render(f"Score: {score}",True,WHITE),(SCREEN.get_width()//2-80,150))
        SCREEN.blit(font.render(f"Level: {level}",True,WHITE),(SCREEN.get_width()//2-80,190))
        SCREEN.blit(font.render(f"Location: {location}",True,WHITE),(SCREEN.get_width()//2-80,230))
        pygame.draw.rect(SCREEN,GREEN,btn_retry);pygame.draw.rect(SCREEN,RED,btn_exit)
        SCREEN.blit(font.render("RETRY",True,BLACK),(btn_retry.x+10,btn_retry.y+5))
        SCREEN.blit(font.render("EXIT",True,BLACK),(btn_exit.x+20,btn_exit.y+5))
        pygame.display.flip(); clock.tick(30)

# Main game
def main():
    ensure_database(DB_NAME,DB_USER,DB_PASSWORD,DB_HOST,DB_PORT); ensure_tables()
    username=get_username()
    conn,cur=db_connect(); cur.execute("SELECT id FROM users WHERE username=%s",(username,)); row=cur.fetchone()
    if row: user_id=row[0]
    else: cur.execute("INSERT INTO users(username) VALUES(%s) RETURNING id",(username,)); user_id=cur.fetchone()[0]; conn.commit()
    cur.close(); conn.close()

    while True:
        conn,cur=db_connect(); cur.execute("SELECT location,state FROM user_scores WHERE user_id=%s ORDER BY saved_at DESC LIMIT 1",(user_id,)); last=cur.fetchone(); cur.close(); conn.close()
        if last: location,st=last; state=pickle.loads(st) if st else None
        else: location,state=1,None

        snake = state['snake'] if state else [(GRID_WIDTH//2, GRID_HEIGHT//2)]
        # ensure new spawn at exact center
        if not state:
            snake = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
        direction=state['direction'] if state else (1,0)
        growth=state['growth'] if state else 0
        food=state['food'] if state else None
        score,level=0,1;clock=pygame.time.Clock();paused=False

        def get_random_food():
            walls=get_walls_for_location(location)
            while True:
                x=random.randint(0,GRID_WIDTH-1);y=random.randint(0,GRID_HEIGHT-1)
                if (x,y) not in snake and (x,y) not in walls: return {'position':(x,y),'weight':random.randint(1,3),'spawn_time':pygame.time.get_ticks()}

        if not food or food['position'] in snake or food['position'] in get_walls_for_location(location):
            food = get_random_food()

        running=True
        while running:
            walls=get_walls_for_location(location);speed=10+(level-1)*2;dir_changed=False
            for e in pygame.event.get():
                if e.type==pygame.QUIT: pygame.quit();sys.exit()
                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_p: paused=not paused
                    elif e.key==pygame.K_l and not paused: location+=1;score,level=0,1;snake=[(GRID_WIDTH//2,GRID_HEIGHT//2)];direction=(1,0);growth=0;food=get_random_food()
                    elif not paused and not dir_changed:
                        if e.key==pygame.K_UP and direction!=(0,1): direction=(0,-1);dir_changed=True
                        elif e.key==pygame.K_DOWN and direction!=(0,-1): direction=(0,1);dir_changed=True
                        elif e.key==pygame.K_LEFT and direction!=(1,0): direction=(-1,0);dir_changed=True
                        elif e.key==pygame.K_RIGHT and direction!=(-1,0): direction=(1,0);dir_changed=True
            if paused: continue
            hx,hy=snake[0];dx,dy=direction;nh=(hx+dx,hy+dy)
            if nh in walls or not(0<=nh[0]<GRID_WIDTH and 0<=nh[1]<GRID_HEIGHT) or nh in snake: running=False
            else:
                snake.insert(0,nh)
                if nh==food['position']: score+=food['weight'];growth+=food['weight'];food=get_random_food()
                else: (growth>0 and (growth:=growth-1)) or snake.pop()
                if pygame.time.get_ticks()-food['spawn_time']>5000: food=get_random_food()
                nl=score//5+1
                if nl!=level:
                    level=nl
                    if level>5: level,score=1,0;location+=1
            SCREEN.fill(BLACK)
            SCREEN.blit(font.render(f"Location:{location}",True,WHITE),(10,10))
            for wx,wy in walls:pygame.draw.rect(SCREEN,WHITE,(wx*TILE_SIZE,wy*TILE_SIZE,TILE_SIZE,TILE_SIZE))
            for x,y in snake:pygame.draw.rect(SCREEN,GREEN,(x*TILE_SIZE,y*TILE_SIZE,TILE_SIZE,TILE_SIZE))
            fx,fy=food['position'];pygame.draw.rect(SCREEN,RED,(fx*TILE_SIZE,fy*TILE_SIZE,TILE_SIZE,TILE_SIZE))
            SCREEN.blit(font.render(str(food['weight']),True,WHITE),(fx*TILE_SIZE+TILE_SIZE//2-10,fy*TILE_SIZE+TILE_SIZE//2-18))
            SCREEN.blit(font.render(f"Score:{score} Level:{level}",True,WHITE),(10,40))
            pygame.display.flip();clock.tick(speed)

                # save after death (do not save state)
        conn, cur = db_connect()
        cur.execute("INSERT INTO user_scores(user_id, location) VALUES(%s, %s)", (user_id, location))
        conn.commit(); cur.close(); conn.close()
        if not game_over_screen(score,level,location):pygame.quit();sys.exit()

if __name__=="__main__":main()
