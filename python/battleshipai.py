
    for move in validmoves:
        # print(move)
        aiboard = board.copy()
        aipiece = aiboard[move[0:2]]
        aiboard[move[0:2]] = '  '
        aiboard[move[3:5]] = aipiece
        ## print(aiboard)
        #movescoredict.update
        movescoredict.update(evaluate(move, color, aiboard, storeboard, color.upper(), pre_enemyscore, turnnum))

    #    movescoredict.update({move: random.randrange(0,1000)})

    difficulty = 4
    bestmoves = [["", -9999]]
    for move, score in movescoredict.items():
        for i in range(difficulty):
            try:
                if score > bestmoves[i][1]:
                    bestmoves.insert(i, [move, score])
                    break
                elif score == bestmoves[i][1]:
                    randomnumber = i + random.randrange(0,2)
                    if randomnumber >= 0:
                        bestmoves.insert(randomnumber, [move, score])
                    else:
                        bestmoves.insert(0, [move, score])
                    break
            except KeyError:
                bestmoves.append([move, score])
                break
    # print(bestmoves)
    bestmoves = bestmoves[0:difficulty]
