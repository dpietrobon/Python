''' Genetic Program and Algorithm Test Design '''
''' 2D Implementation and GUI '''

from tkinter import *
import numpy as np
import random
import time as tm

''' Global Variables and Initializations '''

global canvas_update_speed
global left_mouse_down
global loop_active
global plant_list
global snake_string
global time
global x_step
global y_step
global snake_display

canvas_update_speed = 100
left_mouse_down = False
loop_active = False
plant_list = []
snake_display = False
time = 0


class Plant:
    def __init__(self):
        self.age = 0
        self.x = random.randint(1,canvas.winfo_width())
        self.y = random.randint(1,canvas.winfo_height())
        self.image = canvas.create_rectangle(self.x-1,self.y-1,self.x+1,self.y+1,
                                             fill='green',tag='plant')

    def grow(self):
        '''Grows outward from initial position ... '''
        if self.age < 50:
            x1 = self.x - int(self.age/3)
            y1 = self.y - int(self.age/3)
            x2 = self.x + int(self.age/3)
            y2 = self.y + int(self.age/3)
            canvas.coords(self.image,x1,y1,x2,y2)
            canvas.update()
            

''' SNAKE CLASS: Models Snake Object on Rectangular Grid '''

class Snake:
    ''' Initialize Instance Attributes '''
    def __init__(self, name, body, color, fear, hunger): 
        self.name = name
        self.body = body
        self.color = color
        self.fear = fear
        self.hunger = hunger
        self.grid_x = int(grid_size_x.get())
        self.grid_y = int(grid_size_y.get())
        self.energy = 300
        self.age = 0
        self.food_eaten = 0
        self.state = 'alive'
        self.head = self.head_pixel()
        
    def die(self):
        for elem in self.body:
            draw_plant(elem[0],elem[1])

        canvas.delete(self.name)
        print(self.name + " has died.")
        self.state = 'dead'

    def draw(self):
        ''' should only need to draw the head at every step. '''
        ''' moving is another option '''
        ''' simplest is to delete and redraw everything ?? '''
        body_length_index = len(self.body)-1
        
        for index,elem in enumerate(self.body):
            if index == 0:
                draw_rect(elem[0],elem[1],self.color,[self.name,'snake','tail'])
            elif index == body_length_index:
                draw_rect(elem[0],elem[1],self.color,[self.name,'snake','head'])                
            else:
                draw_rect(elem[0],elem[1],self.color,[self.name,'snake'])

    ''' All this just to draw eyes on the head as it moves.'''
    # It's a goddamn eyesore lmao.
    def draw_eyes(self):
        global x_step
        global y_step
        eye_tag = self.name
        eye_fill = 'black'
        ''' if: snake doesn't move '''
