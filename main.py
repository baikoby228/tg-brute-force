import undetected_chromedriver as uc
import time
import os

from bruteforce import run_bruteforce

def main():
    profile_dir = os.path.abspath("telegram_profile")

    options = uc.ChromeOptions()
    options.add_argument(f'--user-data-dir={profile_dir}')

    options.add_argument('--start-maximized')

    options.add_argument('--no-first-run')
    options.add_argument('--no-service-autorun')
    options.add_argument('--password-store=basic')
    options.add_argument('--disable-popup-blocking')

    print(f"[*] Запуск браузера. Профиль сохраняется в: {profile_dir}")

    #driver = uc.Chrome(options=options, version_main=152)
    driver = uc.Chrome(options=options)

    driver.maximize_window()

    try:
        print("[*] Открываем Telegram Web...")
        driver.get("https://web.telegram.org/")

        print("\n" + "=" * 50)
        print("[ИНСТРУКЦИЯ]")
        print("1. Если это ПЕРВЫЙ запуск: авторизуйтесь в Telegram (по QR или номеру).")
        print("2. При СЛЕДУЮЩИХ запусках сессия загрузится автоматически.")
        print("3. Чтобы закрыть скрипт и браузер, нажмите Ctrl+C в этой консоли.")
        print("=" * 50 + "\n")

        while True:
            run_bruteforce(driver)
            time.sleep(100000)

    except KeyboardInterrupt:
        print("\n[*] Получен сигнал на завершение (Ctrl+C). Закрываем браузер...")
    except Exception as e:
        print(f"\n[!] Произошла ошибка: {e}")
    finally:
        driver.quit()
        print("[*] Работа скрипта успешно завершена.")


if __name__ == '__main__':
    main()