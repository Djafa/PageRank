#author Elio, Djaf
import numpy as np

def pageRankScore(mat1, alpha):
    #we initialise en empty matrix (full of zero) that will be the transition probability matrix
    transitionMatrix = np.zeros(shape=(len(mat1),len(mat1)))
    #the loop for the transtion matrix line's
    for line in range (0, len(mat1)):
      #the loop for the transition matrix column's
      for column in range (0,len(mat1)):
        #we apply the matrix probability method to get all the value in the transitionMatrix
        transitionMatrix [line][column] = mat1[line][column]/np.sum(mat1[line])

    #after checking that the matrix was stochaistic (the sum of every line =1), let's do the Google matrix
    #the formula of the Google Matrix : G[i][j]= alpha*transitionMatrix[i][j] + (1-alpha)* (1/N) where N = number of pages/nodes
    googleMatrix = np.zeros(shape=(len(transitionMatrix), len(transitionMatrix)))
    #We apply the formule above
    for line in range (0, len(googleMatrix)):
        for column in range (0, len(googleMatrix)):
            googleMatrix[line][column]= alpha*transitionMatrix[line][column] + (1-alpha)* (1.0/len(googleMatrix))
    #let's now do the powerMethod in order to find the eigen vector of the google matrix which is simply the pageRankScore of each page
    #first , we create the vector that we need to multiply with the google matrix, this vector will be the final pageRank solution
    vectorPageRank = np.zeros(shape=(len(mat1),1))
    #We make the addition of every column in the adjacency matrix and we store the result in a list
    listOfColumnSum = mat1.sum(axis = 0)
    #we fill the initial vector of Pgae rank with the correct value stored in the list listOfColumnSum
    for fillin in range (0, len(listOfColumnSum)):
        vectorPageRank[fillin][0] = listOfColumnSum[fillin]/ np.sum(mat1)
    #Before computing the power method, we initialise an error margin wich will indicates us that the method found a convergence point
    gamma = 10**-6
    #we create a boolean to go out of the loop as soon as we get a good result, I prefer use a boolean instead of a break statement
    finish = False
    while(not(finish)):
        #we store the value of the Page rank vector at the next iteration we take the transpose of the google
        nextVectorPageRank = np.dot(np.transpose(googleMatrix), vectorPageRank)
        #we compare the vector at the previous iteration and at the next iteration to see wheter the solution is stabilized, the method .all() compare every elements of each vector
        if (abs(nextVectorPageRank - vectorPageRank < gamma )).all():
            #we change the boolean of the while loop
            finish = True
            #we return the last iteration with the highest accuracy
            print (nextVectorPageRank)
        #if the error degree stills to big, we go for an other iteration
        vectorPageRank = nextVectorPageRank
    
def main():
 # we open the file with it's location, in this case, it's in the same folder as the code , no need to print the path
 fichier = open("matrice-adjacence.csv")
 #we are going to read the first line of the document
 contenu = fichier.readline()
 # the dimension of the matrix according to the previous line (we divide it by 2 because the comas are counted)
 dimOfMatrix = int(len(contenu)/2)
 # we initialise a empty matrix (full of zeros)
 matrice = np.zeros(shape=(dimOfMatrix,dimOfMatrix))
 # we create a list for a later use which will count 2 by 2 until the end of the line which is read (to avoid the comas)
 advance = list(range(0,len(contenu),2))
 # this variable will help us to keep track of the matrix line that we are filling
 line = 0
 # that will be our stop condition, whend the variable "contenu" refers to an empty string, that mean that we've reached the end of the file
 while not(contenu ==""):
  # we set up the column to the matrix at zero at each iteration to be able to fill the matrix iteratively   
  column = 0 
  for j in advance:
       # we fill the matrix with the elements inside "contenu", j grows 2 by 2 because we don't need comas in our matrix!
       matrice[line][column]=float(contenu[j])
       #we increment the column to go to the next one
       column +=1 
  line +=1
  # that's the statement that will continue or not the loop
  contenu = fichier.readline()
 # to avoid possible future problems, we have to close the file
 fichier.close()
 pageRankScore(matrice, alpha=0.9)

main()

