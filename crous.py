import time
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox
from pydub import AudioSegment
from pydub.playback import play
import smtplib
import ssl

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


def sendEmail(receiverEmail):
    port = 465
    sender = "retinaenima@gmail.com"
    password = "retina@2007+dz"
    # recieve = str(input('To: '))
    recieve = receiverEmail
    # message = str(input('Message: '))
    message = "Chambre Disponible"
    context = ssl.create_default_context()
    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)
    print("sent email!")

def main():
    while True:
        try:
            PATH = "./driver/geckodriver"
            browser = Firefox(executable_path=PATH)
            # baseUrl = 'https://trouverunlogement.lescrous.fr/tools/residual/20/search?bounds=-10.1585_58.2114_14.6016_31.3674&page=1&price=60000' #FRANCE
            # baseUrl = "https://trouverunlogement.lescrous.fr/tools/residual/20/search?bounds=3.6386_49.4074_4.4926_49.0688&page=1&price=60000" #REIMS
            baseUrl = "https://trouverunlogement.lescrous.fr/tools/residual/20/search?bounds=3.9751_49.3291_4.1401_49.1783&page=1&price=60000" # REIMS 51100
            browser.get(baseUrl)
            resultListId = "SearchResultsList"
            while (True):
                time.sleep(20)
                resulListElement = browser.find_element_by_id(resultListId)
                liListElements = resulListElement.find_elements_by_xpath("./li")
                if len(liListElements) > 0:
                    print("Chambre disponible : ", end='')
                    print("Current Time =", current_time)
                    song = AudioSegment.from_mp3("audio.mp3")
                    play(song)
                    # sendEmail("animer.hichame@gmail.com")
                # elif len(liListElements) == 0:

                    # print("Chambre indisponible")
                time.sleep(60)
                browser.refresh();
        except Exception as e:
            print(e)
            # browser.close()


if __name__ == '__main__':
    main()