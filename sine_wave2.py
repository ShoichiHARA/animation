import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

test  = True
black = (0, 0, 0)
gray  = (0.3, 0.3, 0.3)
white = (1, 1, 1)
red   = (1, 0, 0)
green = (0, 1, 0)
blue  = (0, 0, 1)


class SineWave:
	def __init__(self, f, y_max, phi, label="", color=black):
		self.f      = f      # 周波数
		self.t      = 1 / f  # 周期
		self.y_max  = y_max  # 振幅
		self.phi    = phi    # 初期位相
		self.label  = label  # 波形の名前
		self.color  = color  # 波形の色
		self.x_data = []     # 波形のx座標群
		self.y_data = []     # 波形のy座標群
		return

	def add_data(self, x, y):
		self.x_data.append(x)
		self.y_data.append(y)
		return


def circle(r):
	x = []
	y = []
	phi = 0
	while phi <= 2 * np.pi:
		x.append(r * np.cos(phi))
		y.append(r * np.sin(phi))
		phi += 0.02
	return x, y


def sinewave_anim(sinewaves):
	ps = []  # 円群
	ts = []  # 波形の周期群
	ys = []  # 波形の振幅群
	for i in range(len(sinewaves)):
		if not sinewaves[i].y_max in ys:
			px, py = circle(sinewaves[i].y_max)
			ps.append([px, py])
		ts.append(sinewaves[i].t)
		ys.append(sinewaves[i].y_max)
	t_max = max(ts)  # 波形の周期最大値
	y_max = max(ys)  # 波形の振幅最大値

	fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
	axes[0].set_xlim(-1.1*y_max, 1.1*y_max)
	axes[0].set_ylim(-1.1*y_max, 1.1*y_max)
	axes[0].set_aspect("equal")
	axes[0].set_xlabel("X")
	axes[0].set_ylabel("Y")
	axes[1].set_xlim(0, t_max)
	axes[1].set_ylim(-1.1*y_max, 1.1*y_max)
	axes[1].set_xlabel("t [ms]")
	axes[1].set_ylabel("v [V]")
	for i in range(len(ps)):
		axes[0].plot(ps[i][0], ps[i][1], linestyle=":", color=gray)

	artists = []  # アニメーションの画像群
	frame = 0  # 画像のフレーム
	frame_max = 400  # フレームの最大値
	while frame <= frame_max:
		artist = []  # 画像の要素群
		for i in range(len(sinewaves)):
			t = t_max * frame / frame_max
			x = sinewaves[i].y_max * np.cos(2 * np.pi * sinewaves[i].f * t + sinewaves[i].phi)
			y = sinewaves[i].y_max * np.sin(2 * np.pi * sinewaves[i].f * t + sinewaves[i].phi)
			sinewaves[i].add_data(t, y)
			artist.extend(axes[0].plot([0, x], [0, y], marker="o", linestyle="-", color=sinewaves[i].color))
			artist.append(axes[0].text(x*1.1, y*1.1, sinewaves[i].label, size="large", color=black))
			artist.extend(axes[1].plot(sinewaves[i].x_data, sinewaves[i].y_data, color=sinewaves[i].color))
			artist.extend(axes[1].plot(t, y, marker="o", color=sinewaves[i].color))
			artist.append(axes[1].text(t, y*1.1, sinewaves[i].label, size="large", color=black))
		artists.append(artist)
		frame += 1
	anim = ArtistAnimation(fig, artists, interval=10)
	plt.show()
	anim.save("sinewaveanim.gif", writer="pillow", fps=50)
	plt.close()
	return


if __name__ == "__main__":
	v1 = SineWave(0.05, 141, 0, label="v1", color=red)
	v2 = SineWave(0.05, 141, -np.pi*2/3, label="v2", color=green)
	v3 = SineWave(0.05, 141, np.pi*2/3, label="v3", color=blue)
	sinewave_anim([v1, v2, v3])
