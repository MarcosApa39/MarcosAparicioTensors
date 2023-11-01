import torch
from dataclasses import dataclass


@dataclass
class TensorOperations:
    def __init__(self, tensor_1, tensor_2):
        self.tensor1 = tensor_1
        self.tensor2 = tensor_2

    def zeros(self):
        return torch.zeros_like(self.tensor1)

    def ones(self):
        return torch.ones_like(self.tensor1)

    def random(self):
        return torch.rand(self.tensor1.shape)

    def add(self):
        return self.tensor1 + self.tensor2

    def multiply(self):
        if self.tensor1.shape[1] == self.tensor2.shape[0]:
            return torch.matmul(self.tensor1, self.tensor2)
        else:
            raise ValueError("Tensors dimensions are not compatible for multiplication")

    def resta(self):
        return self.tensor1 - self.tensor2

    def max_value(self):
        return torch.max(self.tensor1)

    def min_value(self):
        return torch.min(self.tensor1)

    def normalize(self):
        min_val = torch.min(self.tensor1)
        max_val = torch.max(self.tensor1)
        normalized_tensor = (self.tensor1 - min_val) / (max_val - min_val)
        return normalized_tensor



