import numpy as n
import matplotlib.pyplot as plt

# square box, with dimensions linearly dependent, alpha = 3:
sequence = n.arange(1, 6, 0.1)  # sequential
samples = n.random.uniform(1, 6, 100)  # in random order

volume_sequence = sequence ** 3
volume_samples = samples ** 3

prob_sequence = 1 / volume_sequence
prob_samples = 1 / volume_samples

x_sequence = n.log(sequence)
y_sequence = n.log(prob_sequence)

x_samples = n.log(samples)
y_samples = n.log(prob_samples)

m, b = n.polyfit(x_samples, y_samples, 1)
plt.plot(x_sequence, y_sequence, 'r-', label='sequence')
plt.plot(x_samples, y_samples, 'bo', label='samples')
plt.title(f'a = {m:10.4f}, b = {b:10.4f}')
plt.show()

######
# box, with dimensions holding nonlinear restrictions, alpha = 2.3
sequence = n.arange(1, 6, 0.1)  # sequential
samples = n.random.uniform(1, 6, 100)  # in random order

x = sequence
y = 2 * sequence ** 0.3
z = 0.2 * sequence ** 0.9
volume_sequence = x * y * z

x = samples
y = 2 * samples ** 0.3
z = 0.2 * samples ** 0.9
volume_samples = x * y * z

prob_sequence = 1 / volume_sequence
prob_samples = 1 / volume_samples

x_sequence = n.log(sequence)
y_sequence = n.log(prob_sequence)

x_samples = n.log(samples)
y_samples = n.log(prob_samples)

m, b = n.polyfit(x_samples, y_samples, 1)
plt.plot(x_sequence, y_sequence, 'r-', label='sequence')
plt.plot(x_samples, y_samples, 'bo', label='samples')
plt.title(f'a = {m:10.4f}, b = {b:10.4f}')
plt.show()

# x, y, z sono quantità
# portions of resources of type x, y, z
# e.g.:
# time:
#    x time allocated by a person or gorup to civil engineering
#    y time allocated to architecture
#    z time allocated to construction
# knowledge:
#    x knowledge of a person or group about civil engineering
#    y knowledge of a person or group about architecture
#    z knowledge of a person or group about construction
# size:
#    as demonstrated above for alpha = 3 and 2.3

# if x, y, z are abstract concepts, such as money, intelligence, free time
# we may consider them as proxies for indirect communication.
#      Such as termites use nest and contruction to reach Collective intelligence and a Cognitive map.
#     We humans present stigmergy using x, y, z as proxies for indirect communication.
#     We can think X, Y, Z as the quantity allocated by all mankind, or a team. That is: X = sum(x_i), all person i
# e.g.:
#   se:
#     pessoa(1): x = 10, y = 20, z = 30
#     pessoa(2): x = 20, y = 0, z = 40
#   then:
#     estas duas pessoas tem repertório em comum sobre x e z
#     mas não sobre y
#     ou seja:
#       pessoa(1) se comunicou com a pessoa(2) indiretamente
#       pessoa(1) e pessoa(2) podem se comunicar sobre x e z e:
# 
#    finally:
#       society form a network of indirect communication:
#           such as termites
#       bipartite:
#           people and resources
#           people hold nonlinear combinations of resources
#           the equanimous distribution of resources among people througth volume
#           imply in the power-law distribution of resources among people
