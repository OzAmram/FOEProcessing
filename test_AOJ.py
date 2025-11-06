import h5py
import sys
import numpy as np
import matplotlib.pyplot as plt

""" Example script of how to read AOJ h5 files
    Usage : python test.py FILENAME
"""



fname = sys.argv[1]
f = h5py.File(fname, "r")

print("Here are all the keys in the h5 file:")
print(list(f.keys()))
jets = f['jet_kinematics'][:]
#event_info = f['event_info'][:]
#jet_constituents = f['PFCands'][:]
#jet_tagging = f['jet_tagging'][:]

print("There are %i jets in the dataset" % jets.shape[0])


print("Here are the 4 vectors (pt, eta, phi, M) of the first 5 jets")
print(jets[:5])
print("Here are the 4 vectors (px,py,pz,E) of the constituents of the first jet")
print(f['PFCands'][0, :, :4])

print('This is the pt range of the jets', np.amin(jets[:,0]), np.amax(jets[:,0]))


print("Now making a histogram of the jet pts : jet_pts.png")
plt.figure()
plt.hist(jets[:,0], bins = 50)
plt.xlim([200., 1000.])
plt.xlabel("jet pt (GeV)")
plt.savefig("jet_pts.png")



print("Now making a histogram of the leading jet constituent energy : jet_const_E.png")
E = f['PFCands'][:,0, 3]
plt.figure()
plt.hist(E, bins = 100, range=(0, 500))
plt.xlim([0., 500.])
plt.xlabel("Leading jet constituent energy (GeV)")
plt.savefig("jet_const_E.png")

f.close()
