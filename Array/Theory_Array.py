
#Theory
"""
 -->>   What is Array ?
            An array is a collection of items of the same variable type that are stored at contiguous memory locations.
            It is one of the most popular and simple data structures used in programming.

 -->>   Basic terminologies of Array
            Array Element: Elements are items stored in an array.
            Array Index: Elements are accessed by their indexes. Indexes in most of the programming languages start from 0.

 -->>   Memory representation of Array
            In an array, all the elements or their references are stored in contiguous memory locations.
            This allows for efficient access and manipulation of elements.

 -->>   Why do we Need Arrays?
            Assume there is a class of five students and if we have to keep records of their marks in examination then,
            we can do this by declaring five variables individual and keeping track of records but what
            if the number of students becomes very large,
            it would be challenging to manipulate and maintain the data. So we use an array of students.

 -->>   Types of Arrays
            1) On the basis of Size   -->  Fixed Sized Arrays , Dynamic Sized Arrays
            2) On the basis of Dimensions  -->  One-dimensional Array(1-D Array) , Multi-dimensional Array

 -->>   Array Types On the basis of Size :
        1. Fixed Sized Arrays :
            We cannot alter or update the size of this array. Here only a fixed size (i,e. the size that is mentioned in square brackets [])
            of memory will be allocated for storage.In case, we don't know the size of the array then
            if we declare a larger size and store a lesser number of elements, it will result in a wastage of memory.
            And if we declare a lesser size than the number of elements then we won't get enough memory to store all the elements.

            example : arr = [0] * 5          this will Create a fixed-size list of length 5

       2. Dynamic Sized Arrays :
            The size of the array changes as per user requirements during execution of code so the coders do not have to worry about sizes.
            They can add and removed the elements as per the need. The memory is mostly dynamically allocated and de-allocated in these arrays.

            example :  arr = []

-->    Arrays on the basis of Dimensions :
       1. One-dimensional Array(1-D Array) :
          You can imagine a 1d array as a row, where elements are stored one after another.

          example : arr = [1,2,3,4]

      2. Multi-dimensional Array:
         A multi-dimensional array is an array with more than one dimension.
         We can use multidimensional array to store complex data in the form of tables, etc.
         We can have 2-D arrays, 3-D arrays, 4-D arrays and so on.

         Two-Dimensional Array(2-D Array or Matrix):
         2-D Multidimensional arrays can be considered as an array of arrays or as a matrix consisting of rows and columns.

         example : A 2D array representing a 3x3 matrix
                    matrix = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]

                    print(matrix)

         refer notes  for array in this folder.
         refer this link for video tutorial : https://www.youtube.com/watch?v=pmN9ExDf3yQ


"""

