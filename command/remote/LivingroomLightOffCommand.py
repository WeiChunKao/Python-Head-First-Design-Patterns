from Command import Command
from Light import Light


class LivingroomLightOffCommand(Command):
    light: Light
        
    def __init__(self, light: Light):
        self.light = light
        
    def execute(self) -> None:
        self.light.off()