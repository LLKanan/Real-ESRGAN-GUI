# Real-ESRGAN-GUI
A GUI for the image upscaling model [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)
This was designed specifically for videos, but can be used for images.
![image](https://user-images.githubusercontent.com/54023991/226312548-a35cfbe7-0279-4676-bb1e-30649b3da393.png)


## Requirements
 - Python >= 3.7 (Recommend to use Anaconda or Miniconda)
 - PyTorch >= 1.7
 - [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN#installation)
 - FFMPEG, you must also set the PATH value for FFMPEG, you also need to install the PIP module for FFMPEG
 - Make sure you can run FFMPEG in terminal/powershell and inference_realesrgan_video.py

##Installation and how to use
 - Place anime-upscaler.py file inside the /Real-ESRGAN directory (This directory should also contain inference_realesrgan_video.py)
 - Run "python anime-upscaler.py"

## Inputs
 - Input File: Directory of the image/video you're trying to upscale
 - Ouptut Directory: Directory of where you want the image/video to be saved
 - Output file suffix: Suffix added to the end of the output file
 - Model: Allows you to specify the Real-ESRGAN model you want to use, you can view them here [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN). By default I have it set to realesr-animevideov3, which I personally have seen the best results from
 - Upscale Ratio: Valid values are 2,3,4. By default, I've set this to 4 however I advise against doing this unless your computer is really fast. For reference a 25 minute video takes around 5 hours to upscale to 4x on an RTX 4080 + Ryzen 5 5600.
 - Num of Processes per GPU: Number of processes to run per GPU, if you don't know what this setting does I recommend just leaving it as is.
