"""COMP1730/6730 assignment template.

Semester 1, 2019.

Co-authors: <u6516811>, <u5960101>
"""

from visualise import *
import  numpy as np
import math


# Load data - do not change this function
def load_heightmap(path):
    """Loads a heightmap dataset.

    Parameters
    ----------
    path : str
        Path to the heightmap data.

    Returns
    -------
    List of lists
        A list of lists containing the heightmap. Each list is
        a row of the map.
        (0, 0) is the top left corner of the heightmap.
    """
    import numpy as np
    return [list(row) for row in np.loadtxt(path)]


# Question 1.
def cells_above_height(heightmap,height):
    '''This function is to figure out how much cells is above given height

    input:
        heightmap: the map with the format n by n matrix
        height: given specific height level

    output:
        n_cells: the integer number of the cell that above given height
    '''
    n_cells = 0
    for row in heightmap:
        for cell in row:
            if cell > height:          # if the value of the cell is greater than given height level
                n_cells += 1
    return n_cells


def area_above_water(heightmap, water_level):
    '''
    This function is to calculate how much area in a map is above water given the water level.
    And assuming that each cell in a map is 1 metre by 1 metre

    input:
        heightmap: the map with the format n by n matrix
        water_level: given specific water level

    output:
        how much the area of the map is above water in hectares.
    '''
    return cells_above_height(heightmap, water_level)/1000000   # divided by the 1000000 is to transform the square meter to hectares


# Question 2.
def highest_point(heightmap):
    '''
    This function is going to compute the highest point of the given the map.

    input:
        heightmap: the map with the format n by n matrix

    output:
        the highest point as a tuple of (x,y) coordinate

    '''
    temp = np.array(heightmap)
    raw, column = temp.shape
    _position = np.argmax(temp)    # find the maximum value of the array
    #  find the index of the maximum value
    m, n = divmod(_position, column)  # row = index / width   columns = index % width

    return n, m     # inverse the coordinate



# Question 3.
def slope(heightmap, x, y):
    '''
    This function is to calculate the steepness, or slop, of each cell in the heightmap.
    The algorithm is :
            1. for each cell, subtract the height of the cell on its left from the cell on its right, so-call "horizontal gradient"
            2. for each cell, subtract the height of the cell above it from the cell below it, so-call "vertical gradient"
            3. Square both gradients, then add them together and take the square root

    Assuming that if edge-case happens, then return 0.

    input:
        heightmap: the map with the format n by n matrix
        x, y :  these two are the coordinate of the given point， should be integer number
    ouput:
        slop: the total gradient of the given point
    '''
    heightmap = np.array(heightmap)
    row, colums = np.shape(heightmap)
    if (x == 0 or x >= row-1):        # edge-case, x=0 or x= last row
        return 0
    if (y == 0 or y >= colums-1):   # edge-case, y=0 or y=last colunms
        return 0
    horizontal_gradient = heightmap[y, x+1] - heightmap [y, x-1]    # computing the "horizontal gradient"
    vertical_gradient = heightmap[y+1, x] - heightmap [y-1, x]      # computing the "vertical gradient"
    slop = np.sqrt(horizontal_gradient**2 + vertical_gradient**2)   # the third step described above

    return  slop

def aspect(heightmap, x, y):
    '''
    This function is to compute the aspect of the given point (x,y) in heightmap
    The algorithm is :
            1. for each cell, subtract the height of the cell on its left from the cell on its right, so-call "horizontal gradient"
            2. for each cell, subtract the height of the cell above it from the cell below it, so-call "vertical gradient"
            3. calculate the aspect using :
                            alpha = arctan(vertical gradient, horizontal gradient)

    Assuming that if edge-case happens, then return 0.

    input:
        heightmap: the map with the format n by n matrix
        x, y :  these two are the coordinate of the given point, should be integer number
    ouput:
        alpha: the aspect of the given point

    '''
    heightmap = np.array(heightmap)
    row, colums = np.shape(heightmap)
    if (y == 0 or y >= row-1):          # edge-case, x=0 or x= last row
        return 0
    if (x == 0 or x >= colums-1):       # edge-case, y=0 or y= last colunms
        return 0
    delta_x = heightmap[y, x+1] - heightmap [y, x-1]    # computing the "horizontal gradient"
    delta_y = heightmap[y+1, x] - heightmap [y-1, x]    # computing the "vertical gradient"
    if delta_x == 0:
        delta_x =  1e-6
    alpha = math.atan2(delta_y, delta_x)            # the third step described above


    return alpha


