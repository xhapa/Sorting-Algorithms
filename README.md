# Sorting-Algorithms
This program was for brush up my skill of advance python and algorithms, where I used pygame for make it visual. I decided to implement 4 algorithms Burble sort, Insertion sort, Merge sort and Quick sort, the last two applying the concept of divide and conquer that is very interesting in algorithms.

<p align="center">
  <img  src="https://i.imgur.com/YAGhzrP.png" width="350" height="245" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img  src="https://i.imgur.com/xYUiioj.png" width="350" height="245" />
</p>

## How did I split the image?
For split in columns I taked the pixel array of the image and divide it on columns of 1px by 400px, and for each column I gave a value or weight that helped to sort the matrix(vector) of values. After I asigned a pygame.Rect object with their coordenates (x,y) for each column slice to be able to draw them.
## About sorting algorithms
### Burble sort
This algorithm consist in compare two consecutive elements of a list and swap them to sort, the time complexity in average case of ![formula](https://render.githubusercontent.com/render/math?math=\Theta(n^2)). 
### Insertion sort
This algorithm is very simple and consist in take a list and for each element take it and insert in the correct position, the time complexity in average case of ![formula](https://render.githubusercontent.com/render/math?math=\Theta(n^2)).
### Merge sort
This algorithm consist in take a list an divide or split in half parts, after compare and decide to divide or swap values when the list have only one element it start to join them, the time complexity in average case of ![formula](https://render.githubusercontent.com/render/math?math=\Theta(n\log_2n)).  
### Quick sort
This algorithms consist in create a partion of the original list and start to swap values and the ordered values with others, in each run the partion complete the list, the time complexity in average case of ![formula](https://render.githubusercontent.com/render/math?math=\Theta(n\log_2n)).

For more about it, see "[Sorting Algorithms](https://en.wikipedia.org/wiki/Sorting_algorithm)"
## How to run it?
For run it you must have Python > 3.9.

Install the other requirements by:

```
pip install -r requirements.txt
```
### For work with virtual env

Create a virtual environment on your working directory by:

For windows:
```
py -m venv env
```
Activate with:

```
.\env\Scripts\activate
```
After install the requirements.

## Contributing
1. Fork or Clone the repository

2. Create a branch

3. Push your changes to GitHub

4. Submit your changes for review
