"Lazy finite geometric sequence example"
# MCS 260 Fall 2021 Lecture 28

class FGS:
    "Lazy finite geometric sequence"
    def __init__(self,start,ratio,length):
        """
        Initialize a finite geometric sequence with first value
        `start`, ratio of successive terms `ratio`, and total
        number of terms `length`.
        """
        self.start = start
        self.ratio = ratio
        self.length = length
    def __len__(self):
        "number of terms"
        return self.length
    def __getitem__(self,idx):
        """
        compute and return the element of the geometric sequence
        at index `idx`
        """
	# uncomment next line to get notification of each call
        # print("FGS.__getitem__({}) was called".format(idx))
        if idx < 0 or idx >= self.length:
            # The requested index is not valid
            raise IndexError("this FGS has {} terms and so index {} is invalid".format(
                self.length,
                idx
            ))
        return self.start * (self.ratio ** idx)

    def __setitem__(self,idx,val):
        if idx == 0:
            self.start = val
        else:
            raise IndexError("FGS only supports item assignment at index 0")