# Question 4.
def find_path(heightmap, x, y, water_level=557):
    '''
    This function is to take a heightmap and a starting position, and then to calculate the path that from the starting point
    to the adjacent cell with the lowest points. This will stop until all adjacent cells have an elevation that is equal to or
    higher than the current cell, or when it reaches the water level. Finally this function will return a list of tuples of
    the (x ,y) coordinates of the cells along the route


    input:
        heihtmap: the map with the format n by n matrix
        x, y : the coordinates of the point, should be integer number
        water_level: the value of the water_level

    ouput:
        path: a list of tuples of the (x ,y) coordinates of the cells along the route

    '''

    heightmap = np.array(heightmap)
    row, colums = np.shape(heightmap)
    current_position = heightmap[y, x]    # obatin the current value of the current position
    if x == 0:          # edge-case, x=0 or x= last row
        right = heightmap[y, x + 1]
        left = right + 1
        up = heightmap[y - 1, x]
        down = heightmap[y + 1, x]
    elif x >= row-1:
        left = heightmap[y, x - 1]
        right = left + 1
        up = heightmap[y - 1, x]
        down = heightmap[y + 1, x]
    elif y == 0:
        right = heightmap[ y, x + 1]
        left = heightmap[y, x - 1]
        up = right + 1
        down = heightmap[y + 1, x]
    elif y >= colums-1:       # edge-case, y=0 or y= last colunms
        right = heightmap[ y, x + 1]
        left = heightmap[y, x - 1]
        up = heightmap[y - 1, x]
        down = up + 1
    else:
        right = heightmap[y, x + 1]       # the following four commands are to obtain the value of the neighbour points of the current cell
        left = heightmap[y, x - 1]
        up = heightmap[y - 1, x]
        down = heightmap[y + 1, x]

    po = [right, left, up, down]  # form a matrix
    path = [(x, y)]        #inital the path
    min_position = min(right, left, up, down)     # find the minimum value among the neighbour points
    while current_position > min_position and current_position > water_level:      # conditions whether need to stop
        if po.index(min_position) == 0: # right
            x += 1
        elif po.index(min_position) == 1:   # left
            x -= 1
        elif po.index(min_position) == 2:   # up
            y -= 1
        elif po.index(min_position) == 3:   # down
            y +=1

        current_position = heightmap[y, x]         # update the current value of the new points

        right = heightmap[y, x + 1]     # update the value of the neighbour points
        left = heightmap[y, x - 1]
        up = heightmap[y - 1, x]
        down = heightmap[y + 1, x]
        po = [right, left, up, down]

        min_position = min(right, left, up, down)           # continue to find the minimum point

        path.append((x, y))    # update the path until stop

    return path


