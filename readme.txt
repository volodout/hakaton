"Новогодняя Черепашья (Pygame) ёлка"

Для решения задачи и возможности графического отображения ёлки и гирлянды была выбрана
библиотека PyGame ввиду её удобства, простоты и многофункциональности.

Вся программа работает с частотой 15 к/с. Программа запускается из файла main.py.


Сначала импортируем библиотеку PyGame и инициализируем её, создаём основной цикл и самый главный
класс программы: Tree(). Её метод draw_tree() отрисовывает саму ёлку на экране, ствол и звезду
на конце.

С помощью метода points() (был удален после использования за ненадобностью) выбираем места,
на которых будут находиться лампочки на ёлке. Все их координаты находятся в файле
points.txt.

Реализуем консольный функционал: метод choice_mode() выводит в консоль сообщение, предлагающее
выбрать режим работы гирлянды, и принимает ответ от пользователя. Все ошибки обрабатываются:
если ответ не целое число или оно не является одним из предложенных программой, это вызовет
исключение, и повторится ожидание ввода.

!!!
Режим гирлянды можно выбрать только один раз сразу после запуска программы. Во время
её выполнения менять режим нельзя.

Работа метода change_colors() полностью зависит от результата работы предыдущего метода.
В зависимости от выбранного режима, гирлянда будет мерцать по-разному. Переменная tick
нужна для удобства и позволяет регулировать скорость мерцания.
Вот какие есть режимы:

1) 	Мерцание разными цветами. Тут все просто: с помощью random.choice() программа
	выбирает цвет из списка COLORS для каждой лампочки и рисует по координатам из
	points.txt круг нужного цвета в нужном месте. Отрисовка происходит каждый tick,
	поэтому лампочки в этом режиме меняют цвет быстрее всего.

2) 	Мерцание одним цветом. С помощью того же random.choice() программа выбирает
	цвет из списка COLORS и теперь уже перекрашивает в него ВСЕ лампочки на ёлке, но уже с 
	каждым пятым тиком.

3)	Мерцание двумя цветами. На этот раз с помощью random.sample() выбираем два
	неодинаковых цвета с1 и с2 и с помощью двух циклов for рисуем лампочки: круги с
	координатами, которые в файле points.txt стоят на чётных строках мы закрашиваем
	цветом с1, а на нечётных - с2. Через 12 тиков наоборот. После четырех таких
	обменов цветов переменные с1 и с2 становятся новыми неодинаковыми цветами.

4)	Мерцание "змейкой". В таком режиме все лампочки закрашиваются в цикле сверху вниз: с каждым разом
	на одну больше. Когда все лампочки загораются одним цветом, выбирается новый, и они
	начинают менять цвет поочереди снова.

Чтобы ёлке не было скучно и одиноко, рисуем ей обстановку: стены, пол, окно, диван, подарки
под ней. Тут все не сложно: с помощью pygame.draw.rect() отображаем на экране всё, что хотим.
Для этого создадим модуль room.py, чтобы не захламлять основной код. В функции draw_room
находится всё, что нам нужно.
Также добавим гирлянду на стену: она не будет зависеть от ввода в консоль, а всегда будет
работать как в режиме № 1 гирлянды на ёлке. Точки для этой гирлянды находятся в файле
wall_points.txt: все по знакомой схеме.

Остаётся только установить PyGame, запустить файл main.py и наслаждаться атмосферой уже ушедшего,
но не менее замечательного праздника)))