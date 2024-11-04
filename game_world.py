#world = [] # 빈 월드 생성, 단일 계층 구조

# world[0] : 백그라운드 객체들
# world[1] : 포어그라운드 객체들

world = [[], [], []]

def add_object(o, depth):
    world[depth].append(o)


def render():
    for layer in world:
        for o in layer:
            o.draw()


def update():
    for layer in world:
        for o in layer:
            o.update()


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return # 지우는 미션 달성.
    print('에러 : 존재하지 않는 객체를 지움')