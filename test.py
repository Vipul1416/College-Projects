import numpy as np
import cv2
import base64
import requests

import DetectChars
import DetectPlates
import PossiblePlate

# module level variables ##########################################################################
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

showSteps = False

###################################################################################################

showSteps = False
regions = ['in']

def main():
    
    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()

    if blnKNNTrainingSuccessful == False:                               # if KNN training was not successful
        print("\nerror: KNN traning was not successful\n")

    cap = cv2.VideoCapture(0)

    #SECRET_KEY='sk_07e6b63f9e5c2fa6c843b7bb'
    
    while(True):
        # Capture frame-by-frame
        
        ret, frame = cap.read()
        if(ret==True):
            cv2.imshow('frame',frame)
            
            listOfPossiblePlates = DetectPlates.detectPlatesInScene(frame)           # detect plates
    
            listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)
            
            if len(listOfPossiblePlates) == 0:                          # if no plates were found
                print("\nno number plate found\n")
            else:
                
                listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
                licPlate = listOfPossiblePlates[0]

                cv2.imshow("imgPlate", licPlate.imgPlate)           # show crop of plate and threshold of plate
                #cv2.imshow("imgThresh", licPlate.imgThresh)
                
                if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
                    print("\nno characters were detected\n\n")
                else:
                    
                    drawRedRectangleAroundPlate(frame, licPlate)
                    #print("\nlicense plate read from image = " + licPlate.strChars + "\n")
                    cv2.imshow('found',frame)
                    
                    retval, buffer = cv2.imencode('.jpg', frame)
                    jpg_as_text = base64.b64encode(buffer)
                    
                    #url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=ind&secret_key=%s' % (SECRET_KEY)  #Replace 'ind' with  your country code
                    url = 'https://api.platerecognizer.com/v1/plate-reader/'
                    #data = dict(regions=regions)
                    files = dict(upload=jpg_as_text)
                    #headers = {'Authorization': 'Token 977a5e289923a513c1397c9194842956608ef444'}
                    #r = requests.post(url, data = jpg_as_text)
                    try:
                        r = requests.post(url,files,{'regions':'in'},headers={'Authorization': 'Token 977a5e289923a513c1397c9194842956608ef444'})
                        print(r.json()['results'][0]['plate'])
                        
                    except:
                        print("No number plate found")
                
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        else:
            print('No video')
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):

    p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)            # get 4 vertices of rotated rect

    cv2.line(imgOriginalScene, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)         # draw 4 red lines
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)
if __name__ == "__main__":
    main()
