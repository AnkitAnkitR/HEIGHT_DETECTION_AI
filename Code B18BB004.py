

import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor
import torch
import numpy as np
import cv2
import torchvision.transforms as T


      
def get_instance_segmentation_model(num_classes):
    # load an instance segmentation model pre-trained on COCO
    model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=False)

    # get the number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    # now get the number of input features for the mask classifier
    in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
    hidden_layer = 256
    # and replace the mask predictor with a new one
    model.roi_heads.mask_predictor = MaskRCNNPredictor(in_features_mask,
                                                       hidden_layer,
                                                       num_classes)
    return model


device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
num_classes = 2

model = get_instance_segmentation_model(num_classes)
model.to(device)

weight_location = "weight.pt"
#img, _ = dataset_test[5]
state_dict = torch.load(weight_location, map_location = 'cuda:0')
model.load_state_dict(state_dict)
# put the model in evaluation mode
model.eval()

trans=T.ToTensor()

cap = cv2.VideoCapture(0)

with torch.no_grad():
    while(True):
        #start = time.time()
        ret, input_img = cap.read()
        frame = trans(input_img)
        prediction = model([frame.to(device)])
        for i in range(len(prediction[0]['scores'])):

            if(prediction[0]['scores'][i].cpu().numpy()>0.5):
                x = prediction[0]['masks'][i,0].mul(255).byte().cpu().numpy()
                #x = cv2.merge((x,x,x))
            break
        _,thresh1 = cv2.threshold(x,50,255,cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
            bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
            break
        cv2.merge((thresh1,thresh1,thresh1))
        cv2.line(thresh1, topmost, bottommost, (120, 255, 0), 4)
        distance = np.sqrt(((topmost[0]-bottommost[0])**2)+((topmost[1]-bottommost[1])**2))
        cv2.putText(thresh1, str(distance), (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0) , 2, cv2.LINE_AA)
        
        cv2.imshow('frame', thresh1)
        #end = time.time()
        #print(end-start)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
cap.release()
cv2.destroyAllWindows()