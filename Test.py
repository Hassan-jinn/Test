import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    import Nalla_8_enc
elif bit == '32bit':
    import Nalla_8_enc
