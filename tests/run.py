
try:
  import mcpi
except Exception as e:
  print("Failed to import the package 'mcpi'.")
  print("Probably, it has not been installed from the local repository.")
  print("Run the following command from the repository's directory first.")
  print("")
  print("    python -m pip install .")
  print("")
  exit(-1)

print("The package 'mcpi' has been successfully imported.")
print("mcpi version: {}".format(mcpi.__version__))
print("")

n = 1000000
pi = mcpi.mcpi(n)

print("samples = {}".format(n))
print("π ~ {}".format(pi))
print("")

print("Run the following command to uninstall the package 'mcpi'.")
print("")
print("    python -m pip uninstall mcpi")
print("")