##        if self.body[-1][0]-self.body[-2][0] == 0 and self.body[-1][1]-self.body[-2][1] == 0:
##            x1 = self.body[-1][0]*x_step + 0.22*x_step
##            y1 = self.body[-1][1]*y_step + 0.22*y_step
##            x2 = self.body[-1][0]*x_step + 0.38*x_step
##            y2 = self.body[-1][1]*y_step + 0.38*y_step
##            canvas.create_rectangle(x1,y1,x2,y2,fill='red',tag=eye_tag)
##            x1 = self.body[-1][0]*x_step + 0.62*x_step
##            y1 = self.body[-1][1]*y_step + 0.22*y_step
##            x2 = self.body[-1][0]*x_step + 0.78*x_step
##            y2 = self.body[-1][1]*y_step + 0.38*y_step
##            canvas.create_rectangle(x1,y1,x2,y2,fill='red',tag=eye_tag)
        ''' snake goes up'''
        if self.body[-1][0]-self.body[-2][0] == 0 and self.body[-1][1]-self.body[-2][1] == 1:
            x1 = self.body[-1][0]*x_step + 0.22*x_step
            y1 = self.body[-1][1]*y_step + 0.62*y_step
            x2 = self.body[-1][0]*x_step + 0.38*x_step
            y2 = self.body[-1][1]*y_step + 0.78*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
            x1 = self.body[-1][0]*x_step + 0.62*x_step
            y1 = self.body[-1][1]*y_step + 0.62*y_step
            x2 = self.body[-1][0]*x_step + 0.78*x_step
            y2 = self.body[-1][1]*y_step + 0.78*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
        ''' snake goes right '''
        if self.body[-1][0]-self.body[-2][0] == 1 and self.body[-1][1]-self.body[-2][1] == 0:
            x1 = self.body[-1][0]*x_step + 0.62*x_step
            y1 = self.body[-1][1]*y_step + 0.22*y_step
            x2 = self.body[-1][0]*x_step + 0.78*x_step
            y2 = self.body[-1][1]*y_step + 0.38*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
            x1 = self.body[-1][0]*x_step + 0.62*x_step
            y1 = self.body[-1][1]*y_step + 0.62*y_step
            x2 = self.body[-1][0]*x_step + 0.78*x_step
            y2 = self.body[-1][1]*y_step + 0.78*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
        ''' snake goes down'''
        if self.body[-1][0]-self.body[-2][0] == 0 and self.body[-1][1]-self.body[-2][1] == -1:
            x1 = self.body[-1][0]*x_step + 0.22*x_step
            y1 = self.body[-1][1]*y_step + 0.22*y_step
            x2 = self.body[-1][0]*x_step + 0.38*x_step
            y2 = self.body[-1][1]*y_step + 0.38*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
            x1 = self.body[-1][0]*x_step + 0.62*x_step
            y1 = self.body[-1][1]*y_step + 0.22*y_step
            x2 = self.body[-1][0]*x_step + 0.78*x_step
            y2 = self.body[-1][1]*y_step + 0.38*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
        ''' snake goes left '''
        if self.body[-1][0]-self.body[-2][0] == -1 and self.body[-1][1]-self.body[-2][1] == 0:
            x1 = self.body[-1][0]*x_step + 0.22*x_step
            y1 = self.body[-1][1]*y_step + 0.22*y_step
            x2 = self.body[-1][0]*x_step + 0.38*x_step
            y2 = self.body[-1][1]*y_step + 0.38*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
            x1 = self.body[-1][0]*x_step + 0.22*x_step
            y1 = self.body[-1][1]*y_step + 0.62*y_step
            x2 = self.body[-1][0]*x_step + 0.38*x_step
            y2 = self.body[-1][1]*y_step + 0.78*y_step
            canvas.create_rectangle(x1,y1,x2,y2,fill=eye_fill,tag=eye_tag)
            
    def eat(self):
        ''' Don't define unchanging variables inside looped behaviour... '''
        global x_step
        global y_step
        global time

        [head_x,head_y] = self.head_xy(x_step,y_step)

        item_near = canvas.find_closest(head_x,head_y)
        item_tags = canvas.gettags(item_near)

        if (item_near and 'plant' in item_tags):
            #print(item_tags)
            item_x = canvas.coords(item_near)[0] + 0.5*x_step
            item_y = canvas.coords(item_near)[1] + 0.5*y_step
            if (abs(head_x - item_x) < x_step-1) and (abs(head_y - item_y) < y_step-1): 
                canvas.delete(item_near)
                self.energy += 50
                self.food_eaten += 1
                ''' every 30 food eaten snake grows '''
                if self.food_eaten % 30 == 0:
                    self.grow()
                    
    def grow(self):
        ''' Adds an extra segment to snake's body '''
        ''' Gen 01: Trigger in update_body(): after 50 pieces of food are eaten '''
        self.body = np.append(self.body,[self.body[-1]],axis=0)

        
    def head_pixel(self):
        ''' Generates unique 5x5 pixel art for the snake head. '''
        head_array = np.zeros([5,5])
        for n in range(5):
            for m in range(5):
                r = random.randint(1,100)
                if r <= 50:
                    head_array[n,m] = 1
        return head_array
        
    def head_xy(self,x_step,y_step):
        ''' Returns the xy (canvas) coordinates of the snake head... '''
        ''' cf: update_body() ''' # top-left corner
        head_x = self.body[-1][0]*x_step + 0.5*x_step
        head_y = self.body[-1][1]*y_step + 0.5*y_step
        return [head_x, head_y]
        
        
    def update_body(self):
        global x_step
        global y_step
        enemy_nearby = False
        food_nearby = False
        self.age += 1
        self.energy += -1
        canvas.delete(self.name) # delete snake body
        canvas.delete('eye') # delete snake eyes - order?
        
        body_clipped = np.delete(self.body,0,0) # numpy arrays are size-immutable
            
        ''' Genetic Algorithm '''
        ''' Gen 01: The snake randomly selects one of the four cardinal
            directions or chooses no movement and heads that way. '''

        v = self.view(x_step,y_step)

        rand_int = random.randint(1,100)
        ''' snake is fearful with probability p = self.fear '''
        if rand_int < self.fear:
            # spiral out (11 x 11) matrix - 6 midpoint.
            # no need to 'spiral out' as snake runs from far enemies
            for x in [1,3,5]:
                for m in range(0,2*x):
                    for n in range(0,2*x):
                        if v[5-x+m,5-x+n] == 3:
                            enemy_nearby = True
                            [a,b] = [5-m,5-n]
                            if a >= 0 and b >= 0:
                                # more detailed analysis involves slope a/b
                                # or extricate from grid and move in opposite dir
                                if rand_int < 50: # because we know the quadrant
                                    d = [0,1]
                                else:
                                    d = [1,0]
                            if a < 0 and b < 0:
                                if rand_int < 50:
                                    d = [0,-1]
                                else:
                                    d = [-1,0]
                            if a < 0 and b >= 0:
                                if rand_int < 50:
                                    d = [1,0]
                                else:
                                    d = [0,-1]
                            if a >= 0 and b < 0:
                                if rand_int < 50:
                                    d = [0,1]
                                else:
                                    d = [-1,0]
                            break
                        
        if enemy_nearby == False and rand_int < self.hunger:
            ''' move towards food '''
            for x in [1,3,5]:
                for m in range(0,2*x):
                    for n in range(0,2*x):
                        if v[5-x+m,5-x+n] == 1: # if we see food item
                            food_nearby = True
                            [a,b] = [5-m,5-n]
                            if a >= 0 and b >= 0:
                                if rand_int < 50: # because we know the quadrant
                                    d = [0,-1]
                                else:
                                    d = [-1,0]
                            if a < 0 and b < 0:
                                if rand_int < 50:
                                    d = [0,1]
                                else:
                                    d = [1,0]
                            if a < 0 and b >= 0:
                                if rand_int < 50:
                                    d = [-1,0]
                                else:
                                    d = [0,1]
                            if a >= 0 and b < 0:
                                if rand_int < 50:
                                    d = [0,-1]
                                else:
                                    d = [1,0]
                            break

        if enemy_nearby == False and food_nearby == False:
            if rand_int < 20:
                d = [1,0]
            if (20 <= rand_int < 40):
                d = [0,-1]
            if (40 <= rand_int < 60):
                d = [-1,0]
            if (60 <= rand_int <= 80):
                d = [0,1]
            if (80 <= rand_int <= 100):
                d = [0,0]
                self.energy += 1 # not moving doesn't use energy

        c = np.mod(body_clipped[-1]+d,[self.grid_x,self.grid_y])
        
        ''' There's this whole stupid delete the entire body everytime
            thing too... Better is MOVE each body element? The head into
            a new square. The body and tail follows the segment immediately
            in front of it... todo '''
        
        body_clipper = np.append(body_clipped,[c],0)
        #print(body_clipper)
        self.body = body_clipper

        self.eat() # eat before draw or snake eats own head.
        self.draw()
        self.draw_eyes()

        ''' snake dies if energy runs out '''
        if self.energy < 0:
            self.die()

        
    def view(self,x_step,y_step):
        ''' creates a matrix of surrounding area (snakes visual field) '''
        ''' gen 01: creates a 5x5 matrix: 0 for empty, 1 for plant, '''
        ''' 2 for own body, 3 for other snake. '''
        view_space = np.zeros([11,11])
        head_xy = self.head_xy(x_step,y_step)
        #print(view_space)
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        for n in range(0,10):
            for m in range(0,10):
                x1 = np.mod(head_xy[0] - 5*x_step + n*x_step - 1, width )
                x2 = np.mod(head_xy[0] - 5*x_step + n*x_step + 1, width )
                y1 = np.mod(head_xy[1] - 5*y_step + m*y_step - 1, height)
                y2 = np.mod(head_xy[1] - 5*y_step + m*y_step + 1, height) 
                #print(view_space[n,m])
                #canvas.create_rectangle([x1,y1],[(x2,y2],fill='red',tag='view')
                viewed_items = canvas.find_overlapping(x1, y1, x2, y2)
                for item in viewed_items:
                    item_tags = canvas.gettags(item)
                    # needs figuring...
                    ''' last item in the stack will take precedent '''
                    if 'plant' in item_tags:
                        view_space[n,m] = 1
                    if 'snake' in item_tags and self.name not in item_tags:
                        view_space[n,m] = 3
                        break
                    if self.name in item_tags:
                        view_space[n,m] = 2
                        break
                    
        #print(self.body[-1])
        view_space = np.transpose(view_space)
        #print(view_space)
        return view_space
    
