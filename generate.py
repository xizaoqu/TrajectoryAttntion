from utils.generate import load_pipeline, generate
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    "--image_folder",
    type=str
)

parser.add_argument(
    "--output_folder",
    type=str
)

parser.add_argument(
    "--trajectory_folder",
    type=str
)

parser.add_argument(
    "--num_frames",
    type=int
)

parser.add_argument(
    "--seed",
    type=int,
    default=12345
)

parser.add_argument(
    "--checkpoint",
    type=str,
)

parser.add_argument(
    "--svd_path",
    type=str,
)

parser.add_argument(
    "--svd_unet_path",
    type=str,
)

args = parser.parse_args()

unet_path = args.svd_unet_path
svd_path = args.svd_path
checkpoint = args.checkpoint
pipeline = load_pipeline(unet_path, svd_path, checkpoint)

image_path = os.listdir(args.image_folder)
assert len(image_path) == 1
image_path = os.path.join(args.image_folder, image_path[0])
generate(pipeline, args.trajectory_folder, image_path, 
         args.output_folder, args.num_frames, seed=args.seed)