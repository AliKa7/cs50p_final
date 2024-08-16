import turtle


#screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.bgcolor('black')
screen.delay(0)

#turtle settings
nazik = turtle.Turtle()
nazik.pensize(1)
nazik.setpos(-350, -200)
nazik.color('orange')
nazik.speed(50)

step = 1
angle = 120

#l-system settings
gens = 7
axiom = 'F'
chr_1, rule_1 = 'F', 'F-G+F+G-F'
chr_2, rule_2 = 'G', 'GG'


def new_line(axiom):
   return ''.join(rule_1 if chr == chr_1 else rule_2 if chr == chr_2 else chr for chr in axiom)


def get_result(gens, axiom):
   for gen in range(gens):
      axiom = new_line(axiom)
      
   return axiom
   
for gen in range(gens+1):
   turtle.pencolor('white')
   turtle.goto(-WIDTH // 2 + 120, -HEIGHT // 2 + 120)
   turtle.clear()
   turtle.write(f'generation: {gen}', font=('Arial', 50, 'normal'))

   for chr in axiom:
      if chr == chr_1 or chr == chr_2:
         nazik.forward(step) 
      
      elif chr == '+':
         nazik.right(angle)

      elif chr == '-':
         nazik.left(angle)
   
   axiom = new_line(axiom)
   
screen.exitonclick()