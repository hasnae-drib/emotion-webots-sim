
from controller import Robot

# Initialisation du robot
robot = Robot()

# Récupération du moteur
motor = robot.getDevice("servo_motor")
motor.setPosition(0.0)

# Durée du pas de simulation
timestep = int(robot.getBasicTimeStep())

# Fonction pour définir la position du moteur selon l'émotion
def set_motor_position(emotion):
    if emotion == "happy":
        motor.setPosition(1.57)  # 90° en radians
    elif emotion == "sad":
        motor.setPosition(0.0)   # 0°
    elif emotion == "angry":
        motor.setPosition(3.14)  # 180° en radians
    elif emotion == "surprised":
        motor.setPosition(4.71)  # 270° en radians
    else:
        motor.setPosition(0.0)   # Position par défaut

# Boucle principale
while robot.step(timestep) != -1:
    # Pour l'instant, on utilise une émotion par défaut
    emotion = "happy"
    set_motor_position(emotion)
