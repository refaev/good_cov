# good_cov
A basic simulation for 3D ray projection 

Usage:

    import basic_simulation

    my_map = basic_simulation.create_map(100)

    loc = np.asarray([80, 50])

    points = basic_simulation.render(my_map=my_map, loc=loc)
  

Display:

    plt.imshow(my_map)

    plt.plot(points[:, 1], points[:, 0], 'or')

    plt.plot(loc[1], loc[0], '*g')

    plt.show()

