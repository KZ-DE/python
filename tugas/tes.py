import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.last_error = 0
        self.integral = 0

    def calculate(self, setpoint, feedback):
        error = setpoint - feedback

        # Proportional term
        P = self.Kp * error

        # Integral term
        self.integral += error
        I = self.Ki * self.integral

        # Derivative term
        D = self.Kd * (error - self.last_error)
        self.last_error = error

        output = P + I + D
        return output


def simulate_system(pid, setpoint, duration):
    current_value = 0
    time = []
    values = []

    for t in range(duration):
        control_signal = pid.calculate(setpoint, current_value)
        current_value += control_signal

        time.append(t)
        values.append(current_value)

    return time, values


# Parameter PID
Kp = 200.0
Ki = 0
Kd = 0

# Inisialisasi PID Controller
pid = PIDController(Kp, Ki, Kd)

# Simulasi sistem dengan kontrol PID
setpoint = 5000
duration = 1000
time, values = simulate_system(pid, setpoint, duration)

# Menampilkan diagram respons sistem
plt.plot(time, values)
plt.xlabel('Time')
plt.ylabel('System Value')
plt.title('PID Control System Response')
plt.grid(True)
plt.show()
