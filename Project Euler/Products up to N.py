def productsoffirstNnumbers(n):
    product=1
    for k in range(2,n+1):
        product=product*k
    return product

print(productsoffirstNnumbers(500))