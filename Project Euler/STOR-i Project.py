import random as random
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy import integrate


class Graph:
    def __init__(self, v=None, e=None):
        self.vertex = v
        self.edges = e

    def __repr__(self):
        return str(self.vertex) + ", " + str(self.edges)

    def points_connected(self):
        num_points = len(self.vertex)
        degrees = [0] * num_points
        edges = self.edges
        for indices in edges:
            degrees[indices[0]-1] += 1
            degrees[indices[1]-1] += 1
        return degrees


def random_coordinates_generator(n):  # Function returns N random coordinates in [0,1]^2
    random_x_coordinates = []
    random_y_coordinates = []
    for j in range(1, n+1):
        random_x_coordinates.append(random.uniform(0, 1))
        random_y_coordinates.append(random.uniform(0, 1))

    return [random_x_coordinates, random_y_coordinates]


def random_nodes_drawer(n):
    coordinates = random_coordinates_generator(n)
    plt.scatter(coordinates[0], coordinates[1])

# Here I add that nodes on our random graph will be connected depending on the outcome of a bernoulli(p) RV
# where p denotes the distance between the nodes / sqrt(2) (NORMALISING CONSTANT)


def euclidean_norm(p1, p2):
    x_change = abs(p1[0]-p2[0])
    y_change = abs(p1[1]-p2[1])
    dist = math.sqrt((x_change ** 2) + (y_change ** 2))
    return dist


def random_nodes_connector(array, p):  # Note this array should be of a particular form, all x coordinates first.
    set_coordinates = []
    edges = []
    number_of_coorindates = len(array[0])
    for j in range(0, number_of_coorindates):
        new_coordinates = [array[0][j], array[1][j]]
        set_coordinates.append(new_coordinates)
    plt.scatter(array[0], array[1])
    for i in range(0, number_of_coorindates):
        plt.text(set_coordinates[i][0] * (1 + 0.02), set_coordinates[i][1] * (1 + 0.02), i+1, fontsize=6)
        for j in range(i+1, number_of_coorindates):
            if np.random.binomial(1, p) == 1:
                x_val_1 = set_coordinates[i][0]
                x_val_2 = set_coordinates[j][0]
                y_val_1 = set_coordinates[i][1]
                y_val_2 = set_coordinates[j][1]
                edges.append([i+1, j+1])
                plt.plot([x_val_1, x_val_2], [y_val_1, y_val_2], 'black')
            else:
                continue
    plt.draw()
    graph = Graph(set_coordinates, edges)
    return graph


def graph_drawer(graph_object):  # HERE this function will draw the graph g.
    vertices = graph_object.vertex
    x_coordinates = []
    y_coordinates = []
    num_coordinates = len(vertices)
    set_coordinates = graph_object.vertex
    for j in range(0, num_coordinates):
        x_coordinates.append(vertices[j][0])
        y_coordinates.append(vertices[j][1])
        plt.text(set_coordinates[j][0] * (1 + 0.01), set_coordinates[j][1] * (1 + 0.01), j + 1, fontsize=6)
    x_connected = []
    y_connected = []
    edges = graph_object.edges
    plt.scatter(x_coordinates, y_coordinates, color='black', marker='.')
    for point in edges:
        x_val_1 = vertices[point[0]-1][0]
        x_val_2 = vertices[point[1]-1][0]
        y_val_1 = vertices[point[0]-1][1]
        y_val_2 = vertices[point[1]-1][1]
        x_connected.append(x_val_1)
        x_connected.append(x_val_2)
        y_connected.append(y_val_1)
        y_connected.append(y_val_2)
        plt.plot([x_val_1, x_val_2], [y_val_1, y_val_2], 'black')
    plt.draw()


def degree_bar(graph):  # Input should be a graph.
    degrees = graph.points_connected()
    set_degree = set(degrees)
    list_degree = list(set_degree)
    frequency = []
    for d in set_degree:
        count = Counter(degrees)
        frequency.append(count[d])

    plt.bar(list_degree, frequency, width=0.4, color='blueviolet')
    plt.xlabel('Degrees')
    plt.ylabel('Frequency')
    plt.title('Degrees and Frequencies')


