import os
import torch
import torch.nn as nn
from matplotlib import pyplot as plt
from tqdm import tqdm
from torch import optim
import logging
import pennylane as qml
import numpy as np
import random
import time

a = time.time()


config = {
    "qubits": 4,  
    "layers": 3,  
}
w = np.random.rand(config["qubits"] * 2)


#dev = qml.device('default.qubit', wires=config["qubits"])
dev = qml.device('lightning.kokkos', wires=config["qubits"])

#@qml.qnode(dev, interface='torch', diff_method='backprop')
@qml.qnode(dev, interface='torch', diff_method='adjoint')
def gen_circuit(w):
    # 随机生成初始角度
    z1 = random.uniform(-1, 1)
    z2 = random.uniform(-1, 1)
    for i in range(config["qubits"]):
        qml.RY(np.arcsin(z1), wires=i)
        qml.RZ(np.arcsin(z2), wires=i)
    for l in range(config["layers"]):
        for i in range(config["qubits"]):
            qml.RY(w[i], wires=i)
        for i in range(config["qubits"]-1):
            qml.CNOT(wires=[i, i+1])
            qml.RZ(w[i + config["qubits"]], wires=i+1)
            qml.CNOT(wires=[i, i+1])
    return [qml.expval(qml.PauliZ(i)) for i in range(config["qubits"])]


x = torch.randn(1, 3, 64, 64)
Ɛ = torch.zeros_like(x)

for i in range(x.shape[1]): 
    for j in range(x.shape[2]):
        values = []
        for k in range(0, x.shape[3]):
            if k % config["qubits"] == 0:  
                values = gen_circuit(w)
                random.shuffle(values)
            Ɛ[:, i, j, k] = values[k % config["qubits"]] 

            
b = time.time()
print(b-a)