### END of Snake Class ###

''' General Purpose Functions '''

def board_regen(event):
    global left_mouse_down
    global time

    tm.sleep(0.1)

    # Doesn't work in the situation where we 'let go' of the resizing mouse...
    if left_mouse_down == False:
            generate_board()

def draw_plant(m,n):
    draw_rect(m,n,'green','plant')
    
def draw_rect(m,n,colour='grey',tagg='rect'):

    ''' Get grid size (n x m) from the grid_size x&y Entry fields '''
    grid_x = int(grid_size_x.get())
    grid_y = int(grid_size_y.get()) 

    ''' Necesarry to check definitions as grid entry fields may be empty. '''
    if (grid_x and grid_y):
        [rect_x,rect_y] = grid_xy(grid_x,grid_y)
        canvas.create_rectangle([(m)*(rect_x),(n)*(rect_y)],[(m+1)*(rect_x),(n+1)*(rect_y)],fill=colour,tag=tagg)

def food_grow():
    ''' every 10 frames add three foods... '''
    n = int(grid_size_x.get())
    m = int(grid_size_y.get())
    a = random.randint(0,n)
    b = random.randint(0,m)
    draw_plant(a,b)

def grid_xy(n,m):
    ''' Returns x and y (Cartesian) canvas coordinates '''
    ''' Given grid-size (n x m) '''
    canvas.update()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    return [(canvas_width)/(n),(canvas_height)/(m)] # this isn't right...

