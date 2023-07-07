class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.error_previous = 0
        self.integral = 0

    def calculate(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.error_previous) / dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.error_previous = error
        return output

# Inisialisasi PID Controller
pid = PID(Kp=0.5, Ki=0.2, Kd=0.1)

# Setpoint dan variabel pengukuran
setpoint = 50
variable = 20
waktu = 100

# Loop kontrol
for _ in range(100):
    # Menghitung error
    error = setpoint - variable
    
    # Menghitung output kontrol
    output = pid.calculate(error, dt= waktu)
    
    # Mengupdate variabel pengukuran (misalnya simulasi sistem)
    variable += output
    
    # Menampilkan hasil
    print("Error:", error, "Output:", output, "Variable:", variable)
