#Dot Painting Maker     by Dr.M-Dev:
import colorgram
import random
from turtle import *
import turtle
#________________________
REFINED_colors_list = [] #THE LIST IS GLOBAL
IMAGE_FOUND = False
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def logo():
    print('''                                                                                                                                                  
                                                                  ...::::.      ...::::::::    :.      .:.   
      5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
      G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
      G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
      7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
      Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
      P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                                 !J!:                                                                
                                                                  ^G@@&P7:                                                           
                                             .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                        :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                    .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                                  ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                                ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                              7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                            .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                           :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                          .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                          #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                         !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                         B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                         @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                       .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                       .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
                   ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
                .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
              :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
            !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
         .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
         J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
          .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
            .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
               ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
                 :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
                   .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


     ''')

    print(""""******** WELCOME TO Dot Painting Maker   -   Dr.M-Dev *********""")


# CODE STARTS WITH:
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def rest_values():
    # restart req:
    global picked_an_image
    global set_extraction_amount
    global image_name
    global colors_amount
    #+
    global IMAGE_FOUND
    ############## - x - ##############
    picked_an_image = False
    set_extraction_amount = False
    image_name = ""
    colors_amount = 0
    #+
    IMAGE_FOUND = False




def start_code():
    # must call variables globally:
    global picked_an_image
    global image_name
    global set_extraction_amount
    global colors_amount
    #+
    global IMAGE_FOUND
    ############## - x - ##############
    picked_an_image = False
    set_extraction_amount = False
    image_name = ""
    colors_amount = 0
    #+
    IMAGE_FOUND = False

    # ________________
    while not picked_an_image:
        try:
            image_name = my_screen.textinput(title="Colors Extraction", prompt="to extract a set of colors from an image just copy and paste the image directory\n📝NOTE:[Example: C:\Downloads\image.png]").lower()
            picked_an_image = True
        except TypeError:
            print("\n")
            print("<!> Error, invalid directory link! try again <!>")
            print("\n")
    ##############################
    while not set_extraction_amount:
        try:
            colors_amount = int(my_screen.textinput(title="Colorset Size", prompt="how many colors do you plan to extract from the image?"))
            set_extraction_amount = True
        except TypeError:
            print("\n")
            print("<!> INPUT-Error, invalid input! try again, using numbers only :) <!>")
            print("\n")
        except ValueError:
            print("\n")
            print("<!> AMOUNT-Error, invalid number! try something bigger than a zero xD <!>")
            print("\n")
    ##############################



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Other functions
def extraction_operation(targeted_file_name, color_set_size):
    global IMAGE_FOUND
    IMAGE_FOUND = True #singnaling to start the code and stop the search-loop
    ##=====================================================================================Extracting Colors
    extracted_colors = colorgram.extract(targeted_file_name, color_set_size)
    # ++++++++++++++++++++++++++++++++++++++++
    # print(f"{rgb_0[0]},{rgb_0[1]},{rgb_0[2]}") #the 3 RGB values inside the 1st extracted color from the image!
    # print(color_0)


    ##=====================================================================================Storing Colors In A List
    global REFINED_colors_list
    #|
    REFINED_colors_list = [] #THE LIST IS GLOBAL
    #REMEMBER THAT EACH ITEM MUST BE [pencolor(r, g, b)] like r,g,b
    #EX:
    # tup = (0.2, 0.8, 0.55)
    # turtle.pencolor(tup)

    #___________________________
    def color_refiner(index): #startig 0 and ending in len(extracted_colors)+1 for the for loop
        color_obj = extracted_colors[index]
        obj_rgb = color_obj.rgb
        #########
        refined_color = obj_rgb[0],obj_rgb[1],obj_rgb[2]
        REFINED_colors_list.append(refined_color)

    #___________________________
    raw_color_index = 0 #Default
    for raw_colors in extracted_colors:
        color_refiner(raw_color_index)
        raw_color_index += 1



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++GRAPHICS! (GUI)-related
my_turtle = turtle.Turtle()
my_screen = Screen()
my_screen.title("🎨🖌Dot Paintings Maker  -  Dr.m_Dev")
####################
#Color mode and setup
turtle.colormode(255)
####################
# turtle.update()
segment_count = 1 #default
####################
#DIRECTION NOTES\\
# 0 - east      #>
# 90 - north    #^
# 180 - west    #<
# 270 - south   #v

