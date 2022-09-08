
# Camera Mouse

    I have made this software to improve myself at image processing. By doing that, 
    I learnt some other libraries and tecniques to make the software run faster.



## Used Libraries

    pyautogui   - Used for getting computer's resolution
    cv2         - Used for image processing
    mediapipe   - Used for hand recognition
    time        - Used for FPS calculation
    math        - Used for mathematical calculations
    numpy       - Used for matrix operations
    mouse       - Used for mouse control

## How to Use

    After running, camera capture will open. There will be a selected rectangular area. 
    That area is the movement area.
    Preffered hand size is 2/3 of the movement area.
    Captured image is flipped, using right hand is preffered.

    # To Move:              Stick index finger to middle finger and move hand in the ractangular area. 
                            If fingers are seperated, mouse will not move.
![mousemove](https://user-images.githubusercontent.com/104989834/188672203-5e020b15-3faa-4da8-a6d0-3b6347e58f4f.gif)

    # To Left Click:        Touch thumb with ring finger.
![mouseleftclick](https://user-images.githubusercontent.com/104989834/188672263-6d8f53b0-899b-4505-95cb-246c6b05fb72.gif)
    
    # To Right Click:       Touch thumb with pinky.
![mouserightclick](https://user-images.githubusercontent.com/104989834/188673128-618250a6-3262-4c84-b3d6-7042fd0445d3.gif)

    # To Double Click:      Stick pinky finger's fingertip to ring finger's fingertip and touch thumb.
![mousedoubleclick](https://user-images.githubusercontent.com/104989834/188674123-156ea700-d28e-418c-8000-4d0c0749ec19.gif)

    # To Hold:              Stick index finger to middle finger and stick to thumb. To move, move hand.
![hold](https://user-images.githubusercontent.com/104989834/188679632-eae64cce-a99d-4f45-a488-89dca73efbee.gif)

    # To Scroll:            Stick four fingers except thumb. Close or open hand to do scroll.
                            When hand is open, it will scroll up. Close hand to scroll down.
![scroll](https://user-images.githubusercontent.com/104989834/188675813-91355116-f9ad-459e-bfce-747767c09772.gif)

## How It's Made

    Capture image from camera.
    
    Image resolution updated according to screen resolution.
    
    Movement area selected.

    Using Mediapipe, hand points detected. 
 
    From detected hand points, necessary points selected. (4,8,10,11,12,15,16,20)
    
    Distance between some points measured.
    
    Using distances, combinations detected.
    
    Using combinations, events done.

![image](https://user-images.githubusercontent.com/104989834/188865875-1b7d781e-d64f-418a-8b48-8d07b905dd04.png)

## What I Learnt

    Instead of for loops, vectorize a function and use it throught the numpy array.
   (lms1 is vectorized | lms2 is for looped)
![optimization](https://user-images.githubusercontent.com/104989834/188869146-4a1af636-ff03-4b90-b6f8-348ef5e15ff2.png)

     Instead of pyautogui library, use mouse library for faster proccess. (Makes 2-3 fps difference)



