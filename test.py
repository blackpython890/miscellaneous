from datetime import datetime
print("Current Date/Time: ", datetime.now())


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Sequential(nn.Conv2d(in_channels=3,out_channels=16,kernel_size=(3,3),padding=1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(num_features=16),
                                   nn.Conv2d(16,32,3, padding = 1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(num_features=32)
                                   )
                                   
        self.maxpool1 = nn.Sequential( nn.nn.MaxPool2d(2,2) )
        
        self.conv2 = nn.Sequential(nn.Conv2d(in_channels=32,out_channels=64,kernel_size=(3,3),padding=1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(num_features=64),
                                   nn.Conv2d(64,64,3,padding = 1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(num_features=64),
                                   nn.Conv2d(in_channels=64,out_channels=128,kernel_size=(3,3),padding=1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(num_features=128)
                                   )
                                   
        self.maxpool2 = nn.Sequential( nn.nn.MaxPool2d(2,2) )
        
        self.conv3 = nn.Sequential(nn.Conv2d(in_channels=128,out_channels=128,kernel_size=(3,3),padding=1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(num_features=128),
                                   nn.Conv2d(128,128,3,padding = 1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(num_features=128),
                                   nn.Conv2d(128,128,3,padding = 1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(num_features = 128)
                                   )
        
        self.gap  =  nn.Sequential( nn.AvgPool2d(kernel_size=8))
        self.fc = nn.Sequential( nn.Linear( 128,10) )
        
        
              


    def forward(self, x):
        x = self.conv1(x)
        x = self.maxpool1(x)
        x = self.conv2(x)
        x = self.maxpool2(x)
        x = self.conv3(x)
        x = self.gap(x)
        x = self.fc(x)
        x = x.view(-1, 10)
        return F.log_softmax(x)


