from maze import agent, maze,COLOR


m=maze(20,30)
m.CreateMaze(theme=COLOR.dark)

a=agent(m, footprints=True, shape='square')
m.enableArrowKey(a)
m.run()