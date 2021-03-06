#!/usr/bin/env python
"""
Use a pcolor or imshow with a custom colormap to make a contour plot.
A proper contour, with contour lines, is on the list of things to do
"""

from matplotlib.matlab import *


def bivariate_normal(X, Y, sigmax=1.0, sigmay=1.0,
                     mux=0.0, muy=0.0, sigmaxy=0.0):
    """
    Bivariate gaussan distribution for equal shape X, Y

    http://mathworld.wolfram.com/BivariateNormalDistribution.html
    """
    Xmu = X-mux
    Ymu = Y-muy

    rho = sigmaxy/(sigmax*sigmay)
    z = Xmu**2/sigmax**2 + Ymu**2/sigmay - 2*rho*Xmu*Ymu/(sigmax*sigmay)
    return 1.0/(2*pi*sigmax*sigmay*(1-rho**2)) * exp( -z/(2*(1-rho**2)))


delta = 0.01
x = arange(-3.0, 3.0, delta)
y = arange(-3.0, 3.0, delta)
X,Y = meshgrid(x, y)
Z1 = bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = bivariate_normal(X, Y, 1.5, 0.5, 1, 1)


cmap = ColormapJet(10)    # 10 discrete contours
im = imshow(Z2-Z1, cmap)  # difference of Gaussians

# set the interpolation method: 'nearest', 'bilinear', 'bicubic' and much more
im.set_interpolation('bilinear')

axis('off')
#savefig('test')
show()

