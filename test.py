#! python3
#Synxis Automation 6/25/2020
import pyautogui, sys, time
print('Press Ctrl-C to quit.')
def main():
    try:
      pyautogui.FAILSAFE = False
      pyautogui.click(x=1879, y=216)
  
      time.sleep(5)

      pyautogui.click(x=739, y=585)
      
      print("getrrrrrrrrrrrrrrrrrr")
      time.sleep(3)
      #input room
      pyautogui.write('NK1', interval=0.25) 
      pyautogui.press('tab', presses=1)
      pyautogui.write('LT02', interval=0.25) 
      pyautogui.press('tab', presses=4)
      pyautogui.write('CO', interval=0.25)
      pyautogui.press('tab', presses=1)
      pyautogui.write('CO', interval=0.25)
      time.sleep(1)
      pyautogui.click(x=1212, y=822)
      
      
      #enter name or wyndham number, need to implement a better soultion
      #maybe get a list of all vip members and copy folio
      pyautogui.write('Mark Mcnally', interval=0.25)
      pyautogui.press('enter', presses=1)
      
      #Instead of time.sleep maybe wait until screen sees dialog box

      time.sleep(40)
      print("ready to check in")
      pyautogui.click(x=1305, y=811)
      print("final screen")
      #Last
      time.sleep(5)
      pyautogui.click(x=375, y=327)
      pyautogui.write('DR', interval=0.25)
      pyautogui.press('tab', presses=1)
      time.sleep(1)
      pyautogui.press('enter', presses=1)
      time.sleep(2)

      pyautogui.click(x=1114, y=346)
      
      time.sleep(1)
      pyautogui.write('*nor', interval=0.25)
      pyautogui.press('tab', presses=1)

      time.sleep(1)
      pyautogui.click(x=93, y=506)
      time.sleep(0.5)
      pyautogui.click(x=748, y=453)
      pyautogui.click(x=1054, y=664)
      time.sleep(1)
      pyautogui.click(x=1864, y=344)
      time.sleep(1)
      pyautogui.press('enter', presses=1)

      
      #x, y = pyautogui.position()
      
    
    except Exception as e:
      print("error", e)
      sys.exit()
main()
