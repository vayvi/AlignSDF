from glob import glob 
import argparse
parser = argparse.ArgumentParser()
DATADIR = '/home/cyrine_kalleli/Hand_reconstruction/'
parser.add_argument("--data_folder", help="folder where data is located",
                    type=str, default =DATADIR + 'AlignSDF/data/obman/train/sdf_hand_mini/')
parser.add_argument("--split_file_path", help="path for the split .json file to be created",
                    type=str, default = DATADIR + 'AlignSDF/experiments/obman/10k_1e2d_mlp5.json')
import json





def create_split(data_folder, split_file_path):
    my_dict = {
  "obman": {},
  "train":[]
  }
    file_list = []  
    for filename in glob(data_folder + '*.npz'):
        meshID = filename.split('/')[-1]
        meshID = meshID.split('.')[0]
        file_list.append(meshID)
        
    my_dict['train'] = file_list
    with open("obman_10k.json", "w") as outfile:
        json.dump(my_dict, outfile)









if __name__ == '__main__':
    args = parser.parse_args()
    create_split(args.data_folder, args.split_file_path)

