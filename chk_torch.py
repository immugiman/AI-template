import torch

print("PyTorch verzió:", torch.__version__)
print("CUDA elérhető:", torch.cuda.is_available())
print("CUDA eszközök száma:", torch.cuda.device_count())
print("Alapértelmezett eszköz:", torch.cuda.current_device())
print("GPU neve:", torch.cuda.get_device_name(0))
