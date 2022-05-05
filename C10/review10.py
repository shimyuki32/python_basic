class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class Smartphone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()
    def does(self):
        return """I have many attachments:
    My laser, to {}.
    My claw to {}.
    My smartphone to {}""".format(
        self.laser.does(),
        self.claw.does(),
        self.smartphone.does()
    )
robbie = Robot()
print(robbie.does())