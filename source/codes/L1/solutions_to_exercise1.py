
# Exercise 1

# Problem 1

from shapely.geometry import Point, LineString, Polygon

# problem 1 Point

def createPointGeom(x_coord, y_coord):
    # create a shapely Point geometry object and return that
    new_point = Point(x_coord, y_coord)
    return new_point


point1 = createPointGeom(2.2, 4.2)

point2 = createPointGeom(7.2, -25.1)

point3 = createPointGeom(9.26, -2.456)


# problem 1 Linestring

def createLineGeom(points_list):
    # Function should first check that the input list really contains Shapely Point(s)
    for p in points_list:
        if not isinstance(p, Point):
            print("point {} is not a Point object".format(str(p)))
            # there are more sophisticated ways to check that, and make the program safer to bad input -> later
    # takes a list of Shapely Point objects as parameter and returns a LineString object of those input points
    new_line = LineString(points_list)
    return new_line


list_of_points = [point1, point2, point3]

line1 = createLineGeom(list_of_points)


# problem 1 Polygon

def createPolyGeom(input_list):
    # input list should contain either points or coords
    # we can call shapely Polygon only with coord list, so we need to check
    first_data = input_list[0]
    if isinstance(first_data, Point):
        poly_from_points = Polygon([[p.x, p.y] for p in input_list])
        return poly_from_points
    else:
        new_poly = Polygon(input_list)
        return new_poly


coord_list = [(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)]

poly1 = createPolyGeom(coord_list)

list_of_points = [point1, point2, point3]

poly2 = createPolyGeom(coord_list)

# problem 2 getCentroid()

def getCentroid(geom):
    return geom.centroid


point1_centroid = getCentroid(point1)
line1_centroid = getCentroid(line1)
poly2_centroid = getCentroid(poly2)


# problem 2 getArea()

def getArea(test_poly):
    if isinstance(test_poly, Polygon):
        return test_poly.area
    else:
        print("error, is not a Polygon")


# problem 2 getLength()

line1_area = getArea(line1)
poly1_area = getArea(poly1)
