def hyp_squared(file_name):
    values = open(file_name, "rt").read().split() # read the dataset downloaded from Rosalina
    return int(values[0])**2 + int(values[1])**2 # make them integers and return the square values