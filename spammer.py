
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")

print("===============================================================================")
print("HOW TO USE:")
print("1. Login to whatsapp web")
print("2. You have to enter chat name exactly as it is on your whatsapp, **chat shouldn't be archived**")
print("3. Input message you want to send to that chat")
print("4. Enter number of times you want to send that message")
print("===============================================================================")

inputElement = None
chat = None

chatName = input("Enter chat name: ")

def selectChat(chatName):
    chat = driver.find_element_by_xpath(f"//*[@title='{chatName}']")
    chat.click()

def sendSpam(chatName,message, repeat):
    selectChat(chatName)
    inputElement = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    for i in range(0, repeat):
        inputElement.send_keys(messageValue)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()


while True:
    messageValue = input("Enter message that you want to send: ")
    repeat = int(input("How many times? -Enter number- :"))

    sendSpam(chatName,messageValue, repeat)

    print("Input number as choice: ")
    choice = int(input("1. Spam this person more?\n2. Spam someone else\n3. Exit.\n===========\nInput:\t"))
    if choice == 1:
        continue
    elif choice == 2:
        chatName = input("Enter chat name: ")
        selectChat(chatName)
        continue
    else:
        break


        
