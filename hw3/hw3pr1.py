# imports 
import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# # Simple plot from matplotlib tutorial
# X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
# C,S = np.cos(X), np.sin(X)
# plt.plot(X,C)
# plt.plot(X,S)

# plt.show()

# # Create a new figure of size 8x6 points, using 100 dots per inch
# plt.figure(figsize=(8,6), dpi=80)
# # Create a new subplot from a grid of 1x1
# plt.subplot(111)
# X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
# C,S = np.cos(X), np.sin(X)
# # Plot cosine using blue color with a continuous line of width 1 (pixels)
# plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
# # Plot sine using green color with a continuous line of width 1 (pixels)
# plt.plot(X, S, color="red", linewidth=1.0, linestyle="-")
# # Set x limits
# plt.xlim(X.min()*1.1, X.max()*1.1)
# # Set x ticks
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
#        [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# # Set y limits
# plt.ylim(C.min()*1.1, C.max()*1.1)
# # Set y ticks
# plt.yticks([-1, 0, +1],
#        [r'$-1$', r'$0$', r'$+1$'])
# # Save figure using 72 dots per inch
# # savefig("../figures/exercice_2.png",dpi=72)
# # Show result on screen

# # Add spines
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data',0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data',0))

# # Add legends
# plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
# plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")

# plt.legend(loc='upper left', frameon=False)

# # Add some points
# t = 2*np.pi/3
# plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
# plt.scatter([t,],[np.cos(t),], 50, color ='blue')

# plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
#              xy=(t, np.sin(t)), xycoords='data',
#              xytext=(+10, +30), textcoords='offset points', fontsize=16,
#              arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
# plt.scatter([t,],[np.sin(t),], 50, color ='red')

# plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
#              xy=(t, np.cos(t)), xycoords='data',
#              xytext=(-90, -50), textcoords='offset points', fontsize=16,
#              arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#  # # see both data and labels
# for label in ax.get_xticklabels() + ax.get_yticklabels():
#     label.set_fontsize(16)
#     label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
# plt.show()

#  # Animation
# # Create new Figure and an Axes which fills it.
# fig = plt.figure(figsize=(7, 7))
# ax = fig.add_axes([0, 0, 1, 1], frameon=False)
# ax.set_xlim(0, 1), ax.set_xticks([])
# ax.set_ylim(0, 1), ax.set_yticks([])

# # Create rain data
# n_drops = 50
# rain_drops = np.zeros(n_drops, dtype=[('position', float, 2),
#                                       ('size',     float, 1),
#                                       ('growth',   float, 1),
#                                       ('color',    float, 4)])

# # Initialize the raindrops in random positions and with
# # random growth rates.
# rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
# rain_drops['growth'] = np.random.uniform(50, 200, n_drops)

# # Construct the scatter which we will update during animation
# # as the raindrops develop.
# scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
#                   s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
#                   facecolors='none')
# def update(frame_number):
#     # Get an index which we can use to re-spawn the oldest raindrop.
#     current_index = frame_number % n_drops

#     # Make all colors more transparent as time progresses.
#     rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
#     rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

#     # Make all circles bigger.
#     rain_drops['size'] += rain_drops['growth']

#     # Pick a new position for oldest rain drop, resetting its size,
#     # color and growth factor.
#     rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
#     rain_drops['size'][current_index] = 5
#     rain_drops['color'][current_index] = (0, 0, 0, 1)
#     rain_drops['growth'][current_index] = np.random.uniform(50, 200)

#     # Update the scatter collection, with the new colors, sizes and positions.
#     scat.set_edgecolors(rain_drops['color'])
#     scat.set_sizes(rain_drops['size'])
#     scat.set_offsets(rain_drops['position'])


# # Construct the animation, using the update function as the animation
# # director.
# animation = FuncAnimation(fig, update, interval=10)
# plt.show()

# # Scatter Plot
# n = 42
# fig = plt.figure()
# # Generate coordinates
# X = np.random.normal(0,1,n)
# Y = np.random.normal(0,1,n)
# # Generate colors
# colors = np.random.rand(n)
# area = np.pi * (15 * np.random.rand(n)) ** 2
# plt.scatter(X,Y, s= area, c= colors)
# fig.suptitle('Scatter Plot with Random Colors and Areas', fontsize=16, fontweight='bold')

# plt.show()

# # Bar Plot
# n = 12
# X = np.arange(n)
# fig = plt.figure()
# Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
# Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

# plt.bar(X, +Y1, facecolor='#ff91af', edgecolor='white')
# plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# for x,y in zip(X,Y1):
#     plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')
# for x1,y1 in zip(X,Y2):
#     plt.text(x1+0.4, -y1-0.09, '%.2f' % -y1, ha='center', va= 'bottom')

# fig.suptitle('Bar Plot', fontsize=16, fontweight='bold')
# plt.ylim(-1.25,+1.25)
# plt.show()

# Choice Plot

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
fig = plt.figure()
X,Y = np.meshgrid(x,y)

plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
fig.suptitle('Contour Plot with Label', fontsize=16, fontweight='bold')
plt.clabel(C, inline=1, fontsize=10)
plt.show()