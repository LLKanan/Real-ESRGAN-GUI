from tkinter import*
from tkinter import filedialog
import os
import logging
import time
import inference_realesrgan_video as irv

def setInputFile(entry):
  logging.info("Requesting new input files")
  newDir = filedialog.askopenfilename()
  entry.delete(0,END)
  entry.insert(0,newDir)
  logging.info("Succesfully replaced input files")

def setDirectory(entry):
  logging.info("Requesting new output directory")
  newDir = filedialog.askdirectory()
  entry.delete(0,END)
  entry.insert(0,newDir)
  logging.info("Requesting new output directory")

def upScaleVideo(inputFile,outputDir,suffix,model,upscaleRatio,numProcess):
  logging.info("Generating command for upscale video")
  command = "python inference_realesrgan_video.py -i " + inputFile + " -o " + outputDir + " -n " + model + " -s " + upscaleRatio + " --suffix " + suffix + " --num_process_per_gpu " + numProcess
  logging.info("Command generated:" + command)
  logging.info("Running command")
  os.system(command)
  logging.info("Video upscale completed")
  print("Video upscale completed")

def main():
  logFile = "./logs/"+ str(int(time.time())) +".log"
  logging.basicConfig(filename= logFile, filemode='w', level=logging.DEBUG)
  logging.info("Setting CUDA devices")
  os.system("set CUDA_VISIBLE_DEVICES=0")
  logging.info("Successfully set CUDA devices")

  logging.info("Initialising GUI")
  root = Tk()

  #Left side labels
  header = Label(root, text="Anime Video Upscaling")
  inputLabel = Label(root, text="Input File:")
  outputLabel = Label(root, text="Output Directory:")
  suffixLabel = Label(root, text="Output file suffix:")
  modelLabel = Label(root, text="Model:")
  ratioLabel = Label(root, text="Upscale Ratio:")
  numProcessLabel = Label(root, text="Number of Processes per GPU:")

  #Right side entries
  inputEntry = Entry(width = 80)
  outputEntry = Entry(width = 80)
  suffixEntry = Entry(width = 80)
  modelEntry = Entry(width = 80)
  ratioEntry = Entry(width = 80)
  numProcessEntry = Entry(width = 80)

  #Default values for entries
  outputEntry.insert(END,"output/")
  suffixEntry.insert(END,"upscaled4x")
  modelEntry.insert(END,"realesr-animevideov3")
  ratioEntry.insert(END,"4")
  numProcessEntry.insert(END,"2")

  #Button
  runCommandButton = Button(root,text="Upscale Video",command=lambda : upScaleVideo(inputEntry.get(),outputEntry.get(),suffixEntry.get(),modelEntry.get(),ratioEntry.get(),numProcessEntry.get()))
  inputDirButton = Button(root,text="...",command=lambda : setInputFile(inputEntry))
  outputDirButton = Button(root,text="...",command=lambda : setDirectory(outputEntry))

  #Grid layout
  header.grid(row=0,column=1)

  #Grid Layout Labels
  inputLabel.grid(row=1,column=0)
  outputLabel.grid(row=2,column=0)
  suffixLabel.grid(row=3,column=0)
  modelLabel.grid(row=4,column=0)
  ratioLabel.grid(row=5,column=0)
  numProcessLabel.grid(row=6,column=0)

  #Grid layout entries
  inputEntry.grid(row=1,column=1)
  outputEntry.grid(row=2,column=1)
  suffixEntry.grid(row=3,column=1)
  modelEntry.grid(row=4,column=1)
  ratioEntry.grid(row=5,column=1)
  numProcessEntry.grid(row=6,column=1)

  #Grid Layout buttons
  inputDirButton.grid(row=1,column=2)
  outputDirButton.grid(row=2,column=2)
  runCommandButton.grid(row=7,column=1)
  logging.info("GUI successfully initialised")


  logging.info("Beginning mainloop")
  root.mainloop()

if __name__ == '__main__':
    main()