def degree_distribution_bar(graph):
    degrees = graph.points_connected()
    num_points = len(degrees)
    set_degree = set(degrees)
    list_degree = list(set_degree)
    frequency = []
    for d in set_degree:
        count = Counter(degrees)
        frequency.append(count[d]/num_points)

    plt.bar(list_degree, frequency, width=0.4, color='blueviolet')
    plt.xlabel('Degrees')
    plt.ylabel('Frequency')
    plt.title('Degrees and Frequencies')


def nodes_drawer(array):
    num_coordinates = len(array)
    x_coordinates = []
    y_coordinates = []
    for j in range(0, num_coordinates):
        x_coordinates.append(array[j][0])
        y_coordinates.append(array[j][1])

    plt.scatter(x_coordinates, y_coordinates, color="turquoise")


def graphon_graph_generator(array, w):  # array the coordinates of points. (given as list), w is the Graphon.
    n = len(array)
    random_indexes = list(np.random.uniform(0, 1, n))
    nodes_drawer(array)
    for i in range(0, n):
        for j in range(0, n):
            p = w(random_indexes[i], random_indexes[j])
            if np.random.binomial(1, p) == 1:
                plt.plot([array[i][0], array[j][0]], [array[i][1], array[j][1]], color="turquoise")
            else:
                continue


def adjacency_matrix(g):  # g will be a graph input
    num_vertex = len(g.vertex)
    matrix = np.zeros(shape=(num_vertex, num_vertex))  # Initialise the matrix to be 0's
    for edge in g.edges:
        row_index = edge[0]-1
        column_index = edge[1]-1
        matrix[row_index][column_index] = 1
        matrix[column_index][row_index] = 1
    return matrix


def network_density(graph):
    n = len(graph.vertex)
    num_edges = len(graph.edges)
    max_edges = math.factorial(n) / (math.factorial(n-2) * 2)
    density = num_edges / max_edges
    return density


# Description: h is the vector that denotes the groupings of the n nodes.
# Description: x denotes the input of the cdf. ie, the ouput of the function will be P(H <= x)
# Description: g denotes the graph (unclear if we need it as of now)

def cumalative_distribution(h, x):
    num_nodes = sum(h)
    num_groups = len(h)
    if x < 1:
        return 0
    elif x >= num_groups:
        return 1
    else:
        if math.floor(x) == 1:
            return h[0] / num_nodes
        else:
            proportion = 0
            for j in range(0, math.floor(x)):
                proportion += h[j]
            return proportion / num_nodes


def cumalative_vector(h):
    num_nodes = sum(h)
    num_groups = len(h)
    cum_vector = [0]
    cumalative_value = 0
    for j in range(0, num_groups):
        cumalative_value += h[j]
        cum_vector.append(cumalative_value)
    for j in range(0, len(cum_vector)):
        cum_vector[j] = cum_vector[j] * 1/num_nodes
    return cum_vector


def cumalative_inverse(h, p):
    num_groups = len(h)
    for j in range(1, num_groups+1):
        if cumalative_distribution(h, j) >= p:
            return j
        else:
            continue


# n denotes the number of points. w denotes the graphon that we wish to use to be the limit of our sequence.

def sequence_graph_uni(w, n):
    uniform_values = list(np.random.uniform(0, 1, n))
    adjacency = np.zeros(shape=(n, n))
    for i in range(1, n):
        for j in range(0, i):
            if np.random.binomial(1, w(uniform_values[i], uniform_values[j])) == 1:
                adjacency[i][j] = 1
                adjacency[j][i] = 1
            else:
                continue
    matrix = np.array(adjacency)
    return matrix

def sequence_graph_det(w, n):
    increment = 1 / n
    det_values = []
    end_p = 0
    for j in range(0, n-1):
        end_p += increment
        det_values.append(end_p)
    end_p += increment
    if end_p > 1:
        det_values.append(1)
    else:
        det_values.append(end_p)
    adjacency = np.zeros(shape=(n, n))
    for i in range(1, n):
        for j in range(0, i):
            if np.random.binomial(1, w(det_values[i], det_values[j])) == 1:
                adjacency[i][j] = 1
                adjacency[j][i] = 1
            else:
                continue
    matrix = np.array(adjacency)
    return matrix

