def odometer(oksana):
  # S = V * T
  if ( len(oksana) >= 2 ):
    v = 0
    temp = []

    for i in range( len(oksana) ):
      if ( oksana[i] % 2 == 0 ):

        if (i+1 == len(oksana)-1 and oksana[i + 1] % 2 == 0):
          temp.append( oksana[i] )
          break
        elif ( i == len(oksana)-1 ):
          temp.append( oksana[i] )
          break

        v += oksana[i]
      elif ( oksana[i] % 2 == 1 ):
        temp.append( v * oksana[i] )
        v = 0

    s = 0
    for i in range( len(temp) ):
      s += temp[i]

    return s