import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animate  
import nibabel as nib
import os

def mri2gif(nifti, filename):
    """Converts nii.gz into .gif"""
    images = []
    img = nib.load(img).get_fdata()

    fig = plt.figure()

    for i in range(len(img)):
        im = plt.imshow(img[i], animated=True, cmap='binary')
        images.append([im])

    ani = animate.ArtistAnimation(fig, images, interval=25,\
        blit=True, repeat_delay=500)
    plt.axis('off')
    ani.save(filename)