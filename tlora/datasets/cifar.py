from tlora.datasets.datasets import processor, DatasetFactory
from tlora.datasets.registry import register_dataset
from typing import Tuple, Optional
from torchvision import datasets
import torch

class CIFAR10Dataset(DatasetFactory, dataset_name="cifar10"):
    """CIFAR-10 implementation following factory pattern"""
    
    def get_splits(self) -> Tuple[torch.utils.data.Dataset, ...]:
        transform = lambda img: processor(img, return_tensors="pt")["pixel_values"].squeeze(0)
        
        train = datasets.CIFAR10(
            root=self.root,
            train=True,
            download=self.download,
            transform=transform
        )
        
        test = datasets.CIFAR10(
            root=self.root,
            train=False,
            download=self.download,
            transform=transform
        )
        
        if self.validation_split:
            val_size = int(len(train) * self.validation_split)
            train, val = torch.utils.data.random_split(train, [len(train)-val_size, val_size])
            return train, val, test
            
        return train, test

class CIFAR100Dataset(DatasetFactory, dataset_name="cifar100"):
    """CIFAR-100 implementation following factory pattern"""
    
    def get_splits(self) -> Tuple[torch.utils.data.Dataset, ...]:
        transform = lambda img: processor(img, return_tensors="pt")["pixel_values"].squeeze(0)
        
        train = datasets.CIFAR100(
            root=self.root,
            train=True,
            download=self.download,
            transform=transform
        )
        
        test = datasets.CIFAR100(
            root=self.root,
            train=False,
            download=self.download,
            transform=transform
        )
        
        if self.validation_split:
            val_size = int(len(train) * self.validation_split)
            train, val = torch.utils.data.random_split(train, [len(train)-val_size, val_size])
            return train, val, test
            
        return train, test