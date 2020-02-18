import torch
import torch.nn as nn
import torchvision.models as models
import torch.nn.functional as F


class CustomCNN(nn.Module):
    def __init__(self):
        super(CustomCNN, self).__init__()
  
        self.conv1 = nn.Conv2d(3, 16, 5, stride=2)
        self.conv2 = nn.Conv2d(16, 32, 3, stride=2)
        self.conv3 = nn.Conv2d(32, 64, 1, stride=1)
        self.conv3_bn = nn.BatchNorm2d(64)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(in_features= 64 * 6 * 6, out_features=500)
        self.dropout = nn.Dropout(0.5)        
        self.fc2 = nn.Linear(in_features=500, out_features=50)
        self.fc3 = nn.Linear(in_features=50, out_features=2)

        
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = F.relu(self.conv3_bn(self.conv3(x)))
        x = self.pool(x)
        x = x.view(x.shape[0], -1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        
        return x

    
class Pre_CNN_VGG(nn.Module):
    def __init__(self):
        super(Pre_CNN_VGG, self).__init__()
        vgg16 = models.vgg16_bn(pretrained=False)
        pre=torch.load(r'pth/vgg16_bn-6c64b313.pth')
        vgg16.load_state_dict(pre)        
        for param in vgg16.parameters():
            param.requires_grad_(False)
        
        modules = list(vgg16.children())[:-1]
        self.vgg16 = nn.Sequential(*modules)
        #self.vgg16 = vgg16
        self.fc1 = nn.Linear(512*7*7, 1024)
        self.dropout1 = nn.Dropout(0.4)        
        self.fc2 = nn.Linear(1024, 128)
        self.dropout2 = nn.Dropout(0.4)        
        self.fc3 = nn.Linear(128, 2)


    def forward(self, x):
        x = self.vgg16(x)
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout1(x)
        x = F.relu(self.fc2(x))
        x = self.dropout2(x)
        x = self.fc3(x)

        return x
