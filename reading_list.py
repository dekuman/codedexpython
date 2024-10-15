
books= ['Zero to One','The Lean Startup','The Mom Test','Make It Stick','Life in Code']

print(books)

books.append('Zero to Sold')
print(books)

books.remove('Zero to One')
print(books)

books.pop(0)
print(books)

newbooks=books.copy()

print('new books are=', newbooks)

books.extend(newbooks)
print('extended list=', books)

print('index of a book= ',books.index('Life in Code'))

reversebook=newbooks.reverse()
print('reverse of a list= ', reversebook)


print('THe number of item "The Mom Test" appears= ', books.count('The Mom Test'))


for i in newbooks:
    print (i)