# Question 5.
def find_buildings(buildings_heightmap):
    '''
    This function is to find all the buildings in the given map, assuming that if two non-zero cells
    are next to each other, then they are part of the same building.This function also contain
    three sub-function, which are "LableConnected4", "EquivalentLabel" and "swap".
    The algorithm is fundamentally based on theConnected-component labeling. After using the
    4-connectivity method that only North and West neighbours of the current pixel, we then merge the
    equivalent label using the EquivalentLabelPairs.

    The algorithm is :
        On the first pass:
            Iterate through each element of the data by column, then by row (Raster Scanning)
            If the element is not the background
            Get the neighboring elements of the current element
            If there are no neighbors, uniquely label the current element and continue
            Otherwise, find the neighbor with the smallest label and assign it to the current element
            Store the equivalence between neighboring labels
        On the second pass:

            Iterate through each element of the data by column, then by row
            If the element is not the background
            Relabel the element with the lowest equivalent label

    input:
        buildings_heightmap: a building map with the format n by n matrix

    ouput:
        index: a list of sets. Each set should contain the coordinates of a single building (stored as tuples of the (x,y)
                coordinates of all the cells of the building)
    '''
    def LableConnected4(M, labelM, eqLable):
        row = M.shape[0]
        col = M.shape[1]

        labelNo = 0
        R = 0
        for C in range(0, col):
            if M[R, C] == 1:
                if C == 0:
                    labelNo += 1
                    labelM[R, C] = labelNo
                else:
                    if labelM[R, C - 1] != 0:
                        labelM[R, C] = labelM[R, C - 1]
                    elif labelM[R, C - 1] == 0:
                        labelNo += 1
                        labelM[R, C] = labelNo

        for R in range(1, row):
            for C in range(0, col):
                if M[R, C] == 1:
                    if C == 0:
                        if M[R - 1, C] == 0:
                            labelNo += 1
                            labelM[R, C] = labelNo
                        else:
                            labelM[R, C] = labelM[R - 1, C]
                    else:
                        if M[R - 1, C] + M[R, C - 1] == 0:
                            labelNo += 1
                            labelM[R, C] = labelNo
                        elif M[R - 1, C] + M[R, C - 1] == 1:
                            labelM[R, C] = max(labelM[R - 1, C], labelM[R, C - 1])
                        else:
                            labelM[R, C] = min(labelM[R - 1, C], labelM[R, C - 1])
                            if labelM[R - 1, C] != labelM[R, C - 1]:
                                if [labelM[R - 1, C], labelM[R, C - 1]] not in eqLable:
                                    eqLable.append([labelM[R - 1, C], labelM[R, C - 1]])

        return labelNo

    def EquivalentLabel(N, labelM, eqLable):
        L = {}
        invalidLabel = []  # the invalid label number in equivalent label pairs
        for i in range(1, N + 1):

            if i in invalidLabel:  # if i is an invalid label
                continue

            L[i] = []
            for j in range(0, len(eqLable)):
                if i in eqLable[j]:
                    invalidLabel.append(max(eqLable[j]))
                    L[i].append(max(eqLable[j]))

            for k in L[i]:  # deep search
                for j in range(0, len(eqLable)):
                    if (k in eqLable[j]) & (max(eqLable[j]) != k):
                        invalidLabel.append(max(eqLable[j]))
                        L[i].append(max(eqLable[j]))

        trueLable = 1
        for k in L:
            labelM[labelM == k] = trueLable
            for labelNo in L[k]:
                labelM[labelM == labelNo] = trueLable
            trueLable += 1

    def swap(array):
        temp = []
        for i in range(len(array)):
            a = array[i]
            a = [a[1], a[0]]
            temp.append(a)

        return temp

    heightmap = np.array(buildings_heightmap)
    heightmap = np.int64(heightmap > 0)           # convert to 1 if the value is non-zero
    labelM = np.zeros(heightmap.shape)             # create a label matrix with the shape of the given map
    eqLabel = []                                    # equivalent label matrix
    labelNo = LableConnected4(heightmap, labelM, eqLabel)    # obtain the total label number
    EquivalentLabel(labelNo, labelM, eqLabel)      # merge the equivalent label

    index = []
    temp = []
    for i in range(1, labelNo+1):
        # find the each set containing the coordinates of a single building
        temp = np.argwhere(labelM == i)
        # find the all the coordinates of points in each set
        index.append(swap(temp))            # swap is to invert x,y coordinates

    return index

# Question 6.
def line_of_sight(ground_heightmap, building_heightmap, x1, y1, x2, y2):
    '''
    This function is to takes a ground heightmap, a building heightmap, and two coordinates (x1, y1) and (x2,y2),
    and returns a list of heights between each position. It is basically implemented by using Bresenham's line algorithm.
	1. Assume that as long as two non-zero cells are next to each other, then they are part of the same building.
    2. Assume that the map is the square, which means that the input matrix should be the N by N matrix.
    3. Assume that all the input is available for the map, which means that the input two coordinates belong to the size of map and should be the integer number.
    4. Ignoring the height of people in this implementation.
    5. Assume that as long as one of part of HIAF can be seen, we would say it is visible.

    input:
        ground_heightmap: the ground map with the format n by n matrix
        building_heightmap: the building map with the format n by n matrix
        x1,y1: the coordinate of starting point
        x2,y2: the coordinate of ending point

    output:
        height_val: a list of heights between each position
    '''
    ground_heightmap = np.array(ground_heightmap)
    building_heightmap = np.array(building_heightmap)

    def bresenham(x0, y0, x1, y1):
        """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
        Input coordinates should be integers.
        The result will contain both the start and the end point.
        """
        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:               #slop < 1
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2 * dy - dx
        y = 0

        for x in range(dx + 1):      # from x0 to x1
            yield x0 + x * xx + y * yx, y0 + x * xy + y * yy      # return the involved (x,y) coordinate
            if D >= 0:
                y += 1
                D -= 2 * dx
            D += 2 * dy

    # start to calculate the real height with ground level.
    height = ground_heightmap + building_heightmap
    # all the coordinates involved
    index = list(bresenham(y1, x1, y2, x2))             # find the path between each position

    height_val = []
    for i in range(len(index)):
        height_val.append(height[index[i]])             # find the height value of each position

    return height_val


