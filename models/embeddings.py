import torch
import torchvision.transforms as transforms
from torchvision.models import resnet18, ResNet18_Weights
import cv2

# Load model (updated, no warning)
model = resnet18(weights=ResNet18_Weights.DEFAULT)
model.fc = torch.nn.Identity()
model.eval()

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def get_embedding(img):
    """
    Takes grayscale or BGR image and returns embedding
    """

    # 🔥 FIX: Convert grayscale → 3 channel
    if len(img.shape) == 2:  # grayscale
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = transform(img).unsqueeze(0)

    with torch.no_grad():
        emb = model(img)

    return emb