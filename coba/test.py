import control
import matplotlib.pyplot as plt

sistem = control.TransferFunction([1, 1], [1, 3, 2])
Kp, Ki, Kd = control.pidtune(sistem, 'ziegler-nichols')
PID = control.TransferFunction([Kd, Kp, Ki], [1, 0])
sistem_pid = control.feedback(sistem*PID, 1)
t, y = control.step_response(sistem_pid)

plt.plot(t, y)
plt.xlabel('Waktu (s)')
plt.ylabel('Output')
plt.title('Respon Sistem dengan PID')
plt.grid(True)
plt.show()

