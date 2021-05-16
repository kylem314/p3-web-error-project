def Multi(userDatabase):
  indexing = -1
  userfound = False
  user2found = False
  user = input("Who is the first user?\n")
  user2 = input("Who is the second user?\n")
  result = input("Which user won? (1/2)\n")
  if result != "1" and result != "2":
    print("Invalid result!")
    Multi(userDatabase)
  userdata = []
  user2data = []
  usernameLength = len(user)
  username2Length = len(user2)
  for letter in userDatabase:
    indexing += 1
    if letter == "-":
      userCheck = userDatabase[indexing+1:indexing+usernameLength+1]
      if user == userCheck:
        userdata = [user,userDatabase[indexing+usernameLength+1:indexing+usernameLength+5],userDatabase[indexing+usernameLength+5:indexing+usernameLength+9],userDatabase[indexing+usernameLength+9]]
        userfound = True
        break
  indexing = -1
  for letter in userDatabase:
    indexing += 1
    if letter == "-":
      userCheck = userDatabase[indexing+1:indexing+username2Length+1]
      if user2 == userCheck:
        user2data = [user,userDatabase[indexing+username2Length+1:indexing+username2Length+5],userDatabase[indexing+username2Length+5:indexing+username2Length+9],userDatabase[indexing+username2Length+9]]
        user2found = True
        break
#  if userfound == True and user2found == True:
  if userdata[2][0] == 0:
    playerElo = int(userdata[2][1:4])
  elif userdata[2][0] != 0:
    playerElo = int(userdata[2])
  if user2data[2][0] == 0:
    player2Elo = int(user2data[2][1:4])
  elif user2data[2][0] != 0:
    player2Elo = int(user2data[2])

  if result == "1":
    playerDiff = player2Elo - playerElo + 600
    divisor1 = 1 + 10**(playerDiff/1000)
    var1 = 1 / divisor1
    var2 = 1 - var1
    playerElo = playerElo + 50 * var2
    playerElo = int(round(playerElo))
    print(user + " now has an ELO rating of " + str(playerElo))
    if playerElo < 1000:
      playerElo = str("0" + str(playerElo))
    return [userdata[1], userdata[3], playerElo]

  elif result == "2":
    playerDiff = playerElo - player2Elo + 600
    divisor1 = 1 + 10**(playerDiff/1000)
    var1 = 1 / divisor1
    var2 = 1 - var1
    playerElo = playerElo - 50 * var2
    playerElo = int(round(playerElo))
    print(user + " now has an ELO rating of " + str(playerElo))
    if playerElo < 1000:
      playerElo = str("0" + str(playerElo))
    return [userdata[1], userdata[3], playerElo]