def grid_steps():
    canvas.update()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    n = int(grid_size_x.get())
    m = int(grid_size_y.get())
    return [(canvas_width)/(n),(canvas_height)/(m)]

def initial_food_generation(p,row,col): 
    for n in range(0,row):
        for m in range(0,col):
            if random.randint(0,100) < p:
                draw_plant(n,m)
    

def canvas_update():
    global canvas_update_speed
    global loop_active
    global plant_list
    global snake_display
    global snake_string
    global time
    
    if loop_active:
        time = time + 1
        time_string = "Time = " + str(time) 
        v.set(time_string)

        if snake.state == 'alive':
            snake.update_body()
        if snake2.state == 'alive':
            snake2.update_body()
        if snake.state == 'dead' and snake2.state == 'dead':
            pause_loop()

        '''add plant elements randomly'''
        #ensures the board state does not run out of food for snakes to eat.
        p_gen = random.randint(1,100) # generate random probability
        if p_gen < 5:
            plant_list.append(Plant())

        for plant in plant_list:
            plant.age += 1
            plant.grow()


        if snake_display:
            for s in [snake,snake2]:
                if s.name == snake_string:
                    display_text.set("Snake: " + snake_string + "\n Age: " + str(s.age) + "\n Energy: " + str(s.energy))
        
        
        canvas.after(canvas_update_speed,canvas_update)

