import torch.nn as nn
import torch.nn.functional as F
import torch

class TheNet(nn.Module):
    def __init__(self):
        super(TheNet, self).__init__()

        # Layer 1
<<<<<<< HEAD
        self.conv1 = nn.Conv2d(28, 32, (1, 10), padding=(0))
        self.batchnorm1 = nn.BatchNorm2d(32, False)
=======
        self.conv1 = nn.Conv2d(28, 14, (1, 10), padding=(0))
        self.batchnorm1 = nn.BatchNorm2d(14)
>>>>>>> fd7c483d653926198b5145cb2dca14bf58387e33

        # Layer 2
        # Layer 2
        self.padding1 = nn.ZeroPad2d((10, 10, 0, 0))
<<<<<<< HEAD
        self.conv2 = nn.Conv2d(32, 64, (1, 3))
        self.batchnorm2 = nn.BatchNorm2d(64, False)
        self.pooling2 = nn.MaxPool2d(1, 10)

        # Layer 2
        self.padding3 = nn.ZeroPad2d((4, 4, 0, 0))
        self.conv3 = nn.Conv2d(64, 128, (1, 3))
        self.batchnorm3 = nn.BatchNorm2d(128, False)
=======
        self.conv2 = nn.Conv2d(14, 4, (1, 3))
        self.batchnorm2 = nn.BatchNorm2d(4)
        self.pooling2 = nn.MaxPool2d(1, 4)

        # Layer 2
        self.padding3 = nn.ZeroPad2d((4, 4, 0, 0))
        self.conv3 = nn.Conv2d(4, 4, (1, 3))
        self.batchnorm3 = nn.BatchNorm2d(4)
>>>>>>> fd7c483d653926198b5145cb2dca14bf58387e33
        self.pooling3 = nn.MaxPool2d(1, 4)

        # Layer 2
        self.padding4 = nn.ZeroPad2d((4, 4, 0, 0))
        self.conv4 = nn.Conv2d(128, 256, (1, 3))
        self.batchnorm4 = nn.BatchNorm2d(256, False)
        self.pooling4 = nn.MaxPool2d(1, 4)

        # FC Layer
        self.fc1 = nn.Linear(768, 2)

        self.apply(self.init_weights)

    def init_weights(self, m):
        if type(m) == nn.Conv2d:
<<<<<<< HEAD
            torch.nn.init.xavier_uniform_(m.weight)
=======
            torch.nn.init.normal(m.weight, 0, 0.01)
            if m.bias is not None:
                nn.init.constant(m.bias, 0)
        elif isinstance(m, nn.BatchNorm2d):
            nn.init.constant(m.weight, 1)
            nn.init.constant(m.bias, 0)
        elif isinstance(m, nn.Linear):
            nn.init.normal(m.weight, 0, 0.01)
            nn.init.constant(m.bias, 0)
>>>>>>> fd7c483d653926198b5145cb2dca14bf58387e33

    def forward(self, x):
        # Layer 1

        x = x.unsqueeze(2)
        print(x.shape)
        x = F.elu(self.conv1(x))
        x = self.batchnorm1(x)
        x = F.dropout(x, 0.50)
        print(x.shape)

        # print(x.shape)
        # Layer 2
        x = self.padding1(x)
        x = F.elu(self.conv2(x))
        x = self.batchnorm2(x)
        x = F.dropout(x, 0.50)
        print(x.shape)
        x = self.pooling2(x)

        # print(x.shape)
        # Layer 3
        x = self.padding3(x)
        x = F.elu(self.conv3(x))
        x = self.batchnorm3(x)
        x = F.dropout(x, 0.50)
        x = self.pooling3(x)

        x = self.padding4(x)
        x = F.elu(self.conv4(x))
        x = self.batchnorm4(x)
        x = F.dropout(x, 0.50)
        x = self.pooling4(x)

        # print(x.shape)

        x = x.view(x.shape[0], -1, 768)
        x = self.fc1(x)
        x = x.squeeze(1)
        return x