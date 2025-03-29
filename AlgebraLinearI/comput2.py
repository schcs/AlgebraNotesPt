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



def sum_embed( mylist ):

    len_mylist = len( mylist )
    if len_mylist == 1 and not isinstance( mylist[0], list ):
        return mylist[0]
    elif len_mylist == 1 and isinstance( mylist[0], list ):
        return sum_embed( mylist[0] )
    else: 
        mid = len_mylist//2
        return sum_embed( mylist[:mid] ) + sum_embed( mylist[mid:] )

print( sum_embed( [[1],[2,[3,4]],[[10,11]]] ))