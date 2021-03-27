import webbrowser
import time
import pyautogui

count = 0
with open("contacts.txt", "r") as contact_list:
	for index, contact in enumerate(contact_list.readlines(), start=1):
		with open("messages.txt", "r") as message:
			contact = contact.replace("\n", "")
			message = message.read()
			webbrowser.open(f"https://web.whatsapp.com/send?phone={contact}&text={message}&app_absent=0")
			time.sleep(10)
			pyautogui.click()
			pyautogui.press("enter")
			time.sleep(3)
			if count:
				pyautogui.hotkey("ctrl", "shift", "tab")
				pyautogui.hotkey("ctrl", "w")
			time.sleep(5)
			print(f"{contact}:{index} has been sent messages")
			count += 1
