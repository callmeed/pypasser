import sys

if len(sys.argv) < 6:
  print "One or more arguments missing"
  sys.exit("Required arguments: attempts completions yards tds interceptions")

def rating(attempts = 0, completions = 0, yards = 0, tds = 0, interceptions = 0): 
  if attempts == 0: return 0.00
  a = (completions / attempts - 0.3) * 5
  b = (yards / attempts - 3) * .25
  c = (tds / attempts) * 20
  d = 2.375 - (interceptions / attempts * 25)
  return ((mm(a) + mm(b) + mm(c) + mm(d)) / 6) * 100

def mm(x):
  return max(0,min(x,2.375))


stats = {
  "attempts"      : float(sys.argv[1]),
  "completions"   : float(sys.argv[2]),
  "yards"         : float(sys.argv[3]),
  "tds"           : float(sys.argv[4]),
  "interceptions" : float(sys.argv[5])
}

print "Passer rating: "
print rating(**stats)