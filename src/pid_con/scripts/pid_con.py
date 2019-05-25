#!/usr/bin/python

import time
import rospy

class pid():
    def __init__(self, p=0.1, i=0.0, d=0.0):
        self.ref = 0 #reference command
        self.out = 0 #controller output
        self.kp = p #proportional gain
        self.ki = i #integral gain
        self.kd = d #derivative gain
        self.P = 0 #proportional propogation term
        self.I = 0 #integral propogation term
        self.D = 0 #derivative propogation term
        self.err = 0 #control error
        self.ts = 0.1 #sampling time
        self.t_now = time.time() #current time
        self.t_prev = self.t_now #previous time
        self.clear()

    #updates PID and error terms
    def update(self):

        return

    #resets PID and error terms
    def reset(self):
        self.ref = 0
        return

    #set proportional gain
    def set_kp(self, k):
        self.kp = k
        return

    #set integral gain
    def set_ki(self, k):
        self.ki = k
        return
    #set derivative gain
    def set_kd(self, k):
        self.kd = k
        return

    def main():
        print("Initializing node...")
        rospy.init_node('pid')
        return 0

if __name__ == '__main__':
    con = pid()
    con.main()
