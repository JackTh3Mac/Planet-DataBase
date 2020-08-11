fimport time
while True: 
  print ("____________________________________________________")
  print ("Name a planet")
  print("Say .help for help")
  planet = input()
  
  # Here are my Planet info variables
    
  JupiterData = ("Jupiter, 0.00006645681348944764 light years away, no lifeforms detected. Notes: Gas Giant, No solid land, Largest planet in the solar system.")
  EarthData = ("Earth, 0 light years away, lifeforms detected. Notes: Has frozen and unfrozen water. Has the only planet that has sent objects to others.")
  VenusData = ("Venus, 0 light years away, no lifeforms detected Notes: Hotest planet in the solar system. Second closest to the sun.")
  NeptuneData = ("Neptune, 0 light years away, no lifeforms detected. Notes: Furthest plantet in the solar system. Very cold.")
  SaturnData = ("Saturn, 0 light years away, no lifeforms detected. Notes: Gas Giant, No solid land. Has Rings")
  MercuryData = ("Mercury, 0 light years away, no lifeforms detected. Notes: Closest to the sun. Very hot.")
  MarsData = ("Mars, 0 light years away, no lifeforms detected. Notes: Has red/orange color. Has ice caps. First planet other than Earth to have a helicopter fly.")
  HelpData = ("Hello! Looks like you need help. Heres a list of things to do. Type in a planet name and find out data. This is a WIP. Commands are... Saturn, Mars, Earth, Venus, Mercury, Neptune, Jupiter, .help.")
  MoonData = ("Error. The Moon is not a planet.")
  PlutoData = ("Error. Pluto is not a planet. It is a dwarf planet.")
  # Just to make it look nicer
    
  print("Loading...")
  time.sleep(1)
  print("Colecting Data...")
  time.sleep(1.)
  print("_____________________________________________________")
    
  # This is to check what planet they are
    
  if planet == 'Mars':
       print(MarsData)
       
  if planet == 'Earth':
       print(EarthData)
          
  if planet == 'Jupiter':
       print(JupiterData)
       
  if planet == 'Saturn':
       print(SaturnData)
       
  if planet == 'Neptune':
       print(NeptuneData)
       
  if planet == 'Venus':
       print(VenusData)
       
  if planet == 'Mercury':
       print(MercuryData)
       
  if planet == '.help':
       print(HelpData)
       
  if planet == 'Moon':
       print(MoonData)     
  
  if planet == 'Pluto':
       print(PlutoData)     




