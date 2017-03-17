

# Aice(Yanlin) Li's  Assignment 2
## SID 998303301 

## Part 1: Image Processing Basics

Computers use tiny dots called _pixels_ to display images. Each pixel is stored as an array of numbers that represent color intensities.

__Example.__ In an 8-bit grayscale image, each pixel is a single number. The number represents light intensity ranging from black (0) to white (255).

__Example.__ In a 24-bit RGB color image, each pixel is an array of 3 numbers. These numbers range from 0 to 255 and represent red, green, and blue intensity, respectively. For instance, `(0, 0, 255)` is <span style="color:#00F">bright blue</span> and `(255, 128, 0)` is <span style="color:#FF8000">orange</span>.

In this assignment, you'll use Python and NumPy to manipulate 24-bit RGB color images.

You can use `Image.open()` from the Python imaging library (PIL) to open an image:


```python
from PIL import Image
# Cat image from https://unsplash.com/photos/FqkBXo2Nkq0
cat_img = Image.open("cat.png")
```

Images display inline in Jupyter notebooks:


```python
cat_img
```




![png](output_3_0.png)



In a Python terminal, you can display the image in a new window with `.show()` instead.

NumPy can convert images to arrays:


```python
import numpy as np
cat = np.array(cat_img)
```

To convert an array back to an image (for display) use the function below:


```python
def as_image(x):
    """Convert an ndarray to an Image.
    
    Args:
        x (ndarray): The array of pixels.
        
    Returns:
        Image: The Image object.
    """
    return Image.fromarray(np.uint8(x))
```

__Exercise 1.1.__ How many dimensions does the `cat` array have? What does each dimension represent?


```python
#print cat
cat.shape
```




    (267, 400, 3)



__Comment__ : 3 dimension. Each dimension represent a color channel . Picture consist of 267*400 pixels points, each pixel has 3 numbers representing the intensity of red(x-axis), green(y-axis) and blue(z-axis). 

__Exercise 1.2.__ Use `.copy()` to copy the cat array to a new variable. Swap the green(1) and blue(2) color channels in the copy. Display the result.


```python
BigCat = cat.copy()
BigCat[:,:,1] = cat[:,:,2]
BigCat[:,:,2] = cat[:,:,1]
def as_image(x):
    return Image.fromarray(np.uint8(x))
as_image(BigCat)

```




![png](output_12_0.png)



__Exercise 1.3.__ Why is `.copy()` necessary in exercise 1.2? What happens if you don't use `.copy()`?


```python
type(cat)
```




    numpy.ndarray



__Comment:__ .copy() means shallow copy. 'cat' is a array, which is mutable. Instead of copyng, '=' creates bindings ('deep copy') between a target and an object for mutable items, we don't want to do that, we simply wants to copy the value of cat. So .()copy is needed so one can change one copy without changing the other. 

__Exercise 1.4.__ Flip the blue(2) color channel from left to right. Display the resulting image. _Hint: see the NumPy documentation on array manipulation routines._


```python
Cat14 = cat.copy()
Cat14[:, :, 2] = np.fliplr(Cat14[:, :, 2])
Image.fromarray(np.uint8(Cat14))
```




![png](output_17_0.png)



## Part 2: Singular Value Decomposition

Suppose $X$ is an $n \times p$ matrix (for instance, one color channel of the cat image). The _singular value decomposition_ (SVD) factors $X$ as $X = UD V^T$, where:

* $U$ is an $n \times n$ orthogonal matrix
* $D$ is an $n \times p$ matrix with zeroes everywhere except the diagonal
* $V$ is an $p \times p$ orthogonal matrix

Note that a matrix $A$ is _orthogonal_ when $A^T A = I$ and $AA^T = I$.

__Example.__ We can use NumPy to compute the SVD for a matrix:


```python
x = np.array(
    [[0, 2, 3],
     [3, 2, 1]]
)
u, d, vt = np.linalg.svd(x)
# Here d is 2x2 because NumPy only returns the diagonal of D.
print "u is:\n", u, "\nd is:\n", d, "\nv^T is:\n", vt
```

    u is:
    [[-0.68145174 -0.73186305]
     [-0.73186305  0.68145174]] 
    d is:
    [ 4.52966162  2.54600974] 
    v^T is:
    [[-0.48471372 -0.62402665 -0.6128975 ]
     [ 0.80296442 -0.03960025 -0.59470998]
     [ 0.34684399 -0.78039897  0.52026598]]


If we let

* $u_i$ denote the $i$th column of $U$
* $d_i$ denote the $i$th diagonal element of $D$
* $v_i$ denote the $i$th column of $V$

then we can write the SVD as $\ X = UDV^T = d_1 u_1 v_1^T + \ldots + d_m u_m v_m^T\ $ using the rules of matrix multiplication. In other words, the SVD decomposes $X$ into a sum!

If we eliminate some of the terms in the sum, we get a simple approximation for $X$. For instance, we could eliminate all but first 3 terms to get the approximation $X \approx d_1 u_1 v_1^T + d_2 u_2 v_2^T + d_3 u_3 v_3^T$. This is the same as if we:

* Zero all but the first 3 diagonal elements of $D$ to get $D_3$, then compute $X \approx UD_3V^T$
* Eliminate all but the first 3 columns of $V$ to get $p \times 3$ matrix $V_3$, then compute $X \approx UDV_3^T$

