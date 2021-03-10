import os

def createDisk(pathDir, name, gb):
    os.system(f"qemu-img create -f qcow2 {pathDir}/{name}.qcow {gb}G")

def deleteDisk(name):
    os.system(f"rm {name}")

def startVM(car, mem):
    os.system(f"qemu-system-x86_64 -hda {car} -m {mem} -enable-kvm")

def bootCar(disk, pathToISO, mem):
    if disk == False:
        os.system(f"qemu-system-x86_64 -boot d -cdrom {pathToISO} -m {mem} -enable-kvm")
    else:
        os.system(f"qemu-system-x86_64 -hda {disk} -boot d -cdrom {pathToISO} -m {mem} -enable-kvm")

def converToRaw(disk):
    name = str(disk).split('.')
    os.system(f"qemu-img convert -O raw {disk} {name[0]}.raw")