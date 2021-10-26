import ctypes
import numpy
import glob
import subprocess as sub


# find the shared library, the path depends on the platform and Python version
libfile = glob.glob('build/*/main*.so')[0]

# 1. open the shared library
mylib = ctypes.CDLL(libfile)

# 2. tell Python the argument and result types of function mysum
# mylib.mysum.restype = ctypes.c_longlong
# mylib.mysum.argtypes = [ctypes.c_int, 
#                         numpy.ctypeslib.ndpointer(dtype=numpy.int32)]

# array = numpy.arange(0, 100000000, 1, numpy.int32)

# # 3. call function mysum
# array_sum = mylib.mysum(len(array), array)

# print('sum of array: {}'.format(array_sum))
str(path_to_alignment_file).encode('ascii')
str(prefix_for_output_files).encode('ascii')
str(path_to_directory).encode('ascii')

# mylib.main.restype = ctypes.c_longlong
mylib.main.argtypes = [ctypes.c_int, ctypes.char_p,
numpy.ctypeslib.ndpointer(dtype=numpy.int32), numpy.ctypeslib.ndpointer(dtype=numpy.float64)]

# Calling mst-backbone_default_output
data = "H3N2_156"
mst_path = "/home/tikare/MST-Backbone-REPO/"
mst_data_path = "/home/tikare/mst-backbone-repo/data/"
mst_backbone = mst_path + "mst-backbone " + mst_data_path + "data " + "--seq .fasta " + "--size size_of_subtree " + "--out prefix_for_output_files " + "--parallel_comp boolflag " 
sub.call (mst_backbone, shell=True)
#  Fasttree = tool_path + "FastTree -nt " + test_data_path + test_prefix + ".fa > " + test_data_path + test_prefix + ".fastree "
#     sub.call (Fasttree, shell=True)
# int main(int argc, char **argv)
# {	
	

# 	# string path_to_alignment_file;
# 	# fs::path alignment_file_path_obj;
# 	# fs::path prefix_path_obj;
#     # string prefix_for_output_files;
# 	# string path_to_directory;	
#     # int size_of_subtree;
# 	# bool parallel_comp = 0;
# 	# int int_parallel_comp;
#  	# struct stat buffer;
# 	# bool flag_alignment_file = 0;
# 	# bool flag_size_of_subtree = 0;
# 	# bool flag_prefix = 0;
#     if (argc < 2) {        
#         cerr << "Usage: " << argv[0] << " --seq sequence_alignment_file --size size_of_subtree --out prefix_for_output_files --parallel_comp boolflag" << endl;
#         return (-1);
#     } else {        
#         // parse arguments            
#         for (int i = 1; i < argc ; i++) {
#         // path to multiple sequence alignment file
#             if (strcmp(argv[i], "--seq") == 0) {				
#                 if (i < argc -1) {
# 					flag_alignment_file = 1;
#                     path_to_alignment_file = argv[++i];
# 					cout << "alignment file name is " << path_to_alignment_file << endl;
# 					if (stat (path_to_alignment_file.c_str(), &buffer) != 0) { // check if input file exists
# 						cout << "Please check if the input filename is correct" << endl;
# 						exit (-1);
# 					}
# 					alignment_file_path_obj = path_to_alignment_file;
#                 }
#         // prefix_to_output_files (e.g. prefix is "covid-19_size_42" and the alignment is in directory "/foo/bar/data/")
# 		// newick file is stored as /foo/bar/data/covid-19_size_42.newick
# 		// log file is stored as /foo/bar/data/covid-19_size_42.mstbackbone_log
#             } else if (strcmp(argv[i], "--out") == 0) {
#                 if (i < argc -1) {
# 					flag_prefix = 1;
#                     prefix_for_output_files = argv[++i];
# 					// prefix_for_output_files = alignment_file_path_obj.parent_path().string() + prefix_for_output_files;
# 					prefix_path_obj =  alignment_file_path_obj.parent_path();
# 					prefix_path_obj /= prefix_for_output_files;
# 					cout << "prefix for output files is" << prefix_for_output_files << endl;					
#                 }
#         // size of subtree Vs
#             } else if (strcmp(argv[i], "--size") == 0) {
#                 if (i < argc -1) {
# 					flag_size_of_subtree = 1;
#                     size_of_subtree = stoi(argv[++i]);
#                 }
# 			}  else if (strcmp(argv[i], "--parallel_comp") == 0) {
#                 if (i < argc -1) {
# 					int_parallel_comp = stoi(argv[++i]);
# 					// cout << "input for parallel_comp is " << stoi(argv[++i]) << endl;					
# 					if (int_parallel_comp == 0 || int_parallel_comp == 1) {
# 						parallel_comp = (bool) int_parallel_comp;
# 						cout << "flag is either 0 or 1" << endl;
# 					} else {						
# 						parallel_comp = 0;
# 					}                 
#                 }
# 			}        
#         }

# 		if (!flag_size_of_subtree) {
# 			size_of_subtree = 10;
# 		}

# 		if (!flag_prefix) {
# 			prefix_path_obj =  alignment_file_path_obj.parent_path();
# 			prefix_path_obj /= "mst-backbone_default_output";			
# 			// prefix_for_output_files = path_obj.parent_path().string() + "mst_backbone";
# 		}
# 		cout << "Calling MSTbackbone " << endl;
# 		MSTBackbone MSTBackboneObj(path_to_alignment_file, size_of_subtree, prefix_path_obj.string(),parallel_comp);
#     }

# 	return 0;
# } 