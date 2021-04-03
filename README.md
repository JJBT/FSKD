# Few-Shot Keypoint Detection (4rd year coursework & diploma work)
## Запуск тренировки на синтетическом MegapixelMNIST
Чтобы сгенерировать данные и создать конфиг под них, необходимо из корневой директории запустить `generate_synthetic_data.py`
* `--mnist_path` - путь к папке, в которой находится датасет MNIST (если датасет не установлен, то он скачается в папку, указанную в параметре)
* `--megapixel_mnist_path` - путь к папке, в которую будет сохранен сгенерированный датасет (если уже существует, то перезапишется)

Чтобы начать тренировку, необходимо из корневой директории запустить `train.py`. Результаты, включающие текущую версию конфига, чекпоинты, файл логгирования, файл тензорборд объекта, сохранятся в папку `outputs/текущая_дата/текущее_время`.
Чтобы изменить параметры тренировки, необходимо передать их в качестве параметров скрипта `train.py` или изменить напрямую в конфиге `conf/config.yaml`.  
Некоторые базовые параметры тренировки:
* `n_steps` - количество шагов 
* `bs` - размер батча
* `hooks` - хуки
    * `type`- тип хука. `LogCallback` инициирует логгирование, `ValidationCallback` инициирует валидацию, `TensorBoardCallback` инициирует запись в тензорборд, `SaveCheckpointCallback` инициируется сохранения чекпоинта
    * `frequency` - частота вызова хука

По умолчанию валидация проводится на валидационных данных, содержащих классы картинок, отличных от тех, что встречаются
в тренировчных данных, а также на валидационных данных содержащих ислючительно классы, совпадающие с тренировочными.
 