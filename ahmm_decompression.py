# Alan and His Merry Men Image Decompression


import argparse, sys



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
		if (self.args.output != ''):
			Setting.OUTFILE = self.args.output
		else:
			Setting.OUTFILE = name_outfile(self.args.image)

	def run(self):
		"""Run the specified model on the given input"""
		pass



# Define custom commandline arguments
algorithm_form_help = "(1)  Super-Resolution Algorithm\n" + \
					  "(2)  Optical Character Recognition Algorithm" + \
					  "(3)  Pipelined Both"
parser = argparse.ArgumentParser(description='Alan and His Merry Men\'s Image Decompression')
parser.add_argument('image', nargs='*', default=[], help='input image files')
parser.add_argument('-o', '--output', type=str, default='', help='specifiy a file name for the output')		# Allow multiple outfile args for multiple inputs?
parser.add_argument('--algorithm', type=int, default=1, help=algorithm_form_help)


# Parse arguments; close if no input images are defined
args = parser.parse_args()
print(args)
if not args.image or args.algorithm not in [1,2,3]:
	parser.print_help()
	sys.exit(0)


# Define application with args, apply args, and run application
app = App(args)
app.apply_args()
app.run()
