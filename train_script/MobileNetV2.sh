python train.py --a mobilenet_v2 --wd 1e-4 --lr 3e-4 --epochs 8 --gpu 1  --tensorboard --train-method norm+last  -t CIFAR10 --pretrained  ./data