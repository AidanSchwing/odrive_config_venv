from dpea_odrive.odrive_helpers import *
od = find_odrive()
ax = ODriveAxis(od.axis0)

dump_errors(od)

# axis0 and axis1 correspond to M0 and M1 on the ODrive
# You can also set the current limit and velocity limit when initializing the axis
ax = ODriveAxis(od.axis0, current_lim=10, vel_lim=10)

# Basic motor tuning, for more precise tuning,
# follow this guide: https://docs.odriverobotics.com/v/latest/control.html#tuning
ax.set_gains(5,0.2,0.1)

if not ax.is_calibrated():
    print("calibrating...")
    ax.calibrate()

ax.set_current_limit(100)

print("Current Limit: ", ax.get_current_limit())
print("Velocity Limit: ", ax.get_vel_limit())


#USING SIMPLE POSITION CONTROL
ax.set_vel_limit(20)

while 1:
    ax.set_pos(1)
    print("Current Position in Turns = ", round(ax.get_pos(), 2))
    sleep(1)
    ax.set_relative_pos(-1)
    print("Current Position in Turns = ", round(ax.get_pos(), 2))
    sleep(1)

