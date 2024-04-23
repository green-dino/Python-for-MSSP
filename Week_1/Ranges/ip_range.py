# Define a variable to hold a string representing the base address
baseAddress = "172.20.4."

# Define a list of host addresses using the range function
# This will give us values of 0 to 19
hostAddresses = range(128)

# Define a list that will hold the resulting IP strings
# This starts out as a simple empty list
ipRange = []

# Loop through the host addresses stored in hostAddresses
# We will append the combined IP strings to the ipRange list
for i in hostAddresses:
    # Append the combined IP strings to the ipRange list
    # By concatenating the base address string with the string value of the integer
    ipRange.append(baseAddress + str(i))

# Print out each IP address in the ipRange list on a separate line
# We loop through the ipRange list object one entry at a time
for ipAddr in ipRange:
    print(ipAddr)
