####
# box, don't compete in space (box can be inside box)

# 100 boxes, x y z:

# 100 volumes:

# 100 probabilities:

# plot:

# plot log log:

# quantities in box X Y Z completelly full in every size:

# quantities in box X Y Z with frac f of empty space:

####
# box, compete in space (box can't be inside box)
# there is empty space, thus f > 0
# say:
f = 0.5  # that is, boxes tend to occupy half of the empty space
free_space = X * Y * Z * f

# case 2.1) total priority to bigger objects:
# biggest boxes get their space first
# then with the remaining space free_space = (free_space - box_space) * f
# the smaller boxes are input

# case 2.2) total priority to smaller objects:
# smallest boxes get their space first
# then with the remaining space free_space = (free_space - box_space) * f
# the bigger boxes are input

# case 2.3) priority to random size:
# box siz is put in random order
# then with the remaining space free_space = (free_space - box_space) * f


####
# box that exist are boxes that best survived the creation and all modifications on the space
# creation
# fitness
#   optimum size of box
#   less space occupied
# population variation:
#   box cross-over
#   box mutation
#   box transformation
# tendecy of the modification on status (each step: p(box length = 1) = 0.5, that is:
#   in each step the length can tur into 1 flip a coin. The boxes will tend to be 1111, or 11xyz, that is: they will tend to zero elements and converge to 11111. These are the surviving boxes.
# noise:
#    random insertion of new values in the population

