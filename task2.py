def odometer(oksana):
  arr = oksana

  if ( len(arr) >= 2 ):
    v = 0
    t = 0
    prevT = 0
    s = 0

    for i in range( len(arr) ):
      if (i % 2 == 0):
        v = arr[i]
      elif (i % 2 == 1):
        t = abs(arr[i] - prevT)
        prevT = arr[i]
        s += v * t
        

    return s
