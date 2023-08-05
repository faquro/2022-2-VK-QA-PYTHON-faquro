## Домашнее задание №4: Appium (необязательное)

#### Цель домашнего задания

  * Научиться использовать инструменты для автоматизации UI мобильных приложений. 


#### Задача
* Тестирование мобильного приложения голосового помощника "Маруся" ([Google Play](https://play.google.com/store/apps/details?id=ru.mail.search.electroscope&hl=ru&gl=US)).
  Apk уже лежит в директории данной лекции.
* Тесты должны запускаться через марк -m Android или AndroidUI
* Тесты должны быть написаны для девайсов с версией Android 11 или выше.
* Appium должен использоваться последней версии.
* **Важное уточнение:** Данное задание является дополнительным и не влияет на вашу успеваемость, 
  т.е. вы можете его сдать и получить доп баллы, а можете ничего не делать, и вам за это ничего не будет.
* Тестирование приложения голосового помощника "Маруся":
     * **Настройка окружения и иные аспекты** (0.25 балла):
       1. Найти appPackage, appActivity, разобраться с выдачей разрешений приложению при его запуске. 
       2. apk приложения должен лежать в отдельной папке, путь к нему должен быть указан относительно корня репозитория 
          (с помощью фикстуры repo_root или иными способами).
       3. весь код (тех заданий, которые вы сделаете) должен быть написан в паттерне PageObject (например, главная пейджа + пейджа настроек + внутренние пейджы для элементов настроек).
       4. в requirements (в корне вашего репозитория) должны присутствовать все новые библиотеки, которые вами использовались.
     * **Взаимодействие с окном команд (1.5 балла)**:
       
       1. Ввести в чат (окно команд) слово Russia (в приложении может быть баг и возможно понадобится вводить слово 2 раза), удостовериться что у нас появился на экране текст с описанием страницы страны. 
       2. В списке приложений для команд проскроллить до "население россии" и нажать на него.
       3. Удостовериться, что результат - 146 млн.
         
     * **Взаимодействие с окном команд, функционал "Калькулятор"** (1 балл):
       
       Ввести в чат (окно команд) какое-то простое математическое выражение (сложение/умножение/возведение в степень целых чисел),
       удостовериться что нам пришло в качестве ответа именно то число, которое предполагалось.
       
       **Важно**: можно ввести что-то и более сложное, но есть шанс нарваться на баги приложения.
     * **Взаимодействие с источником новостей** (1.5 балла):
       
       1. Зайти в настройки приложения, выбрать раздел источник новостей, и там выбрать **Mail.Ru**.
       2. Удостовериться, что на странице выбора новостей у выбранного способа появилась галочка.
       3. Вернуться на главное окно, ввести в окно команд команду News и удостовериться любым способом, что новости появились.
     * **Взаимодействие с настройками приложения** (1 балл):
       
        Открыть бургер-меню, открыть раздел "О приложении" и удостовериться:
          
          а) Что версия (текст с цифрами) приложения содержит в себе именно ту версию, которая также указана в названии APK файла. 
       Проверку осуществлять путем чтения версии из названия файла, а не хардкодом.
          
          б) Что внизу страницы присутствует трейдмарка ("все права защищены")

#### Советы
  * Тесты *НЕ* должны быть зависимыми.
  * Все тесты *ДОЛЖНЫ* проходить. Если в приложении баг и это влияет на стабильность ваших тестов - напишите об этом при сдаче домашки.
  * Тесты *ОБЯЗАТЕЛЬНО* должны что-то проверять. Например если мы что-то создали - необходимо проверить что оно создалось.
  * Тесты *ДОЛЖНЫ* уметь запускаться несколько раз подряд.
  * Тесты должны работать в один поток (xdist не требуется).
 
#### Срок сдачи ДЗ

  До 31 октября 23:59 (включительно)