def click_canvas(event):
    global snake_string
    global left_mouse_down
    global snake_display

    left_mouse_down = True
    
    scan_width = s_canvas.winfo_width()
    scan_height = s_canvas.winfo_height()
    
    item = event.widget.find_withtag("current")
    itags = canvas.gettags(item)
    #print(itags)

    slither = [snake,snake2]
    for s in slither:
        if s.name in itags:
            snake_display = True
            s_canvas.delete('pixel')
            xstep = scan_width/5
            ystep = scan_height/5
            snake_string = s.name
            display_text.set("Snake: " + snake_string + "\n Age: " + str(s.age) + "\n Energy: " + str(s.energy))
            for n in range(5):
                for m in range(5):
                    x1 = n*xstep
                    y1 = m*ystep
                    x2 = (n+1)*xstep
                    y2 = (m+1)*ystep
                    if [n,m]==[1,1] or [n,m]==[3,1]:
                        s_canvas.create_rectangle(x1,y1,x2,y2,fill='red',tag='pixel')
                    elif s.head[n,m]==1:
                        s_canvas.create_rectangle(x1,y1,x2,y2,fill='black',tag='pixel')
                    elif s.head[n,m]==0:
                        s_canvas.create_rectangle(x1,y1,x2,y2,fill=s.color,tag='pixel')
            
    if 'plant' in itags:
        snake_display = False
        display_text.set('plant')
        s_canvas.delete('all')
        x1 = (0.2)*scan_width
        y1 = (0.2)*scan_height
        x2 = (0.8)*scan_width
        y2 = (0.8)*scan_height
        s_canvas.create_rectangle(x1,y1,x2,y2,fill='green',tag='pixel')

def mouse_down(event):
    global left_mouse_down
    left_mouse_down = True
    #print('Left mouse down')

def mouse_up(event):
    global left_mouse_down
    left_mouse_down = False
    #print('Release!')
    
''' Frame Functions '''
# Button Toggles

def toggle_play():
    global loop_active
    global canvas_update_speed
    
    if loop_active:
        loop_active = False #clicking play twice pauses the loop
        #print(Play_Button)
        canvas_update_speed = 100
        Play_Button.config(relief="raised")
    else:
        loop_active = True
        Play_Button.config(relief="sunken")
        canvas_update()

def slow_loop():
    global canvas_update_speed
    canvas_update_speed = int(2*canvas_update_speed)

def fast_forward():
    global canvas_update_speed
    canvas_update_speed = int(0.5*canvas_update_speed)
        

def pause_loop():
    global loop_active
    global canvas_update_speed
    
    if loop_active:
        loop_active = False
        Play_Button.config(relief="raised")
        canvas_update_speed = 100

''' Initialize Root Window '''
root = Tk()
root.title("Snake Game")
root.config(padx=5,pady=5)
root.bind_all('<ButtonRelease-1>',mouse_up)
root.bind_all('<Button-1>',mouse_down)

''' Get geometry of root (startup) window '''
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
padded_w = screen_width - 400   # Pad's user screen resolution.
padded_h = screen_height - 200  # Aesthetic for initial launch of program.
str_geometry = "%dx%d" % (padded_w,padded_h)
root.geometry(str_geometry)

''' Construction of GUI Frames '''
# A1 BX
# A2 BY 
#    BZ

frameA = Frame(root,bd=1,relief='solid')
frameA.pack(expand=True,fill=BOTH,side='left')

frameA1 = Frame(frameA,bd=1,relief='solid')
frameA1.pack(expand=True,fill=BOTH)

frameA2 = Frame(frameA,bd=1,relief='solid')
frameA2.pack(fill=X)

frameB = Frame(root,bd=1,bg='white',relief='solid')
frameB.pack(fill=Y,side='left')

''' Initialize Canvas '''
canvas = Canvas(frameA1,width=300,height=300,bg='white',bd=1,relief='solid')
canvas.bind('<Button-1>', click_canvas)
# canvas.bind('<Configure>',board_regen) # WAY too memory intense atm.
canvas.pack(expand=True,fill=BOTH,side='left')

''' Snake Head CANVAS? Frame '''
s_canvas = Canvas(frameA2,width=60,height=60,bd=1,relief='solid')
s_canvas.pack(side='left',padx=20)

