from Tasks.Task1.Task1_1.Сircle import Сircle #Импорт класса

firstCircle = Сircle() #Создание экземпляра класса. Присвоение класса переменной, чтобы мы могли записать в память и манипулировать классом в дальнейшем.

print("Радиус до того как мы его засетали: " + str(firstCircle.getRadius()))

radius = int(input("Введите радиус: ")) #Вызываем сканер экрана, чтобы считать значение, введённое пользователем и записываем его в переменную radius.
firstCircle.setRadius(radius) #Устанавливаем значение через сеттер, чтобы сделать расчёт в дальнейшем.

print("А это уже после того как мы указали радиус: " + str(firstCircle.getRadius()))

firstCircle.calculateArea(firstCircle.getRadius()) #Теперь введённое значение вставляем в функцию с помощью геттера.
firstCircle.printResult() #Выводим ответ на экран.
