Download the Yolov5 repository from official github.
Train the model on big dataset like flikr sports dataset.
Save the trained model and use it as pretrained model for further train.
Freeze initial 10 layers of yolov5 and train it with our custom dataset(atleast 10 images per class)
freeze = ['model.%s.' % x for x in range(10)] 
Save the final recieved model.
Create a fast api framework to run this as web app.
uvicorn start:app #To run the fast api server