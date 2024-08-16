from fractal import Fractal
def main():
   Fractal.print_fractals_list()
   while True:
      try:
         fractal_name = Fractal.get_input_name()
         break
      except ValueError:
         pass
   
   while True:
      try: 
         gens = Fractal.get_gens(fractal_name)
         break
      except ValueError:
         pass
   
   Fractal.draw_fractal_by_name(fractal_name=fractal_name, gens=gens)


if __name__ == '__main__':
   main()