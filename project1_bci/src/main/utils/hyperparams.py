import torch
torch.manual_seed(30) # 55 not bad
import json

"""
Function that loads the configuration file and gets the parameters.
@:returns
    - model: the model used for training
    - epochs: how many epochs of training
    - batch_size: the batch-size for training
    - learning_rate: the learning rate for training
"""
def load_config():
    # reading file
    with open('config/config.json', 'r') as f:
        config = json.load(f)

    # retrieve hyper params
    epochs = config['epochs']
    batch_size = config['batch_size']
    weight_decay = config['weight_decay']

    return epochs, batch_size, weight_decay




