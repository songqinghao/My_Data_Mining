import numpy as np
dt = np.dtype(np.int32)
print(dt)
print(type(dt))

student = np.dtype([("NAME","S20"),("AGE","i4"),("MARKS","i4")])
print(student)
print(type(student))