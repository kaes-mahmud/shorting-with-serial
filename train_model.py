import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# শক্তিশালী এবং BatchNorm সহ মডেল স্ট্রাকচার
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.main = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 512),
            nn.BatchNorm1d(512), 
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 62)
        )
    def forward(self, x):
        return self.main(x)

def train():
    print("⏳ উন্নত AI মডেল ট্রেনিং শুরু হচ্ছে... (Epochs: 5)")
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1736,), (0.3317,))
    ])
    train_set = datasets.EMNIST(root='./data', split='byclass', train=True, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=128, shuffle=True)
    
    model = Net()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(5):
        model.train()
        for batch_idx, (data, target) in enumerate(train_loader):
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
        print(f"✅ Epoch {epoch+1} শেষ।")
    
    torch.save(model.state_dict(), "handwritten_model.pth")
    print("✨ শক্তিশালী AI মডেল তৈরি শেষ!")

if __name__ == "__main__":
    train()