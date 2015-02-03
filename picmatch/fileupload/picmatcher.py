# encoding: utf-8
import os
import glob
import re

from ssim.utils import get_gaussian_kernel
from ssim.ssimlib import SSIM

def picmatcher(pic_name):
    """pic_name -- Limit a text to 20 chars length, if necessary strips the
    middle of the text and substitute it for an ellipsis.

    Compares an image with a list of images using the SSIM metric.

    """
    match_dict = dict()
    match_res = list()

    PICTURE_DB = 'pictures/*'
    comparison_images = glob.glob(PICTURE_DB)

    gaussian_kernel_sigma = 1.5
    gaussian_kernel_width = 11
    gaussian_kernel_1d = get_gaussian_kernel(
        gaussian_kernel_width, gaussian_kernel_sigma)

    for comparison_image in comparison_images:
        ssim_value = SSIM(pic_name, gaussian_kernel_1d).ssim_value(
            comparison_image)
        match_dict[comparison_image] = ssim_value

    match_res = sorted(match_dict.items(), key=lambda d: d[1], reverse=True)[:10]
    
    return match_res

# if __name__ == '__main__':
#     picmatcher('pictures/申请表第1页.jpg')
