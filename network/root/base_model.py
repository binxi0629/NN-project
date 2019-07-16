import torch.nn as nn


def get_bs2sg():
    layers = [
        nn.LeakyReLU(),
        nn.Linear(1200, 128),
        nn.LeakyReLU(),
        nn.Linear(128, 128),
        nn.LeakyReLU(),
        nn.Linear(128, 230),
        nn.LeakyReLU(),
    ]
    model = nn.Sequential(*layers)
    return model


def get_bs2crys():
    layers = [
        nn.LeakyReLU(),
        nn.Linear(1200, 256),
        nn.LeakyReLU(),
        nn.Linear(256, 128),
        nn.LeakyReLU(),
        nn.Linear(128, 7)
    ]
    model = nn.Sequential(*layers)
    return model


def get_crys2sg(*args):
    layers = []
    for i in range(len(args) - 1):
        layers.append(nn.LeakyReLU())
        layers.append(nn.Linear(args[i], args[i+1]))
    model = nn.Sequential(*layers)
    return model