We always eliminate terms starting from the end rather than the beginning, because these terms contribute the least to $X$.

Why would we want to approximate a matrix $X$?

In statistics, _principal components analysis_ uses this approximation to reduce the dimension (number of covariates) in a  centered (mean 0) data set. The vectors $d_i u_i$ are called the _principal components_ of $X$. The vectors $v_i^T$ are called the _basis vectors_. Note that both depend on $X$. The dimension is reduced by using the first $q$ principal components instead of the original $p$ covariates. In other words, the $n \times p$ data $X$ is replaced by the $n \times q$ data $UD_q = XV_q$

In computing, this approximation is sometimes used to reduce the number of bits needed to store a matrix (or image). If $q$ terms are kept, then only $nq + pq$ values (for $XV_q$ and $V_q^T$) need to be stored instead of the uncompressed $np$ values.

__Exercise 2.1.__ Write the functions described below.

* A function that takes a matrix $X$ and returns its principal component matrix $XV_q$ and basis matrix $V_q^T$. This function should also take the number of terms kept $q$ as an argument.

* A function that takes a principal component matrix $XV_q$ and basis matrix $V_q^T$ and returns an approximation $\hat{X}$ for the original matrix.

As usual, make sure to document your functions. Test your function on the red color channel of the cat image. What's the smallest number of terms where the cat is still recognizable as a cat?


```python
def fun1(Red,q):
    """ Function takes Red(matrix X) and number of terms kept K 
        Apply SVD decompostion
        Return XVq and basis VqT
    """
    u, d, vt = np.linalg.svd(Red) 
    return Red.dot(vt[0:q,:].T),vt[0:q,:] 

def fun2(XVq,VqT):
    """
    Function takes the output from funciton1, apply dot product to return the approx X 
    """
    return XVq.dot(VqT)
```


```python
import numpy as np
Red = cat[:,:,0]
q=13
Image.fromarray(np.uint8(fun2(*fun1(Red,q))))
```




![png](output_22_0.png)



__Comment: __ I asked my roommate what can you see from the picture without giving her any information about the picture. She recognize it's a cat with a flag when I set q to be 13. So approximately 13 is the smallest number of terms where the cat is still recognizable as a cat. But different people may have slightly different imagination. 

__Exercise 2.2.__ You can check the number of bytes used by a NumPy array with the `.nbytes` attribute. How many bytes does the red color channel of the cat image use? How many bytes does the compressed version use when 10 terms are kept? What percentage of the original size is this?


```python
p=10

#if we don't take the difference in bytes for different data type into consideration 
print "percentage of compressed version in the original size without taking consideration of each entry type: "
print float(fun1(Red,p)[0].nbytes+fun1(Red,p)[1].nbytes)/(float(Red.nbytes))
print '\n'

#if we take the difference in bytes for different data type into consideration 
print 'data type in XVq: ',fun1(Red,p)[0].dtype
print 'data type in VqT: ',fun1(Red,p)[1].dtype
print "data type in Red Matrix: ",Red.dtype
print '\n'

print 'size of XVq: ',fun1(Red,p)[0].shape
print 'size of VqT: ',fun1(Red,p)[1].shape
print 'size of original matrix Red: ',Red.shape
print '\n'

print 'total bytes of XVq: ',(fun1(Red,p)[0].nbytes)
print 'total bytes of VqT: ',fun1(Red,p)[1].nbytes
print 'total bytes of compressed version:',(fun1(Red,p)[0].nbytes)+(fun1(Red,p)[1].nbytes)
print 'total bytes of Red Matrix:', Red.nbytes
print '\n'

print "byte for each entry in XVq:",(fun1(Red,p)[0].nbytes)/(267*10)
print "byte for each entry in VqT:",fun1(Red,p)[1].nbytes/(10*400)
print "byte for each entry in Red Matrix:",Red.nbytes/(106800)
print '\n'

print "percentage of compressed version in the original size with taking consideration of each entry type"
print float(fun1(Red,p)[0].nbytes+fun1(Red,p)[1].nbytes)/(float(Red.nbytes)*8)

```

    percentage of compressed version in the original size without taking consideration of each entry type: 
    0.499625468165
    
    
    data type in XVq:  float64
    data type in VqT:  float64
    data type in Red Matrix:  uint8
    
    
    size of XVq:  (267, 10)
    size of VqT:  (10, 400)
    size of original matrix Red:  (267, 400)
    
    
    total bytes of XVq:  21360
    total bytes of VqT:  32000
    total bytes of compressed version: 53360
    total bytes of Red Matrix: 106800
    
    
    byte for each entry in XVq: 8
    byte for each entry in VqT: 8
    byte for each entry in Red Matrix: 1
    
    
    percentage of compressed version in the original size with taking consideration of each entry type
    0.0624531835206


__ Commment__ : 
Red color channel of the cat image use 106800 bytes of int8 entries.  
The compressed version use when 10 terms are kept has total of 53360 bytes of float64 entries.
If we do NOT take the entries type difference into consideration, the compression version is around 50% of the original size. If we take entries type difference into consideration, and say if we save all of the int8 entries of Red color channel as float64 entries, the compression version is around 6.24% of the Red color matrix. 


```python

```
