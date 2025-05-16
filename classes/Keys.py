from random import randint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window




class Keys(Widget):
    map_keys = []
    base_keys = None
    key_size = 9
    current_x_key = 1
    current_y_key = 1
    min_key_value = 1
    max_key_value = 999




    def __init__(self, **kwargs):
        super().__init__(**kwargs)




    def set_key(self):
        try:
            keys = self.random_keys()
            self.map_keys = keys
        
            self.base_keys = keys

        except Exception as e:
            print("\n\nError in 'Calculations' Class - 'set_key' Function", e)


    def random_keys(self):
        try:
            keys = []
            while len(keys) < 9:
                key = randint(self.min_key_value, self.max_key_value)
                keys.append(key) if int(str(key)[:1]) > 1  and len(str(key)) > 2 else None
            return keys
        
        except Exception as e:
            print("\n\nError in 'Keys' Class - 'random_keys' Function", e) 


    def explore(self):
        try:
            x = App.get_running_app().main.map.current_coords[0]
            y = App.get_running_app().main.map.current_coords[1]

            print("\n\n=============================\n")

            print("\n\ncoords")
            print(str(x), ", ", str(y))
            App.get_running_app().main.proof.coords = [x, y]

            if x == 0 and y == 0:
                print("\n\nreturned home")
                self.map_keys = self.base_keys
                return True
            
            if x == 0 and y > 1:
                x = int(str(self.base_keys[0])[:2])
            
            if x == 0 and y < -1:
                x = int(str(self.base_keys[1])[:2])

            if x == 0 and abs(y) == 1:
                x = int(str(self.base_keys[5])[:2])

            if x > 1 and y == 0:
                y = int(str(self.base_keys[2])[:2])

            if x < -1 and y == 0:
                y = int(str(self.base_keys[3])[:2]) 

            if abs(x) == 1 and y == 0:
                y = int(str(self.base_keys[6])[:2])   

            if x + y == 0:
                x = abs(x) * 7 if x > 0 else int(str(self.base_keys[7])[:2]) 
                y = abs(y) * 5 if y > 0 else int(str(self.base_keys[4])[:1])   
            
            keys = []

            i = 0
            while len(keys) < self.key_size:
                num = self.base_keys[i] * ((55-x-i) + y) * (15-x-i)
                new_num = num
                while new_num > self.max_key_value:
                    new_num = new_num - self.max_key_value
                num = abs(new_num)
                keys.append(num) 
                i += 1

            self.map_keys = keys

            print("\n\nmap keys")
            print(str(self.map_keys))

            App.get_running_app().main.proof.explore_data()

            print("\n\n=============================\n")

        except Exception as e:
            print("\n\nError in 'Keys' Class - 'reverse' Function", e) 