def sequence_graph_norm(w, n):
    norm_values = []
    while len(norm_values) != n:
        val = float(np.random.normal(0.5, (1 / 6) ** 2, 1))
        if val > 1 or val < 0:
            continue
        else:
            norm_values.append(val)
    adjacency = np.zeros(shape=(n, n))
    for i in range(1, n):
        for j in range(0, i):
            if np.random.binomial(1, w(norm_values[i], norm_values[j])) == 1:
                adjacency[i][j] = 1
                adjacency[j][i] = 1
            else:
                continue
    matrix = np.array(adjacency)
    return matrix


def constant(x, y):
    return 1

def step_2(x,y):
    if x + y <= 0.5:
        return 0.25
    else:
        return 0.75

def step(x, y):
    if x <= 0.5 and y <= 0.5:
        return 0.25
    elif x <= 0.5 and y > 0.5:
        return 0.5
    elif x > 0.5 and y<= 0.5:
        return 0.5
    else:
        return 0.25


def average(x, y):
    return (x+y) * 0.5


def net_density(adj_mat):
    num_nodes = adj_mat.shape[0]
    num_edges = 0
    for i in range(0, num_nodes):
        for j in range(i+1, num_nodes):
            num_edges += adj_mat[i][j]
    numerator = math.factorial(num_nodes)
    denominator = 2 * math.factorial(num_nodes - 2)
    max_edges = numerator / denominator
    return num_edges / max_edges


# Note 1: Adj_Mat denotes the adjacency matrix.(In particular should be a Numpy matrix)
# Note 2: h denotes the groupings of the vector.
# Note 3: (x,y) denotes the points at which we wish to evaluate the estimate at.


def estimator(adj_mat, h, x, y, values):
    num_nodes = adj_mat.shape[0]
    cum_vec = cumalative_vector(h)
    length = len(cum_vec)
    end_points_x = []
    end_points_y = []
    for j in range(0, length - 1):
        if cum_vec[j] < x <= cum_vec[j+1]:
            end_points_x.append(cum_vec[j])
            end_points_x.append(cum_vec[j+1])
        else:
            continue
    for j in range(0, length - 1):
        if cum_vec[j] < y <= cum_vec[j+1]:
            end_points_y.append(cum_vec[j])
            end_points_y.append(cum_vec[j+1])
        else:
            continue
    x_values = []
    y_values = []
    for i in range(0, num_nodes):
        if end_points_x[0] < values[i] <= end_points_x[1]:
            x_values.append(values[i])
        else:
            continue
    for i in range(0, num_nodes):
        if end_points_y[0] < values[i] <= end_points_y[1]:
            y_values.append(values[i])
        else:
            continue
    points_in_box = []
    num_x = len(x_values)
    num_y = len(y_values)
    for i in range(0, num_x):
        for j in range(0, num_y):
            if x_values[i] != y_values[j]:
                points_in_box.append([x_values[i], y_values[j]])
    num_points_in_box = len(points_in_box)
    num_connected = 0
    if num_points_in_box != 0:
        for i in range(0, num_points_in_box):
            row = values.index(points_in_box[i][0])
            col = values.index(points_in_box[i][1])
            if adj_mat[row][col] == 1:
                num_connected += 1
            else:
                continue
        block_density = num_connected / num_points_in_box
        net_dens = net_density(adj_mat)
        return block_density * (1/net_dens)
    else:
        return 0

def l2_error(w, n, h, values):  # This function is specialised as we know the approximation will be a step function.
    adj_mat = sequence_graph_uni(w, n)
    c_vec = cumalative_vector(h)
    dim = len(c_vec) - 1
    error = 0
    for i in range(0, dim):
        for j in range(0, dim):
            mid_x = 0.5 * (c_vec[i] + c_vec[i+1])
            mid_y = 0.5 * (c_vec[j] + c_vec[j+1])
            val_in_rectangle = estimator(adj_mat, h, mid_x, mid_y, values)

            def f(x, y):
                return abs(w(x,y) - val_in_rectangle) ** 2
            integral = (integrate.dblquad(f, c_vec[i], c_vec[i+1], lambda x: c_vec[j], lambda x: c_vec[j+1]))[0]
            error += integral
    return error





