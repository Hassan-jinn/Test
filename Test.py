import os, sys, platform

bit = platform.architecture()[0]
try:
    if bit == '64bit':
        print("Running on 64-bit architecture...")
        import Nalla_8_enc
    elif bit == '32bit':
        print("Running on 32-bit architecture...")
        import Nalla_8_enc
    else:
        print("Unknown architecture.")
except ModuleNotFoundError:
    print(f"Nalla_8_enc module not found for {bit} architecture.")
    sys.exit(1)
