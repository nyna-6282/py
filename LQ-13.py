import matplotlib.pyplot as plt
import numpy as np
def plot_curves():
    x=np.linspace(-10,10,400)
    sin_curve=np.sin(x)
    cos_curve=np.cos(x)
    poly_curve=x**3-4*x**2+x+6
    exp_curve=np.exp(x)

    #sine
    plt.subplot(2,2,1)
    plt.plot(x,sin_curve,color='green')
    plt.title('SINE CURVE',color='red')
    plt.grid(True)

    #cosine
    plt.subplot(2,2,2,)
    plt.plot(x,cos_curve,color='blue')
    plt.title('COSINE CURVE',color='red')
    plt.grid(True)

    #polynomial
    plt.subplot(2,2,3)
    plt.plot(x,poly_curve,color='orange')
    plt.title('POLYNOMIAL CURVE',color='red')
    plt.grid(True)

    #exponential curve
    plt.subplot(2,2,4)
    plt.plot(x,exp_curve,color='aqua')
    plt.title('EXPONENTIAL CURVE',color='red')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
plot_curves()
