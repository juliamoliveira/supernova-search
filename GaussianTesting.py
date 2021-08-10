from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from astropy.convolution import convolve, Gaussian2DKernel, Box2DKernel
from astropy.visualization import MinMaxInterval
from scipy.ndimage import gaussian_filter

hdu_splus = fits.open('iDR3.STRIPE82-0001.000148_359.515791_-1.407501-crop.fits')
hdu_sdss = fits.open('iDR3.STRIPE82-0001.000148_359.515791_-1.407501-rep.fits')


### SPLUS ###

fig = plt.figure()
fig.suptitle('SPLUS')
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Resampling
ax1.imshow(hdu_splus[0].data, origin='lower')
ax1.set_title('Resampled', fontsize=10)

# Normalization
max_splus = hdu_splus[0].data.max()
norm_splus = hdu_splus[0].data / max_splus
ax2.imshow(norm_splus, origin='lower')
ax2.set_title('Normalized', fontsize=10)

'''
# Gaussian
gauss_kernel = Gaussian2DKernel(2)
smoothed_data_gauss = convolve(hdu_splus[0].data, gauss_kernel)
ax3.imshow(smoothed_data_gauss, origin='lower')
ax3.set_title('Gaussian', fontsize=10)
plt.show()
'''

# Gaussian
interval1 = MinMaxInterval()
vmin1, vmax1 = interval1.get_limits(hdu_splus[0].data)
result1 = gaussian_filter(hdu_splus[0].data, sigma=5)
max_gauss1 = result1.max()
result1 = result1 / max_gauss1
ax3.imshow(result1, origin='lower')
ax3.set_title('Gaussian', fontsize=10)
plt.show()

print('\nSPLUS')
print('Original (min e max): ', hdu_splus[0].data.min(), hdu_splus[0].data.max())
print('Final (min e max): ', result1.min(), result1.max())
print('----------------------------------------------------')


### SDSS ###

fig = plt.figure()
fig.suptitle('SDSS')
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Resampling
ax1.imshow(hdu_sdss[0].data, origin='lower')
ax1.set_title('Resampled', fontsize=10)

# Normalization
max_norm = hdu_sdss[0].data.max()
norm_sdss = hdu_sdss[0].data / max_norm
ax2.imshow(norm_sdss, origin='lower')
ax2.set_title('Normalized', fontsize=10)

# Gaussian
interval2 = MinMaxInterval()
vmin2, vmax2 = interval2.get_limits(hdu_sdss[0].data)
result2 = gaussian_filter(hdu_sdss[0].data, sigma=5)
max_gauss2 = result2.max()
result2 = result2 / max_gauss2
ax3.imshow(result2, origin='lower')
ax3.set_title('Gaussian', fontsize=10)
plt.show()

print('\nSDSS')
print('Original (min e max): ', hdu_sdss[0].data.min(), hdu_sdss[0].data.max())
print('Final (min e max): ', result2.min(), result2.max())
print('----------------------------------------------------')


### RESIDUE ###

res = result1 - result2
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
im = ax.imshow(res, origin='lower')
fig.colorbar(im)
plt.title('Residue (SPLUS - SDSS)')
plt.show()

print('\nResidue (min e max): ', res.min(), res.max())
