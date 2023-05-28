import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

test = False


# 正弦波生成クラス
class SineWave:
    p_x = 0
    p_t = 0
    f = 0
    y_max = 0
    phi = 0
    x_data = []
    y_data = []

    def __init__(self, f, y_max, phi):
        self.f = f
        self.y_max = y_max
        self.phi = phi
        self.clear()
        return

    def clear(self):
        self.x_data.clear()
        self.y_data.clear()

    def sine(self, x):
        y = self.y_max * np.sin(2 * np.pi * self.f * x + self.phi)
        return y
    
    def wave(self, p_x, x_max):
        self.p_x = p_x
        x = 0
        while x <= x_max:
            y = self.sine(x)
            self.x_data.append(x)
            self.y_data.append(y)
            x += p_x
        return

    """
    def graph(self):
        fig, ax = plt.subplots(1, 1, figsize=(8, 5))
        ax.set_xlim(min(self.x_data), max(self.x_data))
        ax.set_ylim(1.1 * min(self.y_data), 1.1 * max(self.y_data))
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        art = ax.plot(self.x_data, self.y_data, color=(1, 0, 0))
        # plt.show()
        return art

    def animation(self, p_x, x_max, p_t, t_max):
        self.p_x = p_x
        self.p_t = p_t
        t = 0
        while t < t_max:
            self.wave(p_x, x_max)
            artist = self.graph()
            self.clear()
            t += p_t
            self.phi += 2 * np.pi * self.f * p_t
            self.artists.append(artist)
        return
    """


def circle(r):
    x = []
    y = []
    phi = 0
    while phi <= 2 * np.pi:
        x.append(r * np.sin(phi))
        y.append(r * np.cos(phi))
        phi += 0.02
    return x, y

        
if __name__ == "__main__":
    sin1 = SineWave(1/(2*np.pi), 1, 0)
    sin2 = SineWave(1/(2*np.pi), 0.6, -np.pi/2)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    axes[0].set_xlim(-1.1, 1.1)
    axes[0].set_ylim(-1.1, 1.1)
    axes[0].set_aspect("equal")
    axes[0].set_xlabel("X")
    axes[0].set_ylabel("y")
    axes[1].set_xlim(0, 6.3)
    axes[1].set_ylim(-1.1, 1.1)
    axes[1].set_xlabel("ω [rad]")
    axes[1].set_ylabel("v [V], i [A]")
    px, py = circle(1)
    axes[0].plot(px, py, linestyle=":", color=(0.2, 0.2, 0.2))
    px, py = circle(0.6)
    axes[0].plot(px, py, linestyle=":", color=(0.2, 0.2, 0.2))

    artists = []
    t = 0
    v = [[], []]
    i = [[], []]
    while t <= 6.28:
        artist = []
        i_x = np.cos(t)
        i_y = np.sin(t)
        i[0].append(t)
        i[1].append(i_y)
        artist.extend(axes[0].plot([0, i_x], [0, i_y], marker="o", linestyle="-", color=(0, 0, 1)))
        artist.append(axes[0].text(i_x*1.1, i_y*1.1, "i_R", size="large", color=(0, 0, 0)))
        artist.extend(axes[1].plot(i[0], i[1], color=(0, 0, 1)))
        artist.extend(axes[1].plot(i[0][-1], i[1][-1], marker="o", color=(0, 0, 1)))
        artist.append(axes[1].text(i[0][-1], i[1][-1], "  i_R", size="large", color=(0, 0, 0)))
        v_x = 0.6 * np.cos(t)
        v_y = 0.6 * np.sin(t)
        v[0].append(t)
        v[1].append(v_y)
        artist.extend(axes[0].plot([0, v_x], [0, v_y], marker="o", linestyle="-", color=(1, 0, 0)))
        artist.append(axes[0].text(v_x*1.2, v_y*1.2, "v", size="large", color=(0, 0, 0)))
        artist.extend(axes[1].plot(v[0], v[1], color=(1, 0, 0)))
        artist.extend(axes[1].plot(v[0][-1], v[1][-1], marker="o", color=(1, 0, 0)))
        artist.append(axes[1].text(v[0][-1], v[1][-1], "  v", size="large", color=(0, 0, 0)))
        # artist.append(plt.legend(["電流", "電圧"]))
        t += 0.04
        artists.append(artist)
    # axes[1].legend(["電流", "電圧"])
    anim = ArtistAnimation(fig, artists, interval=50)
    plt.show()
    anim.save("sine_wave01.gif", writer="pillow", fps=50)
    plt.close()
