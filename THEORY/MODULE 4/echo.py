import sys

print("RUNNING FILE =", __file__)
print("ARGV =", sys.argv)

for arg in sys.argv:
    print(arg)  # команда  python echo.py test --user -hello some text
