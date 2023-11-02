# MarcosAparicioTensors

# TENSOR CALCULATOR


# DESCRIPTION:
This project consists on the coding of a module that allows the user to perform some operations with Pytorch 2-dimensional Tensors. These operations are:
- Returns an all-Zeros Tensor -> zeros().
- Returns an all-Ones Tensor -> ones().
- Returns a Tensor with random values -> random().
- Returns the sum of two tensor -> add().
- Returns the multiplication of two tensors -> multiply().
- Returns the maximum value of one tensor -> max_value().
- Returns the minimum value of one tensor -> min_value().
- Returns a normalized tensor -> normalize().


# PACKAGES:
In order to be able to use correctly this module you should import these packages or modules:
- torch.
- TensorOperations from module_structure.tensors.

You must import this packages with the following commands:
- import torch.
- from module_structure.tensors import TensorOperations.

# USAGE:
As I have explained in the previous section, firstly you should put the following commands:

    from module_structure.tensors import TensorOperations
    import torch

After that, you should create two PyTorch tensors. For example, using this code:

    tensor1_input = input("Enter the first tensor (e.g., [[1, 2], [3, 4]]): ")
    tensor2_input = input("Enter the second tensor (e.g., [[5, 6], [7, 8]]): ")

    # Parse user input to create PyTorch tensors
    tensor1 = torch.tensor(eval(tensor1_input))
    tensor2 = torch.tensor(eval(tensor2_input))

Then, you have to create an instance of TensorOperations:

    # Create an instance of TensorOperations
    operations = TensorOperations(tensor1, tensor2)

And finally, you can perform the operations I have explained in the DESCRIPTION section with the following code:
    
    result_zeros = operations.zeros()
    print("\nZeros Tensor:")
    print(result_zeros)

    result_ones = operations.ones()
    print("\nOnes Tensor:")
    print(result_ones)

    result_random = operations.random()
    print("\nRandom Tensor:")
    print(result_random)

    result_add = operations.add()
    print("\nSum of Tensors:")
    print(result_add)

    result_multiply = operations.multiply()
    print("\nMultiplication of Tensors:")
    print(result_multiply)

    result_norm = operations.normalize()
    print("\nTensor normalizado:")
    print(result_norm)

    res_max = operations.max_value()
    print("\nMax value:")
    print(res_max)

    res_min = operations.min_value()
    print("\nMin value:")
    print(res_min)


# LICENSE:
Copyright (c) 2023 Marcos Aparicio Blázquez. Consult 'LICENSE' for more details.
