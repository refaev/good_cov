import numpy as np
import matplotlib.pyplot as plt


def create_map(sz: int = 100) -> np.ndarray:
    my_map = np.zeros((sz, sz))
    my_map[30:50, 30:50] = 1
    my_map[10:20, 30:50] = 1
    my_map[40:50, 80:100] = 1
    my_map[80:100, 80:100] = 1
    my_map[20:90, 10:20] = 1
    #plt.imshow(my_map)
    return my_map


def render(my_map: np.ndarray, loc: np.ndarray):
    points = []
    for ang in range(0, 360, 10):
        point = project_ray(my_map, loc, ang)
        points.append(point)
    points = np.asarray(points)
    return points


def project_ray(my_map: np.ndarray, loc: np.ndarray, ang: int) -> np.ndarray:
    ang_rad = np.pi*ang/180.
    depth = my_map.shape[0]
    ray_end = np.asarray([loc[0] + 1.5*depth*np.sin(ang_rad),loc[1] + 1.5*depth*np.cos(ang_rad)])
    # plt.plot(ray_end[1], ray_end[0],'xb')
    res = find_first_one_on_ray(my_map, loc, ray_end)
    return res


def find_first_one_on_ray(my_map: np.ndarray, loc: np.ndarray, ray_end: np.ndarray) -> np.ndarray:
    depth = max(np.abs(loc[0]-ray_end[0]),np.abs(loc[1]-ray_end[1]))
    step = 1/float(depth)
    for alpha in np.arange(0,1,step):
        new_loc = alpha*ray_end + (1-alpha)*loc
        new_loc = np.round(new_loc).astype(int)
        if new_loc[0] < 0 or new_loc[0] >= my_map.shape[0] or new_loc[1] < 0 or new_loc[1] >= my_map.shape[1]:
            return [None, None]
        elif my_map[new_loc[0], new_loc[1]]:
            return new_loc
    return [None, None]


def main():
    # Usage:
    my_map = create_map(100)
    loc = np.asarray([80, 50])
    points = render(my_map=my_map, loc=loc)

    # Display:
    plt.imshow(my_map)
    plt.plot(points[:, 1], points[:, 0], 'or')
    plt.plot(loc[1], loc[0], '*g')
    plt.show()


if __name__ == '__main__':
    main()

