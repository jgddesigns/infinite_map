from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)



class Proof(Widget):
        itr = 0 
        test_explore = []
        coords = []
        matching_data = []
    



        def __init__(self, **kwargs):
                super().__init__(**kwargs)




        def explore_data(self):
                try:
                        self.itr +=1

                        self.test_explore.append({"iteration": str(self.itr), "keys": App.get_running_app().main.key.map_keys, "coords": str(self.coords)})

                        for data in self.test_explore:
                                self.check_match(data) 
                                
                except Exception as e:
                        print("\n\nError in 'Proof' Class - 'explore_data' Function", e)


        def check_match(self, data):
                try:
                        matched = False

                        for compare in self.test_explore:
                                if str(data["keys"]) == str(compare["keys"]) and str(data["iteration"]) != str(compare["iteration"]):
                                        self.matching_data.append([data, compare]) if [data, compare] not in self.matching_data and [compare, data] not in self.matching_data else None
                                        matched = True
                                
                        return matched
                
                except Exception as e:
                        print("\n\nError in 'Proof' Class - 'check_match' Function", e)


        def show_proof(self):
                try:
                        print("\n\n\n\nSHOWING PROOF...\n\n\n\n")

                        if len(self.matching_data) < 1:
                                print("\n\nNo maps have been revisited.")

                        i = 1
                        for data in self.matching_data:
                                print("\n\nProof #" + str(i) + ":\n")
                                print("data: " + str(data[0]))
                                print("compare: " + str(data[1]))

                                i+=1

                        print("\n\n\n\nEND SHOWING PROOF\n\n\n\n")

                except Exception as e:
                        print("\n\nError in 'Proof' Class - 'show_proof' Function", e)


        def output(self):
                try:
                        with open('map_proof.txt', 'w') as file:
                                file.write("INFINITE MAP CONCEPT SESSION DATA\n\n\n\n")
                                file.write("The format is as follows:")
                                file.write("\n\niteration - the count of eachm time the map changes.")
                                file.write("\n\nkeys - the randomized keys used to create and place sprites.")
                                file.write("\n\ncoords - the coordinates where the match appears.")
                                file.write("\n\n\nNote: Iterations will be different and indicate progression/movement of the map. Matching keys and coordinates indicate that the map has the same layout at the same coordinates that were previously visited. When this occurs and the iteration differs, this shows that the map layout has stayed the same, despite wherever else the player has travelled on the map.\n\n\n\nData:\n\n")

                                i = 1
                                for data in self.matching_data:
                                        file.write("\n\n\nProof " + str(i))
                                        file.write("\n\ndata: " + str(data[0]))
                                        file.write("\ncompare: " + str(data[1]))               
                                        i+=1

                                print("\n\nFile written successfully.")

                except Exception as e:
                        print("\n\nError in 'Proof' Class - 'output' Function", e)
    