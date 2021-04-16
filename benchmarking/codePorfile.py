import cProfile
cProfile.run("[x for x in range(1500)]")
#         4 function calls in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
ncalls is the number of calls made.
tottime is a total of the time spent in the given function.
percall refers to the quotient of tottime divided by ncalls
cumtime is the cumulative time spent in this and all subfunctions. It’s even accurate for recursive functions!
The second percall column is the quotient of cumtime divided by primitive calls
filename:lineno(function) provides the respective data of each function
'''

### python -m cProfile test.py

