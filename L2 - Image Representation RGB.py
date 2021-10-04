# theCODEinitiative - Computational Thinking curriculum lesson 2: 
# Image Representation - Pixel RGB code accompaniment, by Michael Pennefather

# A code file that helps students understand how images are represented by numbers and allows
# them to experiment with a basic RGB color representation system.



# NOTE: This is a demo version of the functional .mkcd file, and is only intended for being viewed where the .mkcd cannot

# Minecraft: education edition's blocks<->python code conversion is useful but results in
# inflexible function/variable naming conventions and other strange design choices that I can't
# change.


def on_on_chat():
    global line0, line1, line2, line3, line4, line5, lists
    # make_a: on chat command "make_a", 
    # draw a lower-case a with the current picked color
    line0 = [0, 1, 1, 1, 0]
    line1 = [0, 0, 0, 0, 1]
    line2 = [0, 1, 1, 1, 1]
    line3 = [1, 0, 0, 0, 1]
    line4 = [1, 0, 0, 0, 1]
    line5 = [0, 1, 1, 1, 1]
    lists = [line5, line4, line3, line2, line1, line0]
    draw()
player.on_chat("make_a", on_on_chat)

def on_on_chat2(RedAMT, GreenAMT, BlueAMT):
    # pickColor command: on chat command "pickColor RedAMT(0,1) GreenAMT(0,1) BlueAMT(0,1)",
    # choose a basic color based on the "RGB" value given, where:
    # 0 represents a color value of 0 on a traditional RGB system,
    # and 1 represents a color value of 255. 
    
    # Colors are only available in values of 0 and 255 because of minecraft limitations - 
    # only a discrete palette we can use with set colors 
    

    #Valid RGB check: Boolean variables are not implemented in MC? So I had to do this
    if -1 >= RedAMT or RedAMT >= 2 or (-1 >= GreenAMT or GreenAMT >= 2) or (-1 >= BlueAMT or BlueAMT >= 2):
        player.say("Error: Please use either 1 or 0 for your color amounts!")

    # # (0,0,0) - Black
    if RedAMT == 0 and GreenAMT == 0 and BlueAMT == 0:
        agent.set_item(BLACK_WOOL, 5, 2)
        player.say("No colors (0,0,0) == Black selected!")
        
    elif RedAMT == 1 and GreenAMT == 1 and BlueAMT == 1:
        # # (1,1,1) - White
        agent.set_item(WOOL, 5, 2)
        player.say("All colors (1,1,1) == White selected!")

    elif RedAMT == 1 and GreenAMT == 0 and BlueAMT == 0:
        # # (1,0,0) - Red
        agent.set_item(RED_WOOL, 5, 2)
        player.say("Just red (1,0,0) == Red selected!")

    elif RedAMT == 1 and GreenAMT == 1 and BlueAMT == 0:
        # # (1,1,0) - Yellow
        agent.set_item(YELLOW_WOOL, 5, 2)
        player.say("Red and green (1,1,0) == Yellow selected!")

    elif RedAMT == 0 and GreenAMT == 1 and BlueAMT == 0:
        # # (0,1,0) - Green
        agent.set_item(GREEN_WOOL, 5, 2)
        player.say("Just green (0,1,0) == Green selected!")

    elif RedAMT == 0 and GreenAMT == 1 and BlueAMT == 1:
        # # (0,1,1) - Cyan ("Light blue" in minecraft)
        agent.set_item(LIGHT_BLUE_WOOL, 5, 2)
        player.say("Green and blue (0,1,1) == Cyan selected!")

    elif RedAMT == 0 and GreenAMT == 0 and BlueAMT == 1:
        # # (0,0,1) - Blue
        agent.set_item(BLUE_WOOL, 5, 2)
        player.say("Just blue (0,0,1) == Blue selected!")

    elif RedAMT == 1 and GreenAMT == 0 and BlueAMT == 1:
        # # (1,0,1) - Magenta
        agent.set_item(MAGENTA_WOOL, 5, 2)
        player.say("(1,0,1) == Magenta selected!")
player.on_chat("pickColor", on_on_chat2)

def on_on_chat3():
    global line0, line1, line2, line3, line4, line5, lists
    # make_b: on chat command "make_b", 
    # draw a lower-case b with the current picked color
    line0 = [1, 0, 0, 0, 0]
    line1 = [1, 0, 0, 0, 0]
    line2 = [1, 1, 1, 1, 0]
    line3 = [1, 0, 0, 0, 1]
    line4 = [1, 0, 0, 0, 1]
    line5 = [1, 1, 1, 1, 0]
    lists = [line5, line4, line3, line2, line1, line0]
    draw()
player.on_chat("make_b", on_on_chat3)

def on_on_chat4():
    # make_c: on chat command "make_c",
    # draw a lower-case c with the current picked color
    global line0, line1, line2, line3, line4, line5, lists
    line0 = [0, 1, 1, 1, 0]
    line1 = [1, 0, 0, 0, 0]
    line2 = [1, 0, 0, 0, 0]
    line3 = [1, 0, 0, 0, 0]
    line4 = [1, 0, 0, 0, 0]
    line5 = [0, 1, 1, 1, 0]
    lists = [line5, line4, line3, line2, line1, line0]
    draw()
player.on_chat("make_c", on_on_chat4)

def on_on_chat5():
    # draw() chat calling command: on chat command "draw",
    # repeat the last make_ command.
    draw()
player.on_chat("draw", on_on_chat5)

def draw():
    # using the current drawing array and color, draws a picture in 


    # inital agent setup: Teleports the agent to the player, then moves away from them
    agent.teleport_to_player()
    agent.move(FORWARD, 4)
    agent.move(UP, 1)
    agent.set_slot(1)
    agent.set_assist(PLACE_ON_MOVE, False)
    agent.set_assist(DESTROY_OBSTACLES, True)
    agent.set_item(WOOL, 5, 1)


    # loop over each array of the matrix, 0s correspond to slot 1 "unpainted" wool and 
    # 1s correspond to slot 2"painted" wool 
    # default is white wool in 1st slot (index 0) and black wool in 2nd slot(index 1)
    # use pickColor command to choose RGB wool color for slot 2
    for index in lists:
        for index2 in index:

            #arrays use 0 based indexing while agent slots use 1 based unfortunately
            # if index2 is a 0 then place slot 1 - otherwise place slot 2
            agent.move(FORWARD, 1)
            agent.set_slot(index2 + 1)
            agent.place(DOWN)

        #move the agent to the beginning of the next row
        agent.move(UP, 1)
        agent.turn(LEFT_TURN)
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, 5)
        agent.turn(LEFT_TURN)
        agent.turn(LEFT_TURN)



#unused blank canvas function
def makeBlank():
    global line0, line1, line2, line3, line4, line5, lists
    line0 = [0, 0, 0, 0, 0]
    line1 = [0, 0, 0, 0, 0]
    line2 = [0, 0, 0, 0, 0]
    line3 = [0, 0, 0, 0, 0]
    line4 = [0, 0, 0, 0, 0]
    line5 = [0, 0, 0, 0, 0]
    lists = [line5, line4, line3, line2, line1, line0]


# drawing array intialization - 
# lists is a list of all the lines, which is iterated by index in draw()
# the line_ lists are the rows of the matrix
lists: List[List[number]] = []
line5: List[number] = []
line4: List[number] = []
line3: List[number] = []
line2: List[number] = []
line1: List[number] = []
line0: List[number] = []
# default color set to black
agent.set_item(BLACK_WOOL, 5, 2)