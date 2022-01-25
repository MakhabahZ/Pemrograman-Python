import turtle #mengimport turtle graphics
turtle.bgcolor("black") #background
turtle.pensize(5) #ukuran garis

#Pendefinisian warna dan radius
def circle(radius,color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
turtle.goto(-30,-280) #pergeseran x dan y
circle(300,'red') #Radius x dan y dan besaran lingkaran

turtle.goto(-30,-240) #pergeseran x dan y
circle(260,'white') #Radius x dan y dan besaran lingkaran

turtle.goto(-30,-200) #pergeseran x dan y
circle(220,'red') #Radius x dan y dan besaran lingkaran

turtle.goto(-30,-160) #pergeseran x dan y
circle(180,'blue') #Radius x dan y dan besaran lingkaran

turtle.goto(-200,75) #radius x dan y
turtle.begin_fill()
turtle.color('white')

#Perulangan dalam membuat bintang
for i in range(5):
    turtle.forward(340) #ukuran bintang
    turtle.right(144) #arah pergerakan garis
turtle.end_fill()

turtle.hideturtle() #menghilangkan pen


turtle.done()