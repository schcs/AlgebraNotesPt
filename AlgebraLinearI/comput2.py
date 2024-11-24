from sympy import *

def elementary_matrix( n, i, j ):
    mat = Matrix.zeros( n, n )
    mat[i,j] = 1
    return mat

def matrix_of_matrix_mult( A ):
     
    n = A.rows
    mat = Matrix.zeros(n**2, n**2)
    for i in range( n ):
        for j in range( n ):
            print( i, j )
            # put in the coordinates of E_{i,j}
            mat[j*n:(j+1)*n,i*n+j] = A[:,j]

    return mat

def adjacency_matrix( n, edge_list ):
    mat = Matriz.zeros( n, n )
    for e in edge_list:
        mat[e[0],e[1]] = mat[e[1],e[0]] = 1
        
    return mat 
