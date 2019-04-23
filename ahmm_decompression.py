# Alan and His Merry Men Image Decompression


import argparse, sys, os



class Setting:
    pass


def name_outfile(infile):
	""" DO SOMETHING BETTER HERE; Consider multiple input files"""
	return infile[0] + "output"


class App:
	"""
	Class for running the machine learning models
	"""
	
	def __init__(self, args):
		self.args = args

	def apply_args(self):
		"""Apply arguments using Setting class"""
		Setting.IMAGES = self.args.image
		Setting.ALGORITHM = self.args.algorithm
		Setting.DEVICE = self.args.device
		if (self.args.output != ''):
			Setting.OUTFILE = self.args.output
		else:
			Setting.OUTFILE = name_outfile(self.args.image)

	def run_model(self):
		"""Run the specified model on the given input"""
		if Setting.ALGORITHM == 1:
			# Run super-resolution model
			print("Running Super-Resolution Algorithm...")
			
			# Model only accepts one input at a time; run for each input image
			for input_image in Setting.IMAGES:
				print("\nEnhancing image \"" + input_image + "\"\n")
				input_image = Setting.IMAGES[0]
				super_res_call = "python3 enhance.py --type=photo --model=custom --zoom=4 --device " + Setting.DEVICE + " " + input_image
				os.system(super_res_call)
		else:
			# No valid model selected
			print("No valid model selected.")



# Define custom commandline arguments
implemented_model_ids = [1]
algorithm_form_help = "(1)  Super-Resolution Algorithm (Does not accept output specification)\n" #+ \
					  #"(2)  Optical Character Recognition Algorithm" + \
					  #"(3)  Pipelined Both"
parser = argparse.ArgumentParser(description='Alan and His Merry Men\'s Image Decompression')
parser.add_argument('image', nargs='*', default=[], help='input image files')
parser.add_argument('-o', '--output', type=str, default='', help='specifiy a file name for the output')		# Allow multiple outfile args for multiple inputs?
parser.add_argument('--device', type=str, default="cpu", help="device to use for network (cpu, cuda, opencl) default: cpu")
parser.add_argument('--algorithm', type=int, default=1, help=algorithm_form_help)


# Parse arguments; close if no input images are defined
args = parser.parse_args()
#print(args)
if not args.image or args.algorithm not in implemented_model_ids:
	parser.print_help()
	sys.exit(0)


# Define application with args, apply args, and run application
app = App(args)
app.apply_args()
app.run_model()