#MOVES:
def horizontal_print_x(width, spacing):
    global my_turtle
    ##################
    my_turtle.penup()
    ##################
    my_turtle.setheading(0) #>
    my_turtle.forward(spacing) #to move forward, since the vertical-function will be drawing the dots on the Y axis! :)
    for dots in range(width-1):
        # ____________Coloring
        current_pen_color = random.choice(REFINED_colors_list)
        my_turtle.pencolor(current_pen_color)
        #
        #____________writing/marking
        my_turtle.pendown()
        my_turtle.forward(1)
        my_turtle.penup()
        #
        my_turtle.forward(spacing)
        #~~~~~DEBUG~~~~~~
        print("1 cycle on X")
        my_screen.update()  # DEBUG-UPDATE

#________________________________
def vertical_print_y(current_height_update, spacing, updated_segment_count):
    global my_turtle
    ##################-----------REPOSITIONING:
    my_turtle.teleport(0,0)
    my_turtle.setheading(90) #^
    #
    if current_height_update > 0:
        for steps in range(updated_segment_count-1):
            #____________Coloring
            current_pen_color = random.choice(REFINED_colors_list)
            my_turtle.pencolor(current_pen_color)
            #
            my_turtle.forward(spacing)
            #____________writing/marking
            my_turtle.pendown()
            my_turtle.forward(1)
            my_turtle.penup()
            # ~~~~~DEBUG~~~~~~
            my_screen.update() #DEBUG-UPDATE
            print(f"1 cycle on Y AND [{updated_segment_count}]")
    else:
        print("DONE DEBUG")

#________________________________
def printing_protocol(height, width, spacing):
    global segment_count
    global my_screen
    global current_height
    ##################-----------PRINTING:
    current_height = height
    #--
    for segments in range(current_height):
        current_height -= 1
        segment_count += 1
        #----------------
        horizontal_print_x(width, spacing)
        if current_height > 0:
            vertical_print_y(current_height, spacing, segment_count)
        # elif current_height == 0:                                        #Cancled
        #     horizontal_print_x(width, spacing) #to print the last row    #Cancled
        # ~~~~~DEBUG~~~~~~
        print("1 WHOLE cycle")
        my_screen.update() #DEBUG-UPDATE


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def print_on_coordinates(height, width, spacing, pensize_value ):
    global my_turtle
    global my_screen
    ##################
    #TURNING ON THE GRAPHICS
    ##################
    print(f"PRINTING... portrait [{height}] x [{width}] with spacing of [{spacing}] ")
    #_______________________
    # ______#OUR DRAWING TURTLE (Spawns here)
    # ___________________________________
    # Details:
    my_turtle.shape("classic")
    my_turtle.pencolor("Black")
    my_turtle.pensize(pensize_value)
    # ____________________________________#Reposition
    my_turtle.home()
    # ____________________________________#WORK/CREATING
    # ------REVEAL
    print(my_turtle)
    ##############################
    printing_protocol(height, width, spacing)
    ##############################
    # ------RESULT
    print(my_turtle)

    my_screen.textinput(title="PRINTING DONE!", prompt="Press OK to check the final result :)")
    # input("Pressing any key will restart your code :>")

    my_screen.mainloop()


