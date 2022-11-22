from robot_class import RobotControl
import rospy

class TurtleBotMaze():

# You can also define degrees using 1st approach as defined below
    #def __init__(self, degrees = 90):

        #self.rc = RobotControl()
        #self.degrees = degrees
# Or you can use the 2nd approach as defined below.

    def __init__(self, degrees, degrees2, motion, speed, time):

        self.rc = RobotControl()
        self.degrees = degrees
        self.degrees2 = degrees2
        self.motion = motion
        self.speed = speed
        self.time = time


    def move(self):

        self.rc.move_straight()

    def move_straight(self):

        self.rc.move_straight_time(self.motion, self.speed, self.time)

    def rotate(self):

        self.rc.rotate(self.degrees)

    def rotate2(self):

        self.rc.rotate(self.degrees2)

    def stop(self):

        self.rc.stop_robot()

    
    def turtlebot(self):

        i = self.rc.get_laser(360)

        while (i > 1): 

            self.move()
            i = self.rc.get_laser(360)
            print ("Current distance to wall: %f" % i)
            self.rc.stop_robot()

            if (i<1):

                self.rotate()
            

        self.rc.stop_robot()


        i = self.rc.get_laser(360)     #  360 is the front side of the laser mounted on the robot 

        while (i > 1): 

            self.move()
            i = self.rc.get_laser(360)
            print ("Current distance to wall: %f" % i)
            self.rc.stop_robot()

            if (i<1):

                self.rotate()
            

        self.rc.stop_robot()



        i = self.rc.get_laser(360)

        while (i > 1): 

            self.move()
            i = self.rc.get_laser(360)
            print ("Current distance to wall: %f" % i)
            self.rc.stop_robot()

            if (i < 1):

                self.rotate2()
        
        self.rc.stop_robot()

    def turtlebot2(self):

        self.move_straight()

# creating different instances of class TurtleBotMaze and calling different functions on it...

f1 = TurtleBotMaze(80, -93, "forward", 0.5, 5.0)
f1.turtlebot()   

f2 = TurtleBotMaze(80, -93, "forward", 0.5, 7.0)
f2.turtlebot2()

rospy.loginfo(" WOW, the robot has successfully come out of the maze.")
