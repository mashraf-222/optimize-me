import numpy as np
from scipy.ndimage import convolve


def manual_convolution_1d(signal: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    signal_len = len(signal)
    kernel_len = len(kernel)
    result_len = signal_len - kernel_len + 1
    result = np.zeros(result_len)
    for i in range(result_len):
        for j in range(kernel_len):
            result[i] += signal[i + j] * kernel[j]
    return result


def gaussian_blur(
    image: np.ndarray, kernel_size: int = 3, sigma: float = 1.0
) -> np.ndarray:
    k = kernel_size // 2
    y, x = np.ogrid[-k : k + 1, -k : k + 1]
    kernel = np.exp(-(x * x + y * y) / (2.0 * sigma * sigma))
    kernel = kernel / kernel.sum()
    height, width = image.shape[:2]
    channels = 1 if len(image.shape) == 2 else image.shape[2]
    output = np.zeros_like(image)
    mask = np.ones_like(image, dtype=np.float64)
    if channels == 1:
        conv_img = convolve(image.astype(np.float64), kernel, mode='constant', cval=0.0)
        conv_mask = convolve(mask, kernel, mode='constant', cval=0.0)
        np.divide(conv_img, conv_mask, out=output, where=conv_mask > 0)
    else:
        for c in range(channels):
            conv_img = convolve(image[:, :, c].astype(np.float64), kernel, mode='constant', cval=0.0)
            conv_mask = convolve(mask[:, :, c], kernel, mode='constant', cval=0.0)
            np.divide(conv_img, conv_mask, out=output[:, :, c], where=conv_mask > 0)
    return output
