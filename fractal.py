import csv
from draw_data import DrawData
import colorama
from colorama import Fore, Style
import turtle
from random import randint

class Fractal():
   fractals_list = ['Honeycomb', 'Triangle', 'Dragon', 'Snowflake', 'Tree', 'Complex tree']
   gens_dict = {
      'Honeycomb': [14, 18],
      'Triangle': [3, 8],
      'Dragon': [9, 13],
      'Snowflake': [2, 5],
      'Tree': [4, 7],
      'Complex tree': [6, 9],
   }
   
   @classmethod
   def print_fractals_list(cls):
      colorama.init(autoreset=True)
      print(Fore.BLUE + Style.BRIGHT + 'Available fractals: ')
      print(Fore.YELLOW + Style.BRIGHT + 'Honeycomb*')
      print(Fore.RED + Style.BRIGHT + 'Triangle*')
      print(Fore.MAGENTA + Style.BRIGHT + 'Dragon*')
      print(Fore.WHITE + Style.BRIGHT + 'Snowflake*')
      print(Fore.GREEN + Style.BRIGHT + 'Tree*')
      print(Fore.CYAN + Style.BRIGHT + 'Complex tree*')
      

   @classmethod
   def get_input_name(cls):
      typed_name = input('Type the name of fractal picture of which you want to see: ').strip().lower().capitalize()
      if typed_name in cls.fractals_list:
         return typed_name
      else:
         raise ValueError()
      
   @classmethod
   def get_gens(cls, fractal_name):
      range_ = cls.gens_dict[fractal_name]
      gens = int(input(f'Type the level of fractal complexity, of range {range_[0]} to {range_[1]} inclusively: '))
      if gens >= range_[0] and gens <=range_[1]:
         return gens
      else:
         raise ValueError()
      
   @classmethod
   def draw_fractal_by_name(cls, fractal_name, gens):
      if fractal_name == 'Honeycomb':
         draw_data = DrawData(
            name='Honeycomb', 
            full_name='Koch Hierarchical Honeycomb',
            gens=gens, 
            draw_color='orange', 
            angle=60, 
            axiom='A',
            chr_1='A',
            rule_1='AB',
            chr_2='B',
            rule_2='A'
            )
      elif fractal_name == 'Triangle':
         draw_data = DrawData(
            name='Triangle', 
            full_name='Sierpinski triangle',
            gens=gens, 
            draw_color='red', 
            angle=120, 
            axiom='F',
            chr_1='F',
            rule_1='F-G+F+G-F',
            chr_2='G',
            rule_2='GG'
         )
      elif fractal_name == 'Dragon':
         draw_data = DrawData(
            name='Dragon', 
            full_name='Harter-Heighway Dragon',
            gens=gens, 
            draw_color='magenta', 
            angle=90, 
            axiom='XY',
            chr_1='X',
            rule_1='X+YF+',
            chr_2='Y',
            rule_2='-FX-Y'
         )
      elif fractal_name == 'Snowflake':
         draw_data = DrawData(
            name='Snowflake', 
            full_name='Koch Snowflake',
            gens=gens, 
            draw_color='white', 
            angle=60, 
            axiom='F++F++F',
            chr_1='F',
            rule_1='F-F++F-F',
            chr_2='',
            rule_2=''
         )
      elif fractal_name == 'Tree':
         draw_data = DrawData(
            name='Tree', 
            full_name="L-system's tree",
            gens=gens, 
            draw_color='green', 
            angle=25, 
            axiom='XY',
            chr_1='F',
            rule_1='FF',
            chr_2='X',
            rule_2='F[+X]F[-X]+X'
         )
      elif fractal_name == 'Complex tree':
         draw_data = DrawData(
            name="Complex tree", 
            full_name="L-system's complex tree",
            gens=gens, 
            draw_color=[0.35, 0.2, 0.0], 
            angle=lambda: randint(10, 30), 
            axiom='XY',
            chr_1='X',
            rule_1='F[@[-X]+X]',
            chr_2='',
            rule_2=''
         )
      
      try:
         draw_fractal_template(draw_data=draw_data)
      except ArithmeticError:
         colorama.init(autoreset=True)
         print(Fore.BLUE + Style.BRIGHT + 'Program is closed.')
         
   @classmethod
   def get_final_gen(cls, axiom, gens, fractal_name, chr_1, rule_1, chr_2, rule_2):
      def new_line(axiom):
         if fractal_name == 'Honeycomb':
            return ''.join(rule_1 if chr == chr_1 else rule_2 for chr in axiom)
         elif fractal_name == 'Triangle' or fractal_name == 'Dragon':
            return ''.join(rule_1 if chr == chr_1 else rule_2 if chr == chr_2 else chr for chr in axiom)
         elif fractal_name == 'Snowflake' or fractal_name == 'Complex tree':
            return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom])
         elif fractal_name == 'Tree':
            return ''.join([rule_1 if chr == chr_1 else rule_2 if chr == chr_2 else chr for chr in axiom])

      for _ in range(gens):
         axiom = new_line(axiom)
      
      return axiom