def is_hiaf_visible(ground_heightmap, building_heightmap, x, y, hiaf_x=337, hiaf_y=423):
    '''
    This function is to takes a ground heightmap, a building heightmap, and two coordinates (x1, y1) and (x2,y2),
    and returns False or True to decide whter the HAIF is invisible or visible.
    It is basically implemented by using Bresenham's line algorithm and algorithm described in report.

    Assume that as long as one of part of HIAF can be seen, we would say it is visible.
    Ignoring the height of people.
    input:
        ground_heightmap: the ground map with the format n by n matrix
        building_heightmap: the building map with the format n by n matrix
        x1,y1: the coordinate of starting point
        x2,y2: the coordinate of ending point

    output:
        True: The HAIF is visible
        False : The HAIF is invisible
    '''
    ground_heightmap = np.array(ground_heightmap)
    building_heightmap = np.array(building_heightmap)
    # compute the high value of the path
    def bresenham(x0, y0, x1, y1):
        """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
        Input coordinates should be integers.
        The result will contain both the start and the end point.
        """
        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2 * dy - dx
        y = 0

        for x in range(dx + 1):
            yield x0 + x * xx + y * yx, y0 + x * xy + y * yy
            if D >= 0:
                y += 1
                D -= 2 * dx
            D += 2 * dy

    # start to calculate the real height with ground level.
    height = ground_heightmap + building_heightmap
    height_HIAF = height[hiaf_y, hiaf_x]
    HIAF_cor = (hiaf_y, hiaf_x, height_HIAF)

    # starting point
    start_point = height[y, x]
    start_cor = (y, x, start_point)
    index = list(bresenham(y, x, hiaf_y, hiaf_x))       # find the path between each position
    height_val = line_of_sight(ground_heightmap, building_heightmap, x, y, hiaf_x, hiaf_y)

    new_cor = []
    for i in range(len(index)):
        x = index[i]
        new_cor.append((x[0],x[1], height_val[i]))

    # starting points ---> HAIF
    Start_to_HAIF = np.abs(HIAF_cor[2] - start_cor[2])/np.sqrt((HIAF_cor[1] - start_cor[1])**2 +(HIAF_cor[0] - start_cor[0])**2 )

    #starting points ---> points of the path
    s_distance = []
    for i in range(1,len(index)):
         temp = new_cor[i]
         s_distance.append(np.abs(temp[2] - start_cor[2])/np.sqrt((temp[1] - start_cor[1])**2 + (temp[0] - start_cor[0])**2))
    print(s_distance)

    for i in range (len(s_distance)):
        if s_distance[i] >= Start_to_HAIF:
            return False
        else:
            return True






if __name__ == "__main__":
    # If you want to run any of the functions in this assignment, do so from here.


    # For example, if you uncomment the following lines they will load and visualise a heightmap
    # that should look similar to the one in the assignment specification.
    # heightmap = load_heightmap("height_anu.txt")
    # buildings = load_heightmap("buildings_anu.txt")
    # # n_cells = area_above_water(heightmap,557)
    # # print(n_cells)
    #
    # heightmap = np.array(heightmap)
    # buildings = np.array(buildings)
    # map = heightmap + buildings
    # index =  highest_point(map)
    # print(index)
    # print(map[index[1], index[0]])
    # combined_heightmap = [[heightmap[y][x] + buildings[y][x] for x in range(len(buildings[0]))] for y in range(len(buildings))]
    # visualise_heightmap(combined_heightmap)
    #visualise_slope(slope, heightmap)
    #visualise_aspect(aspect, heightmap)
    # visualise_path(heightmap, find_path, 450, 350)
    #visualise_buildings(find_buildings(heightmap), heightmap)
    #visualise_line_of_sight(heightmap, buildings, 120, 200, 337, 423, line_of_sight)
    pass



