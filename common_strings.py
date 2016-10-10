import os.path
import sys
import time
from pprint import pprint

def main():
    count = solution_part_a()
    print count

def solution_part_a():
    '''
    Assumptions:
        - The machine running this program has at least 1 GB of RAM
        - Strings in each text file are unicode UTF-8 (8 bits in length). Total size of each file
        would be approx. 1M lines * 32 characters/line * 1 byte/character = 32 MB
        - Since both files are sufficiently small - they can fit in RAM with sufficient space left over, thus,
        the program can reasonably read in and process both files in main memory.
        - This solution would not be a good one for part B. See explanation.

    Solution Description:
        - To count the common elements between two collections, we can use an approach where we first filter each
        collection down to unique elements only (use Python set). Then we can find the elements common to both 
        collections by finding the intersection of the two collections (use Python intersection). Last, we can 
        count the number of elements in the resulting intersection.

    '''

    # Get filepaths from stdin
    filepaths = get_args() 

    #start = time.time()
    #filepaths = ['data/strings1.txt','data/strings2.txt']

    # Preprocess files
    #start_preprocess = time.time()
    results = preprocess_files(filepaths)
    #print '\nTime to preprocess files %s' % str((time.time()-start_preprocess))

    # Count common strings between files
    #start_count = time.time()
    count = count_common_strings(*results)
    #print '\nTime to count common strings %s' % str((time.time()-start_count))
    #print 'Total time elapsed %s ' % str(time.time() - start)

    return count

def solution_part_b():
    '''
    The solution for part A will not work well for files with 1 billion strings. 
    Using the same assumption about the string encoding, the approximate size of 
    a single file would be 32 GB. Unless we were running the program on a machine
    with RAM sufficiently greater than 32 GB, the solution to part A would 
    simply not work.

    Even if we did have a machine with enough RAM, there is probably a more time
    efficient way to solve the problem. My approach for large data like this would
    be to use a slightly different algorithm for counting the common strings. The 
    new algorithm would be to sort each file, use a function to find the unique
    strings in each file, and then a function to find the intersection between
    the two sets of unique elements. 

    After some research, I've found that there are several built-in unix 
    programs (sort, uniq, comm) that are better suited for large data sets. 
    Source: http://stackoverflow.com/questions/373810/unix-command-to-find-lines-common-in-two-files

    Unix sort uses an external mergesort algorithm, where if the input data 
    cannot be sorted and stored in RAM, it sorts the data in chunks and 
    temporarily stores chunks on disk.
    Source: https://en.wikipedia.org/wiki/External_sorting

    Additionally, I've noticed that the bottleneck in preprocessing is in 
    extracting the unique strings. Unix sort offers options to parallelize
    the sort and increase RAM usage for buffering. By default, unix sort is
    set to utilize 50 percent of RAM and # of availabe processors on the system. 
    If my machine is not doing much more than performing this task, I would 
    increase the RAM to maybe 70 percent and then set sort's
    parallel option equal max # of cores available.
    '''
    pass


def get_args():
    ''' Read in 2 arguments from user '''
    arg_count = 1
    filepaths = []
    
    while arg_count <= 2:
        line = raw_input("Enter the file path for file # %s: " % str(arg_count))
        filepaths.append(line.strip())
        arg_count+=1

    return filepaths

def count_common_strings(*list_of_sets):
    ''' Returns strings common to sets in list_of_sets. If list_of_sets is empty, then return -1'''

    if list_of_sets:
        return len(set.intersection(*list_of_sets))
    else:
        print 'No common strings exist because input collections are empty!'
        return -1

def preprocess_files(filepaths):
    ''' Preprocess files - extract unique strings from each file'''
    
    if validate_files(filepaths):
        return map(preprocess_file,filepaths)
    else:
        print 'Exiting program, one or more files did not exist!'
        sys.exit(1)
        

def preprocess_file(filepath):
    ''' Extract only the unique strings from file '''

    try:
        unique_lines = []
        with open(filepath, 'r') as data_file:
            #start = time.time()
            unique_lines = set(data_file.readlines())
            #print 'Time to read and find unique lines %s' % str(time.time() - start)
            
            return unique_lines

    except IOError:
        print 'Exiting program, error reading file: %s!' % filepath
        sys.exit(1)
    

def validate_files(filepaths):
    ''' Validate all filepaths - true iff all files are valid'''
    
    if filepaths:
        return all([validate_file(filepath) for filepath in filepaths])
    else:
        return False


def validate_file(filepath):
    ''' Check if file exists and it is a text file'''
    # http://stackoverflow.com/questions/2472221/how-to-check-if-a-file-is-a-textfile
    
    # Does file exist
    valid_file = os.path.isfile(filepath)
    if valid_file:
        # Is it a text file
        import mimetypes
        if mimetypes.guess_type(filepath)[0] != 'text/plain':
            valid_file = False
            print '%s Not a valid text file!' % filepath
    else:
        print 'File %s does not exist!' % filepath

    return valid_file


if __name__ == '__main__':
	main()