import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ObjectPosition:
    def __init__(self):
        # wave's parameters
        self.c = 3e8
        self.landa = 3  
        self.wave_num = 2 * np.pi / self.landa
        self.omega = self.c * self.wave_num

    def data(self):
        # wave setting
        self.x_space = np.linspace(-10, 10, 500)
        self.t_space = np.linspace(0, 1e-8, 50)

        self.object_position = 2 
        self.boost = 3

        self.figur, self.axes = plt.subplots(figsize=(10, 5))
        self.axes.set_xlim(-10, 10)
        self.axes.set_ylim(-3, 3)

        self.wave, = self.axes.plot([], [], 'b', label="EM_wave")
        self.axes.axvline(self.object_position, color='r', linestyle='--', label="object_place")
        self.axes.legend()
        # when wave is boosted
        def boosting(x):
            return np.where(np.abs(x - self.object_position) < 1, self.boost, 1)
        # create moving wave
        def moving(t):
            wave_ = np.cos(self.wave_num * self.x_space - self.omega * t) * boosting(self.x_space)
    
            self.wave.set_data(self.x_space, wave_)
            return self.wave,
        self.ani = animation.FuncAnimation(self.figur, moving, frames=self.t_space, interval=50, blit=True)
        return plt.show()


ins = ObjectPosition()
print(ins.data())