#=============================
#=============================#=============================
#=============================
def define_painting():
    dimension_x_defined = False
    dimension_y_defined = False
    spacing_set = False
    pensize_set = False
    #
    painting_width = 0
    painting_height = 0
    spacing = 0
    pensize_value = 0

    #-------------------
    print("define the dimensions of the painting you want")
    #-------------------
    while not dimension_x_defined:
        try:
            painting_width = int(my_screen.textinput(title="The wanted width", prompt="Enter how many [pixels]:"))
            dimension_x_defined = True
        except TypeError:
            print("\n")
            print("<!> INPUT-Error, invalid input! try again, using numbers only :) <!>")
            print("\n")
        except ValueError:
            print("\n")
            print("<!> AMOUNT-Error, invalid number! try something bigger than a zero xD <!>")
            print("\n")

    #-------------------
    while not dimension_y_defined:
        try:
            painting_height = int(my_screen.textinput(title="The wanted height", prompt="Enter how many [pixels]:"))
            dimension_y_defined = True
        except TypeError:
            print("\n")
            print("<!> INPUT-Error, invalid input! try again, using numbers only :) <!>")
            print("\n")
        except ValueError:
            print("\n")
            print("<!> AMOUNT-Error, invalid number! try something bigger than a zero xD <!>")
            print("\n")

    #------------------
    while not spacing_set:
        try:
            spacing = int(my_screen.textinput(title="How much spacing you want",
                                              prompt="it's recommended 15-pixels, or anything more than 10"))
            spacing_set = True
        except TypeError:
            print("\n")
            print("<!> INPUT-Error, invalid input! try again, using numbers only :) <!>")
            print("\n")
        except ValueError:
            print("\n")
            print("<!> AMOUNT-Error, invalid number! try something bigger than a zero xD <!>")
            print("\n")

    # ------------------
    while not pensize_set:
        try:
            pensize_value = int(my_screen.textinput(title="Pensize/Dotsize",
                                              prompt="How big are the dots you want?: [recommended 5]"))
            pensize_set = True
        except TypeError:
            print("\n")
            print("<!> INPUT-Error, invalid input! try again, using numbers only :) <!>")
            print("\n")
        except ValueError:
            print("\n")
            print("<!> AMOUNT-Error, invalid number! try something bigger than a zero xD <!>")
            print("\n")

    #------------------
    if dimension_x_defined == True and dimension_y_defined == True : #IMPORTANT_POINT
        print_on_coordinates(painting_height, painting_width, spacing, pensize_value)





#=======================================================================================================================
#=======================================================================================================================CODE RUNS HERE
#=======================================================================================================================
RUNNING = True
did_it_run_once = False

while RUNNING:
    if did_it_run_once:
        print("\n" * 50)
        print("<!><!> Multiple directory errors have occurred, PLEASE make sure the directory is correct :[ <!><!>")
        print("restarting....")
    else:
        print("Loading... \n")

    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    my_screen.textinput(title="welcome to DOT-PAINTINGS maker",prompt="Press OK to start :)")
    did_it_run_once = True
    #||||||||||||||
    picked_an_image = False
    set_extraction_amount = False
    #########
    image_name = ""
    colors_amount = 0
    #______________________________________________
    #______________________________________________
    start_code()

    ###############################_____________________________________________

    #___________________________________________________________________________
    my_screen.textinput(title="Loading...",prompt="READY! Press [ok] to start color-extraction")
    print("Loading... \n")
    while not IMAGE_FOUND:
        try:
            extraction_operation(image_name,colors_amount)
        except FileNotFoundError:
            print("Couldn't find the image :/, please make sure the image directory is correct, and file extension included")
            #
            my_screen.textinput(title="⚠️  ERROR", prompt="Error occured, press [ok] to restart")
            #RESET\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            print("\n" * 50)
            print("Loading... \n")
            #
            rest_values()
            #
            start_code()

    #___________________________________________________________________________
    #___________________________________________________________________________EXTRACTION ASSESSMENT (the situation is crazy/insane)
    #___________________________________________________________________________
    if IMAGE_FOUND:         #old statement: len(REFINED_colors_list) > 0:
        # DEBUG
        print("\n")
        # input("show results?")
        print("\n")
        # DEBUG
        #||||||||||||||
        print(REFINED_colors_list)
        #THEN LAUNCH A NEW FUNCTION HERE THAT START ASKING YOU FOR THE PAINTING DIMENSIONS (GRAPHICS! (GUI)) #IMPORTANT_POINT
        define_painting()
    else:
        print("<!>invalid file directory<!>\"again\"... no colors were extracted! :(")
        my_screen.textinput(title="⚠️  ERROR", prompt="Error occured, press [ok] to restart")
        # RESET\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        print("\n" * 50)
        print("Loading... \n")
        #
        rest_values()
        #
        start_code()
