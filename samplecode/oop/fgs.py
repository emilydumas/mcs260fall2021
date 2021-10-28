"Lazy finite geometric sequence example"

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
        print("FGS.__getitem__({}) was called".format(idx))
        if idx < 0 or idx >= self.length:
            # The requested index is not valid
            raise IndexError("this FGS has {} terms and so index {} is invalid".format(
                self.length,
                idx
            ))
        return self.start * (self.ratio ** idx)

    
