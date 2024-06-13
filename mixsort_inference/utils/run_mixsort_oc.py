import os
import subprocess

def run_inference(expn):
    expn = "yolox_x_" + expn
    expn_py = expn + ".py"
    f = os.path.join("exps/example/mot/", expn_py)
    bash_command = f"""
    export CUDA_VISIBLE_DEVICES=0

    python3 tools/track_mixsort_oc_simple.py \
    -expn {expn} \
    -f {f} \
    -c pretrained/yolox_x_sports_mix.pth.tar \
    -b 1 \
    -d 1 \
    --config track
    """

    process = subprocess.Popen(bash_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print("Output:", stdout.decode())
    if stderr:
        print("Error:", stderr.decode())

# Example usage
#run_bash_script('yolox_x_sample_test', 'exps/example/mot/yolox_x_sample_test.py')
