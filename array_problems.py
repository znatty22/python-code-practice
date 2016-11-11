

def main():
	ap = ArrayProblems()
	test_reverse(ap)

def test_rotate(ap):
	arr = [1,2,3,4,5,6,7]
	print 'Original arr: %s' % arr
	k = 3
	print 'Shift by %d:  %s' % (k,str(ap.rotate_array(arr,3)))

def test_reverse(ap):
	arr = [1,2,3,4,5,6,7]
	print 'Original arr: %s' % arr
	print 'Reversed: %s' % (str(ap.reverse_array(arr)))
	
def test_search_1d(ap):
	a = [[1,2,3,4],
		[5,6,7,8]]
	target = 7
	found = ap.binary_search(a,target)
	print 'Search for %d: %s' % (target,str(found))	

def test_search_1d(ap):
	a = [1, 5, 6, 10, 15, 16]
	target = 10
	found = ap.binary_search(a,target)
	print 'Search for %d: %s' % (target,str(found))
	
class ArrayProblems:

	def reverse_array(self,arr):
		start = 0
		end = len(arr) - 1
		while(start < end):
			temp = arr[end]
			arr[end] = arr[start]
			arr[start] = temp
			start+=1
			end-=1
		return arr
		
	def rotate_array(self,arr,k=1):
		"""
		Rotate an array k steps to the right.
		Takes O(n*k) time and O(1)
		"""
		for i in range(k):
			self._shift_by_one(arr)
		return arr
	
	def _shift_by_one(self,arr):
		i = 0
		current = 0
		prev = arr[i]
		while i < len(arr) - 1:
			current = arr[i+1]
			arr[i+1] = prev
			prev = current
			i+=1
		
		# Replace first with last
		arr[0] = current
		
		return arr
		
	def binary_search(self,structure,target):
		"""
		Searches a 1D or 2D structure for the target.
		
		Runs binary search algorithm. If structure is 
		1D, run normal binary search. If structure is
		2D, treat structure as 1D but map 1D index to 
		row,col in 2D structure when computing mid element.
		"""
		if not structure:
			return False
		
		start_index = 0
		end_index = self._get_size(structure) - 1
		while(start_index <= end_index):
			# Rounds down to nearest int
			mid_index = int((start_index + end_index)/2)
			# Compute the mid element in structure
			mid_element = self._get_mid(structure,mid_index)
			# Decide which direction to go
			if target == mid_element:
				return True
			elif target < mid_element:
				end_index = mid_index - 1
			else:
				start_index = mid_index + 1
		
		return False
	
	def _get_size(self,structure):
		"""
		Get size of structure, where structure
		can be either 1D or 2D.
		"""
		
		if isinstance(structure,list) and isinstance(structure[0],list):
			size = len(structure) * len(structure[0])
		else:
			size = len(structure)
		
		return size
	
	def _get_mid(self,structure,mid_index):
		"""
		Get the element at mid_index in structure.
		"""
		if isinstance(structure,list) and isinstance(structure[0],list):
			mid_element = self._get_mid_2d(structure,mid_index)
		else:
			mid_element = self._get_mid_1d(structure,mid_index)
		
		return mid_element
		
	def _get_mid_1d(self,arr,idx):
		return arr[idx]
		
	def _get_mid_2d(self,matrix,idx):
		"""
		Given an index from a 1D structure, 
		find the element in the 2D structure.
		"""
		cols = len(matrix[0])
		row = int(idx/cols)
		col = idx - (cols*row)
		return matrix[row][col]
		
if __name__ == '__main__':
	main()