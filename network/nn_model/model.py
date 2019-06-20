import torch
import torch.nn as nn


def get_base_model():
    # can create more models to try which is better
    # Model_1: output = SELU*W3*{lrelu*[W2*[Sigmoid*(W1*lrelu*input+C1)]+C2]}+C3
    layers = []
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(480, 91))
    layers.append(nn.Sigmoid())
    layers.append(nn.Linear(91, 35))
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(35, 31))
    layers.append(nn.SELU())
    model = nn.Sequential(*layers)
    return model


def get_base_model_2():
    # Model_2: Added more nodes in hidden layer 360->256->128->35->40
    # Model_1: output = SELU*W3*{lrelu*[W2*[Sigmoid*(W1*lrelu*input+C1)]+C2]}+C3
    layers = []
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(360, 256))
    # layers.append(nn.Sigmoid())
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(256, 128))
    layers.append(nn.Sigmoid())
    # layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(128, 35))
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(35, 38))
    layers.append(nn.SELU())
    model = nn.Sequential(*layers)
    return model


def get_base_model_3():
    # Model_3: Added more nodes in hidden layer 256->512
    # Model_1: output = SELU*W3*{lrelu*[W2*[Sigmoid*(W1*lrelu*input+C1)]+C2]}+C3
    layers = []
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(360, 512))
    layers.append(nn.Sigmoid())
    layers.append(nn.Linear(512, 35))
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(35, 230))
    layers.append(nn.SELU())
    model = nn.Sequential(*layers)
    return model


def get_base_model_4():
    # Model_4: Added more nodes in hidden layer 512-512-512-256-64

    # Model_1: output = SELU*W3*{lrelu*[W2*[Sigmoid*(W1*lrelu*input+C1)]+C2]}+C3
    layers = []
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(360, 512))
    layers.append(nn.Sigmoid())
    layers.append(nn.Linear(512, 512))
    layers.append(nn.Sigmoid())
    layers.append(nn.Linear(512, 256))
    layers.append(nn.Sigmoid())
    layers.append(nn.Linear(256, 64))
    layers.append(nn.Sigmoid())
    layers.append(nn.Linear(64, 35))
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(35, 230))
    layers.append(nn.SELU())
    model = nn.Sequential(*layers)
    return model


def get_base_model_5():
    # Model_4: Added more nodes in hidden layer 512-512-512-256-64

    # Model_1: output = SELU*W3*{lrelu*[W2*[Sigmoid*(W1*lrelu*input+C1)]+C2]}+C3
    layers = []
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(600, 512))
    layers.append(nn.Sigmoid())
    layers.append(nn.Linear(512, 256))
    layers.append(nn.Sigmoid())
    layers.append(nn.Linear(256, 128))
    layers.append(nn.Sigmoid())
    layers.append(nn.Linear(128, 64))
    layers.append(nn.Sigmoid())
    layers.append(nn.Linear(64, 35))
    layers.append(nn.LeakyReLU())
    layers.append(nn.Linear(35, 27))
    layers.append(nn.SELU())
    model = nn.Sequential(*layers)
    return model