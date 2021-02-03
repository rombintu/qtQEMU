# qtQEMU
gui for qemu by Nickolsky (for Linux)

**Dependencies:**
- qemu
- qemu-kvm (optional)
- python3

*Run once:*
> git clone https://github.com/rombintu/qtQEMU.git  
> cd qtQEMU  
> pip install -r req.txt  
> python main.py  

*Install (beta):*
> git clone https://github.com/rombintu/qtQEMU.git  
> cd qtQEMU  
> pip install -r req.txt  
> sh pyinstaller.sh  
> ln qtQemu /bin/qtqemu  
> qtqemu  

*Manual:*  
Для работы с ВМ рекомендуется создать диск (Создать -> Новый диск)  
Для запуска машины в live (Действия -> Запустить iso без диска)  
После установки образа на диск можно запускать машину из главного окна, указывая путь к ней  
