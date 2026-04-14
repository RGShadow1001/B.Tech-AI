specs={
    "cpu" : "Intel core i5 12400F",
    "ram" : "32 GB DDR4 Dual Chanel(16 GB)",
    "stg" : "512GB pcieX4 NVMe SSD",
    "gpu" : "NVIDIA GeForce RTX5060Ti",
    "mb" : "Gigabyte Z690 UD Ax DDR4 V2"

}
def recall():
    inp=input("what do you want to see cpu/gpu/ram/mb/stg")
    print(specs[inp])
recall()