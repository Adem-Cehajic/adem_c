import os

package_directory = os.path.dirname(os.path.abspath(__file__))

################## To edit
# Dataset
packaged_data_folder = '/home/mkeller2/data2/Data/hit_release/hit_dataset_v1.0/repackaged'

# Trained HIT models
trained_models_folder = os.path.join(package_directory, '../pretrained')  # folder to save the trained models
pretrained_male_smpl = os.path.join(package_directory, '../pretrained/pretrained_male_smpl.ckpt') 
pretrained_female_smpl = os.path.join(package_directory, '../pretrained/pretrained_female_smpl.ckpt')
                                    
smplx_models_path = '/home/ademc/HIT/smplx_models' # folder containing the smplx models, to download from https://smpl-x.is.tue.mpg.de/downloads

# Training logging
wandb_entity = 'mkeller' # wandb account or team to log to
wandb_project_name = 'hit_rel' # wandb project to log to
##################


# assets
v2p = os.path.join(package_directory, 'assets/v2p.pkl')  # file that for each smpl vertex, gives the corresponding part

n_chunks_test = 10 # number of chunks to split the test set into. Increase to reduce memory usage when caching the dataset
n_chunks_train = 20 # Same for the train set
    
# Logger for training
logger = 'wandb' # only wandb is supported