''' Snake Label Below Canvas '''
display_text = StringVar()
snake_string = " ... " 
display_text.set(snake_string)
Snake_Label = Label(frameA2,textvariable=display_text,bd=1,relief='solid')
Snake_Label.pack(expand=True,fill=BOTH,side='top')

''' Frames On Right Side '''
frameX = Frame(frameB)
frameX.pack()

frameY = Frame(frameB)
frameY.pack()

frameZ = Frame(frameB)
frameZ.pack()

frameZ1 = Frame(frameB)
frameZ1.pack()

frameZ2 = Frame(frameB)
frameZ2.pack()

frameZ3 = Frame(frameB)
frameZ3.pack()

''' Draw Grid - Entry Fields & Labels '''
Grid_Num_Rows = Label(frameB,text="Grid Size = ")
Grid_Num_Rows.pack(side='left')

grid_size_x = Entry(frameB,width=3)
grid_size_x.insert(10,'20')
grid_size_x.pack(side='left')

Grid_Label_x = Label(frameB,text="×").pack(side='left')

grid_size_y = Entry(frameB,width=3)
grid_size_y.insert(0,'20')
grid_size_y.pack(side='left')

''' Draw Grid Button '''
# Note: Buttons pack()ed inline are not recognised as Button objects.

''' Food Growth - Label & Entry '''
##Food_Growth = Label(frameX, text="Food Growth = ")
##Food_Growth.pack(side='left')
##
##Food_Growth_Entry = Entry(frameX,width=2)
##Food_Growth_Entry.insert(0,'10')
##Food_Growth_Entry.pack(side='left')

''' Food Generation - Label & Entry '''
Initial_Food = Label(frameY, text="Initial Food = ")
Initial_Food.pack(side='left')

Initial_Food_Entry = Entry(frameY,width=2)
Initial_Food_Entry.insert(0,'33')
Initial_Food_Entry.pack(side='left')

Food_Label_2 = Label(frameY,text="%").pack(side='left')

''' Time Step Counter and Label '''
v = StringVar()
Time_Step_Label = Label(frameZ, textvariable=v).pack()
time_string = "Time = " + str(time) 
v.set(time_string)

''' Boardstate Generation Button '''
##Board_Set_Button = Button(frameZ1,text="Reset Board",command=generate_board) 
##Board_Set_Button.pack()

''' Number of Snakes - Label and Entry Field '''

##Num_Snake_Label = Label(frame9,text="Number of Snakes: ").pack(side='left')
##Num_Snakes_Entry = Entry(frame9,width=2).pack(side='left')

##''' Slow Button '''
##slow_image = PhotoImage(file = 'slow_button.png')
##Slow_Button = Button(frame10,image=slow_image,command=slow_loop,relief="raised")
##Slow_Button.pack(side='left')

''' Play Button '''
play_image = PhotoImage(file = 'play_button.png')
Play_Button = Button(frameZ2,image=play_image,command=toggle_play,relief="raised")
Play_Button.pack(side='left')

''' Fast Forward Button '''
# Maybe better in terms of game enjoyability to have NO FF ??
fast_forward_img = PhotoImage(file = 'fast_forward_button.png')
Fast_Forward_Button = Button(frameZ2,image=fast_forward_img,command=fast_forward,relief="raised")
Fast_Forward_Button.pack(side='left')

''' Pause Button '''
pause_image = PhotoImage(file = 'pause_button.png')
Pause_Button = Button(frameZ2,image=pause_image,command=pause_loop)
Pause_Button.pack(side='left')

'''      ''' 
### Main ###
''' MAIN '''
###      ###

canvas.update()
[x_step,y_step] = grid_steps() 

''' Initialize and Draw Snakes '''

body = np.array([[4,6],[5,6],[6,6]])
snake = Snake('Jeff_Sr.',body,'#33CEFF',fear=20,hunger=100)
snake.draw()

body2 = np.array([[7,10],[8,10],[9,10]])
snake2 = Snake('Snakerella',body2,'#B953FF',fear=88,hunger=100)
snake2.draw()

##for [a,b] in [[11,11],[11,12],[11,13]]:
##    draw_rect(a,b,'black','snake')

canvas.update()

#canvas.after(200, canvas_update)

root.mainloop()
