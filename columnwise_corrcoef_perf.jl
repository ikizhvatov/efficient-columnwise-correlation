# This is columnwise correlation in Julia, to compare with numpy.
# Julia designers were smart enough to implement the built-in cor function
# that computes correaltion columnwise.
#
# Ilya Kizhvatov, with help from Cees-Bart Breunesse

# system information
versioninfo()

# setup
O = rand(Float64, 100000, 1000)
P = rand(Float64, 100000, 256)

# timing
@time cor(O, P)
