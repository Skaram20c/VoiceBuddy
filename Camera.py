#from picamera import PiCamera
#from Speak import speak
#import main as m
#from time import sleep

#camera = PiCamera()

#def cameraMode():
#        while True:
#                speak("Please Select Camera Setup")
#                print("Select Camera Setup: Take photo \t Record video \t Quit\n")
#                query = m.parseCommand().lower()
#                if "take" and "photo" in query:
#                        filename = input("Enter filename for the photo: ")
#                        speak("Please say or enter the filename")
#                        camera.start_preview()
#                        sleep(5)
#                        speak("taking a photo")
#                        camera.capture(f'/home/skaram/Pictures/{filename}.jpg') 
#                        camera.stop_preview()
#                        speak("Your photo saved")
#                        print("Photo saved as", filename)
#                elif "record" and "video" in query:
#                        speak("enter name for your video")
#                        filename = input("Enter filename for the video: ")
#                        duration = int(input("Enter duration of the video (in seconds): "))
#                        camera.start_preview()
#                        camera.start_recording(f'/home/skaram/Videos/{filename}.h264')
#                        sleep(duration)
#                        camera.stop_recording()
#                        camera.stop_preview()
#                        speak("Your video saved as")
#                        print("Video saved as", filename)
#                elif "quit" in query:
#                        break
#                else:
#                        print("Invalid choice, please try again")

