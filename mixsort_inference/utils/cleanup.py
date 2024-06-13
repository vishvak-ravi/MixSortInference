import shutil
import os

def inference_cleanup(experiment_name, video_folder):
    mot_name = experiment_name + "_mot"
    coco_name = experiment_name + "_coco"
    base_dir = 'datasets/'
    mot_dir = os.path.join(base_dir, mot_name)
    coco_dir = os.path.join(base_dir, coco_name)
    file_name = f"yolox_x_{experiment_name}_coco.py"
    exp_dir = "exps/example/mot/"
    exp_file_name = os.path.join(exp_dir, file_name)
    
    if os.path.exists(mot_dir) and os.path.isdir(mot_dir):
        shutil.rmtree(mot_dir)
        print(f"Successfully cleand up the directory: {mot_dir}")
    else:
        print(f"The directory does not exist: {mot_dir}")
        
    if os.path.exists(coco_dir) and os.path.isdir(coco_dir):
        shutil.rmtree(coco_dir)
        print(f"Successfully cleand up the directory: {coco_dir}")
    else:
        print(f"The directory does not exist: {coco_dir}")    
    if os.path.exists(exp_file_name) and os.path.isfile(exp_file_name):
        os.remove(exp_file_name)
        print(f"Successfully deleted the file: {exp_file_name}")
    else:
        print(f"The file does not exist: {exp_file_name}")
        
    source_dir = f"YOLOX_outputs/yolox_x_{coco_name}/"
    target_dir = os.path.join(video_folder, experiment_name)
        
    if os.path.exists(source_dir) and os.path.isdir(source_dir):
        shutil.move(source_dir, target_dir)
        print(f"Successfully moved the directory: {source_dir} to {target_dir}")
    else:
        print(f"The directory does not exist: {source_dir}")
    
# Example usage
#delete_experiment_directory('yolox_x_sample_test')
