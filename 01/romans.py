def int_to_roman (num):


    val = [1000, 900, 500, 400, 100, 90 ,50 ,40 , 10 ,9 ,5, 4, 1]
    rom = ["M", "CM", "VD", "CD", "C" , "XC" ,"L" ,"XL", "X", "IX" , "V" , "IV" ,"I"]    

   
    romano = ''
    i = 0
    

    while  num > 0:

        for x in range (num // val [i]):
            num -= val[i]    
            romano += rom[i] 
        i += 1  

    return romano







