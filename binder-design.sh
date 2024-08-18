#!/bin/bash

# Variables
models_dir="/home/lily/amelie/Workspace/RFdiffusion/models"
new_output_dir="/home/lily/amelie/Workspace/RFdiffusion/outputs/gap-junctions/run1"
timestamp=$(date +%Y%m%d%H%M%S)
input_pdb="/home/lily/amelie/Workspace/RFdiffusion/examples/input_pdbs/8qoj.pdb"
num_designs=10
contigs="J19-102/J194-282/0 6-6/0 I19-102/I194-282"
hotspot_res="J29,J30,J31,J32,J33,J34,J35,J36,J37,I81,I82,I83,I84,I85,I86,I87,I88,I89,I90,I91,I92"

# Docker command
docker run -it --rm --gpus all \
    -v "${models_dir}:${models_dir}" \
    -v "${input_pdb}:${input_pdb}" \
    -v "${new_output_dir}:${new_output_dir}" \
    rfdiffusion \
    inference.output_prefix="${new_output_dir}/output_${timestamp}" \
    inference.model_directory_path="${models_dir}" \
    inference.input_pdb="${input_pdb}" \
    inference.num_designs=${num_designs} \
    contigmap.contigs="[${contigs}]" \
    ppi.hotspot_res="[${hotspot_res}]"
