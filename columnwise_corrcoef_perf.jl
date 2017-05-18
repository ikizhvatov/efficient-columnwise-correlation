# This is columnwise correlation in Julia, to compare with numpy.
# Julia designers were smart enough to implement the built-in cor function
# that computes correaltion columnwise.
#
# Ilya Kizhvatov, with help from Cees-Bart Breunesse

# system information
versioninfo()

# dummy arrays for the dry run
foo = rand(Float64, 100000, 1000)
bar = rand(Float64, 100000, 256)

# arrays representing real data
O = rand(Float64, 100000, 1000)
P = rand(Float64, 100000, 256)

# timing dry run to compile the function and the timing functions
println("Dry run...")
@time cor(foo, bar)

# real timing
println("Real run...")
@time cor(O, P)