def l2_error_uni(w, n, h):  # This function is specialised as we know the approximation will be a step function.
    adj_mat = sequence_graph_uni(w, n)
    c_vec = cumalative_vector(h)
    uni_values = list(np.random.uniform(0, 1, n))
    dim = len(c_vec) - 1
    error = 0
    for i in range(0, dim):
        for j in range(0, dim):
            mid_x = 0.5 * (c_vec[i] + c_vec[i+1])
            mid_y = 0.5 * (c_vec[j] + c_vec[j+1])
            val_in_rectangle = estimator(adj_mat, h, mid_x, mid_y, uni_values)

            def f(x, y):
                return abs(w(x,y) - val_in_rectangle) ** 2
            integral = (integrate.dblquad(f, c_vec[i], c_vec[i+1], lambda x: c_vec[j], lambda x: c_vec[j+1]))[0]
            error += integral
    return error


def l2_error_det(w, n, h):
    adj_mat = sequence_graph_det(w, n)
    c_vec = cumalative_vector(h)
    uni_values = list(np.random.uniform(0, 1, n))
    dim = len(c_vec) - 1
    error = 0
    for i in range(0, dim):
        for j in range(0, dim):
            mid_x = 0.5 * (c_vec[i] + c_vec[i + 1])
            mid_y = 0.5 * (c_vec[j] + c_vec[j + 1])
            val_in_rectangle = estimator(adj_mat, h, mid_x, mid_y, uni_values)

            def f(x, y):
                return abs(w(x, y) - val_in_rectangle) ** 2

            integral = (integrate.dblquad(f, c_vec[i], c_vec[i + 1], lambda x: c_vec[j], lambda x: c_vec[j + 1]))[0]
            error += integral
    return error


def l2_error_norm(w, n, h):
    adj_mat = sequence_graph_norm(w, n)
    c_vec = cumalative_vector(h)
    uni_values = list(np.random.uniform(0, 1, n))
    dim = len(c_vec) - 1
    error = 0
    for i in range(0, dim):
        for j in range(0, dim):
            mid_x = 0.5 * (c_vec[i] + c_vec[i + 1])
            mid_y = 0.5 * (c_vec[j] + c_vec[j + 1])
            val_in_rectangle = estimator(adj_mat, h, mid_x, mid_y, uni_values)

            def f(x, y):
                return abs(w(x, y) - val_in_rectangle) ** 2

            integral = (integrate.dblquad(f, c_vec[i], c_vec[i + 1], lambda x: c_vec[j], lambda x: c_vec[j + 1]))[0]
            error += integral
    return error

plt.axis([0, 200, -0.5, 4])
plt.xlabel('Number of Nodes', fontsize=10)
plt.ylabel('L2-Error', fontsize=10)
plt.suptitle('L2 Error in Constant Graphon Approximation')


for num in range(5, 201, 5):
    print(num)
    groupings = [5] * int(num/5)
    assigned_1 = list(np.random.uniform(0, 1, num))
    assigned_2 = []
    assigned_4 = []
    while len(assigned_2) != num:
        val = float(np.random.normal(0.5, (1/6)**2, 1))
        if val > 1 or val < 0:
            continue
        else:
            assigned_2.append(val)
    assigned_3 = []
    increment = 1 / num
    end_p = 0
    for j in range(0, num-1):
        end_p += increment
        assigned_3.append(end_p)
    end_p += increment
    if end_p > 1:
        assigned_3.append(1)
    else:
        assigned_3.append(end_p)
    while len(assigned_4) != num:
        exp = float(np.random.exponential(0.1, 1))
        if exp > 1:
            continue
        else:
            assigned_4.append(exp)
    e_1 = l2_error(constant, num, groupings, assigned_1)
    e_2 = l2_error(constant, num, groupings, assigned_2)
    e_3 = l2_error(constant, num, groupings, assigned_3)
    e_4 = l2_error(constant, num, groupings, assigned_4)
    plt.scatter(num, abs(e_1), color="turquoise")
    plt.scatter(num, abs(e_2), color="orange")
    plt.scatter(num, abs(e_3), color="magenta")
    plt.scatter(num, abs(e_4), color='red')

plt.legend(['Uniform', 'Normal','Deterministic', 'Exponential'])


plt.show()
