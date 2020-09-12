#The input format:
# Two lines: first the spin of the particle, 
# then its charge. You do NOT have to convert 
# these values to floats.

# The output format:
# The particle and its class separated by a space.

input1 = input()
input2 = input()

if input1 == "1/2" and input2 == "-1/3":
    print("Strange Quark")

if input1 == "1/2" and input2 == "2/3":
    print("Charm Quark")

if input1 == "1/2" and input2 == "-1":
    print("Electron Lepton")

if input1 == "1/2" and input2 == "0":
    print("Neutrino Lepton")

if input1 == "1" and input2 == "0":
    print("Photon Boson")



# Interesting method
# a = {
#     "1/2 -1/3": "Strange Quark",
#     "1/2 2/3": "Charm Quark", 
#     "1/2 -1": "Electron Lepton",   
#     "1/2 0": "Neutrino Lepton",
#     "1 0": "Photon Boson"}
#
# spin = str(input())
# charge = str(input())
# print(a[spin + " " + charge])