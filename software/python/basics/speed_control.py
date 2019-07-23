# speed_control.py takes target speeds and generates duty cycles
# to send to motors, and will perform PID control (when finalized)

import motors_ex1 as m
import numpy as np


# THE FOLLOWING FUNCTION PAIR IS FOR BOTH MAPPING AND DRIVING BY THETA & # X
# DO NOT USE THIS SECTION UNLESS INVERSE KINEMATICS IS BROKEN.
#----------------------------------------------------------------------------
# generate_duty is a placeholder function for the inverse kinematics program
def generate_duty(x_dot,theta_dot):
    # Calculate Left and Right Wheel Duty Cycles
    duty_r = ((  1 * (theta_dot)) + x_dot )
    duty_l = (( -1 * (theta_dot))  + x_dot )
    duties = np.array([ duty_l, duty_r ])   # put the values into an array
    duties[0] = sorted([-1, duties[0], 1])[1] # place bounds on duty cycle
    duties[1] = sorted([-1, duties[1], 1])[1] # place bounds on duty cycle
    return duties

def drive(x_dot, theta_dot):
    duties = generate_duty(x_dot, theta_dot)
    m.MotorL(duties[0]) # fcn allows -1 to 1
    m.MotorR(duties[1]) # fcn allows -1 to 1

# THE FOLLOWING FUNCTION PAIR IS FOR BOTH MAPPING AND DRIVING BY pdl & pdr targets
#----------------------------------------------------------------------------
# a function for converting target rotational speeds to PWMs without feedback
def openLoop(pdl,pdr):
    DRS = 0.8   # create a variable for direct-re-scaling
    duty_l = pdl * 1/9.75 * DRS  # 1 is max voltage and 9.75 is max rad/s possible
    duty_r = pdr * 1/9.75 * DRS  #
    duties = np.array([ duty_l, duty_r ])   # put the values into an array
    duties[0] = sorted([-1, duties[0], 1])[1] # place bounds on duty cycle
    duties[1] = sorted([-1, duties[1], 1])[1] # place bounds on duty cycle
    return duties

def driveOpenLoop(dutyl,dutyr):
    duties = openLoop(dutyl,dutyr)
    m.MotorL(duties[0])
    m.MotorR(duties[1])

# def driveClosedLoop()

#     #calculate the error 
#     e = targ_phi[0] - curr_phi[0]
#     print(targ_phi[0], ' ', curr_phi[0])
#     time.sleep(0.5)
#     #define e_max
#     #e_max = 0.4 #m/s
#     #define u_max
#     #u_max = 1.0 #duty
#     #calculate the kp value 
#     #kp = u_max/e_max #This five you a Kp of 2.5
#     #variable Kp 
#     kp = 0.5 
#     #multiply the k by the error to get U_poroportional 
#     u_proportional = e * kp 
#     #sort u_proportional equal to duty 
#     duty = u_proportional
#     duty = sorted([-1,duty,1])[1]
#     #send duty to m.MotorL 
#     m.MotorL(duty)
#     #send 0 to m.MotorR
#     m.MotorR(0)
