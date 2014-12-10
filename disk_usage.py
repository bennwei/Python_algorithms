import os

def disk_usage(path):
    """ 
    Return the number of bytes used by a file/folder and any descendents.
    """
    
    total = os.path.getsize(path) # count direct usage
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print '{0:<10} {1}'.format(total, path)
    return total
