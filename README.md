Infinite map within a finite amount of memory. All locations stay the same. 


Concepts:

    - A list of random numbers is generated when the game starts.

    - Sprite randomization is based on the initial random number grid and the current player coordinates. A new number list is generated each time the screen changes (when the player leaves the screen).

    - Calculations for sprite type, position and color are determined by the numbers in the number list. In certain cases, numbers from the original list are used. 

    - The only static memory is the original random number list, coordinates (x, y) and player sprite attributes. 

    - Current, non-static memory changes for each map. This is the npc/map sprites. 

    - To prevent large numbers and to keep values within acceptable ranges for calculations in this demo, map keys are kept within a range of 1-999. For more detailed applications, the ceiling for these values can be higher. 
    


Proof:

    - To test the map, visit several areas by pressing the directional arrow keys. The map changes when the player object leaves the screen. The concept can become clear by revisting past locations. 

    - Press the 'x' button at any time to display proof of matching map number grids that have been visited in the console. 

    - Proof is displayed as a set matching number keys and their related coordinates.

    - For better readability, an output file can be created by pressing 'f'. The file will be located in this project's root directory and titled "map_proof.txt".



Notes:

    - Randomization quality can be increased further by making more complex math-based algorithms for sprite generation keys.

    - As mentioned previously, the map keys are what is used to determine the placement, shape and color of the sprites on the screen. This list can be expanded for more sprites and/or details. For instance, in a large 3d game, the list would be much greater in size. This is due to the number of factors that are used to affect the display (skin color range, detail, animation, sound etc.). 
    
    - A rudimentary concept is shown in this demo to convey the basic idea of unlimited memorized object randomization with a limited amount of memory. In other words, the 2d shapes on the screen in this app can be expanded upon given a larger list of map keys (and a larger range of values if needed). The concept is the same for a 3d game, but the design process is much more involved.

    - This is only a seemingly infinite map. Most users will never experience the same location twice, but it is possible. Eventually, the visuals can match another map exactly.
    
    - When testing the theory, consider that the only way no matching maps could exist is if the number range used for the keys is incremented based on user coordinates and has no limit. This would allow for more precise calculations. Still, considering constraints such as the size of each map area, and sprite variables such as colors and shapes, there would be a limited amount of randomizations even with an infinite range of calculation keys. 
    
    - Perhaps there could technically be unlimited colors or shapes, but eventually the nuances would be so small that nobody could tell the difference. For example, if the shade in a sprite's rgba value is .000000001 different than the next most comparable object, and all other variables have similar properties.




Created by Jason Dunn

Github: https://www.github.com/jgddesigns

Portfolio: https://work-portfolio-jgddesigns-projects.vercel.app/

jaygeorgedunn@gmail.com