def draw_fractal_template(draw_data: DrawData):
   #screen settings
   screen = turtle.Screen()
   screen.bgcolor('black')
   screen.delay(0)
   
   #l-system settings
   gens = draw_data.gens
   axiom = draw_data.axiom
   chr_1, rule_1 = draw_data.chr_1, draw_data.rule_1,
   chr_2, rule_2 = draw_data.chr_2, draw_data.rule_2,
   stack = []
   
   #turtle settings
   angle = draw_data.angle
   nazik = turtle.Turtle()
   
   with open("complexity_settings.csv", mode="r") as file:
      reader = csv.DictReader(file)
      for row in reader:
         if row['name']==draw_data.name and int(row['gens']) == gens:
            nazik.pensize(int(row['pensize']))
            thickness = int(row['pensize'])
            x, y = row['position'].split(',')
            nazik.setpos(int(x), int(y))
            step = float(row['step'])
            
   nazik.hideturtle()
   nazik.speed(1000)
   nazik.color(draw_data.draw_color)

   draw_information(gens, draw_data)
   
   axiom = Fractal.get_final_gen(axiom, gens, draw_data.name, chr_1, rule_1, chr_2, rule_2)
   #print(axiom)
   #drawing fractal
   if draw_data.name == 'Honeycomb':
      for chr in axiom:
         if chr == chr_1:
            nazik.left(angle)
            nazik.forward(step)
         elif chr == chr_2:
            nazik.right(angle)
            nazik.forward(step)
   
   elif draw_data.name == 'Triangle' or draw_data.name == 'Dragon':
      for chr in axiom:
         if chr == chr_1 or chr == chr_2:
            nazik.forward(step) 
         elif chr == '+':
            nazik.right(angle)
         elif chr == '-':
            nazik.left(angle)
   
   elif draw_data.name == 'Snowflake':
      for chr in axiom:
         if chr == chr_1:
            nazik.forward(step) 
         elif chr == '+':
            nazik.right(angle)
         elif chr == '-':
            nazik.left(angle)
   
   elif draw_data.name == 'Tree':
      nazik.left(90)
      for chr in axiom:
         if chr == chr_1:
            nazik.forward(step)
         elif chr == '+':
            nazik.right(angle)
         elif chr == '-':
            nazik.left(angle)
         elif chr == '[':
            angle_, pos_ = nazik.heading(), nazik.pos()
            stack.append((angle_, pos_))
         elif chr == ']':
            angle_, pos_ = stack.pop()
            nazik.setheading(angle_)
            nazik.penup()
            nazik.goto(pos_)
            nazik.pendown()
   
   elif draw_data.name == 'Complex tree':
      nazik.left(90)
      #thickness = draw_data.pensize
      colors = draw_data.draw_color
      for chr in axiom:
         nazik.color(colors)
         if chr == 'F' or chr == 'X':
            nazik.forward(step)
         elif chr == '@':
            step -= 6
            colors[1]+=0.04
            thickness -= 2
            thickness = max(1, thickness)
            nazik.pensize(thickness)
         elif chr == '+':
            nazik.right(angle())
         elif chr == '-':
            nazik.left(angle())
         elif chr == '[':
            angle_, pos_ = nazik.heading(), nazik.pos()
            stack.append((angle_, pos_, thickness, step, colors[1]))
         elif chr == ']':
            angle_, pos_, thickness, step, colors[1]  = stack.pop()
            nazik.pensize(thickness)
            nazik.setheading(angle_)
            nazik.penup()
            nazik.goto(pos_)
            nazik.pendown()
         

   screen.exitonclick()
   
#function to write information for user
def draw_information(gens, draw_data: DrawData):
   turtle.title('Fractals drawer, CS50P Final Project')
   turtle.penup()
   turtle.pencolor('white')
   turtle.goto(-680, -330)
   turtle.clear()
   turtle.write(f'Level of fractal complexity: {gens}', font=('Arial', 30, 'normal'))
   turtle.goto(-680, 250)
   turtle.write(f'Fractal: {draw_data.name}', font=('Arial', 45, 'bold'))
   turtle.goto(-675, 210)
   turtle.write(f'Full name: {draw_data.full_name}', font=('Arial', 18, 'normal'))
   turtle.goto(-675, 160)
   turtle.write('Project made by Ali Kaiyr, Kazakhstan', font=('Arial', 18, 'italic'))
   turtle.hideturtle()