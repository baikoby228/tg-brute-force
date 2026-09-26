import time

from selenium.webdriver.common.bidi.browsing_context import PrintResult
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

BAD = "Нет"

def run_bruteforce(driver):
    try:
        input("==> После того как открыли нужный чат, нажмите ENTER здесь для старта... <==")
        time.sleep(1)

        print("\n[+] Подключаюсь к полю ввода по ID...")
        try:
            message_input = driver.find_element(By.CSS_SELECTOR, ".input-message-input")
            print("[+] Поле найдено! Начинаю отправку...")
        except Exception as e:
            print(f"[-] Ошибка: Поле ввода не найдено. Чат точно открыт? ({e})")
            return

        message_input.click()
        time.sleep(0.5)

        for i in range(200):
            code = f"{i:06d}"

            driver.execute_script("arguments[0].innerText = '';", message_input)
            driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", message_input)

            message_input.send_keys(code)
            message_input.send_keys(Keys.ENTER)

            time.sleep(0.1)

            if i % 10 == 0:
                try:
                    #messages = driver.find_elements(By.CSS_SELECTOR, "div.peer-color-3 div.content-inner div.text-content")
                    messages = driver.find_elements(By.CSS_SELECTOR, ".translatable-message")

                    last_messages = [msg.text for msg in messages[-250:]]

                    stop_found = False
                    print("sz =", len(last_messages))
                    for msg_text in last_messages:
                        if msg_text.lower() == '':
                            print('skip')
                            continue
                        #print("!!!")
                        if not BAD.lower() in msg_text.lower():
                            print("!", msg_text)
                            print(f"\n[★★★] УСПЕХ! Бот ответил: '{msg_text}'")
                            print(f"[★★★] Правильный код оказался: {code}")
                            stop_found = True
                            break
                        else:
                            print("! no ", msg_text)

                    if stop_found:
                        break

                except Exception as e:
                    pass

                print(f"[Прогресс] Отправлено: {code} ... ждем ответ")

        print("\n[+] Работа цикла завершена.")

    finally:
        print("[!] Оставляю браузер открытым на время для проверки...")
        time.sleep(100000)
        driver.quit()


if __name__ == "__main__":
    run_bruteforce()
