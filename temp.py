
upper = ['w','w','w','w']
lower = ['y','y','y','y']
front = ['b','b','b','b']
back  = ['o','o','o','o']
left  = ['g','g','g','g']
right = ['r','r','r','r']

if((back[0] == 'w') & (upper[1] == 'b') & (right[1] == 'o')):
    print(" Your next move is rp\n")
    n = 1
    return(n)

if((front[3] == 'w') & (right[2] == 'o') & (lower[1] == 'b')):
    print(" Your next move is rr\n")
    n = 1
    return(n)

if((right[3] == 'o') & (lower[3] == 'w') & (back[2] == 'b')):
    print(" Your next move is rr rr\n")
    n = 2
    return(n)

if((upper[0] == 'o') & (left[0] == 'b') & (back[1] == 'w')):
    print(" Your next move is bp rp\n")
    n = 2
    return(n)

if((front[2] == 'o') & (left[3] == 'w') & (lower[0] == 'b')):
    print(" Your next move is dd rr\n")
    n = 2
    return(n)

if((right[3] == 'w') & (lower[3] == 'b') & (back[2] == 'o')):
    print(" Your next move is dp rr\n")
    n = 2
    return(n)

if((back[3] == 'w') & (lower[2] == 'b') & (left[2] == 'o')):
    print(" Your next move is dd dd rr\n")
    n = 3
    return(n)

if((back[3] == 'o') & (lower[2] == 'w') & (left[2] == 'b')):
    print(" Your next mvoe is dp rr rr\n")
    n = 3
    return(n)

if((back[0] == 'b') & (upper[1] == 'o') & (right[1] == 'w')):
    print(" Your next move is rr dp rr\n")
    n = 3
    return(n)

if((front[3] == 'b') & (right[2] == 'w') & (lower[1] == 'o')):
    print(" Your next move is rp dp rr\n")
    n = 3
    return(n)

if((front[3] == 'o') & (right[2] == 'b') & (lower[1] == 'w')):
    print(" Your next move is dd rr rr\n")
    n = 3
    return(n)

if((front[1] == 'w') & (upper[3] == 'o') & (right[0] == 'b')):
    print(" Your next move is rp dd rr rr\n")
    n = 4
    return(n)

if((front[1] == 'o') & (upper[3] == 'b') & (right[0] == 'w')):
    print(" Your next move is rr rr dp rr\n")
    n = 4
    return(n)

if((back[0] == 'o') & (upper[1] == 'w') & (right[1] == 'b')):
    print(" Your next move is uu rp up rr\n")
    n = 4
    return(n)
        
if((upper[0] == 'w') & (left[0] == 'o') & (back[1] == 'b')):
    print(" Your next move is bb bb rr rr\n")
    n = 4
    return(n)

if((front[2] == 'b') & (left[3] == 'o') & (lower[0] == 'w')):
    print(" Your next move is dd dd rr rr\n")
    n = 4
    return(n)
        
if((front[2] == 'w') & (left[3] == 'b') & (lower[0] == 'o')):
    print(" Your next move is dd rp dp rr\n")
    n = 4
    return(n)
        
if((right[3] == 'b') & (lower[3] == 'o') & (back[2] == 'w')):
    print(" Your next move is rr dd rr rr\n")
    n = 4
    return(n)

if((upper[0] == 'b') & (left[0] == 'w') & (back[1] == 'o')):
    print(" Your next move is uu rr up rr rr\n")
    n = 5
    return(n)

if((back[3] == 'b') & (lower[2] == 'o') & (left[2] == 'w')):
    print(" Your next move is dd fp rp ff rr rr\n")
    n = 6
    return(n)
        
