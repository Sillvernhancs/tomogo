### for examples on how to use the libary:
Go to python > examples > epd_2in13_V4_test.python

for further documentation check out the "E-ink display documentation.pdf"

### Precausion When Using/Coding for the E ink display
1. <span style="color: red;">For E-paper displays that support partial refresh, please note that you cannot refresh them with the partial refresh mode all the time. After refreshing partially several times, you need to fully refresh EPD once. Otherwise, the display effect will be abnormal, which cannot be repaired!</span> 
   1. Maybe Partial Refresh 5-20 times before a full refresh(?)
2. <span style="color: red;">Note that the screen cannot be powered on for a long time. When the screen is not refreshed, please set the screen to sleep mode or power off it. Otherwise, the screen will remain in a high voltage state for a long time, which will damage the e-Paper and cannot be repaired!</span>
   1. Put the device on sleep mode after 5-20 minutes, When walking around, the device shouldn't have to display anything, if an encounter apeared, ping the player with the speaker first, once the user interact with the device in any capacity is when you start the screen again.
3. <span style="color: red;">When using the e-Paper display, it is recommended that the refresh interval is at least 180s, and refresh at least once every 24 hours. If the e-Paper is not used for a long time, you should use the program to clear the screen before storing it. (Refer to the datasheet for specific storage environment requirements.)</span>
   1. Clear the display on start up, and on shutdown, if the device stay on more than 23 hours, full refresh the device.
4. After the screen enters sleep mode, the sent image data will be ignored, and it can be refreshed normally only after initializing again.
5. Control the 0x3C or 0x50 (refer to the datasheet for details) register to adjust the border color. In the demo, you can adjust the Border Waveform Control register or VCOM AND DATA INTERVAL SETTING to set the border.
6. If you find that the created image data is displayed incorrectly on the screen, it is recommended to check whether the image size setting is correct, change the width and height settings of the image and try again.
7. The working voltage of the e-Paper display is 3.3V. If you buy the raw panel and you need to add a level convert circuit for compatibility with 5V voltage. The new version of the driver board (V2.1 and subsequent versions) has added a level processing circuit, which can support both 3.3V and 5V. The old version only supports a 3.3V working environment. You can confirm the version before using it. (The one with the 20-pin chip on the PCB is generally the new version.)
8. <span style="color: red;">The FPC cable of the screen is fragile, Please note: Do not bend the cable along the vertical direction of the screen to avoid tearing the cable; Do not repeatedly excessive bending line, to avoid line fracture; Do not bend the cable toward the front of the screen to prevent the cable from being disconnected from the panel. It is recommended to use fixed wiring during debugging and development.</span>
9.  <span style="color: red;">The screen of e-Paper is relatively fragile, please try to avoid dropping, bumping, and pressing hard.</span>
10. We recommend that customers use the sample program provided by us to test with the corresponding development board.