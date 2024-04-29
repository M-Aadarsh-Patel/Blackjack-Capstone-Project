import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(cards_to_be_dealt_to, K):
    for i in range(K):
        cards_to_be_dealt_to.append(random.choice(cards))

def caluculate_score(hand):
    score = sum(hand)
    if score == 21:
        return 0
    else:
       return score

def result_declaration(computer_final, player_final):
    if player_final < computer_final < 21:
        print(f"The computer had a score of {computer_final}, Your score is {player_final}, the computer won!, You lost")

    elif computer_final and player_final == 0:
        print("You both had a Blackjack, its a draw!!")

    elif computer_final == 0:
        print("The computer had a Blackjack. You lost!!")

    elif player_final == 0:
        print("You had a Blackjack. You Win!!")

    elif computer_final >= 21 and player_final < 21:
        print(f"The computer had a score {computer_final}, You win!!")

    elif player_final >= 21 and computer_final < 21:
        print(f"You had a score of {player_final}, You lose!")

    elif computer_final < player_final < 21:
        print(f"you had a score of {player_final} which is greater than the computer's score of {computer_final}, You win!!")

    elif computer_final and player_final >= 21:
        print(f"It's a draw!! (computer's score: {computer_final}, Your score {player_final})")


while True:

    player_cards = []
    computer_cards = []

    playing = input("Do you want to play a game of Blackjack? (Type 'y' or 'n') ")

    if playing.lower() == 'y':
        deal_card(cards_to_be_dealt_to=player_cards, K=2)
        current_player_score = caluculate_score(hand=player_cards)

        deal_card(cards_to_be_dealt_to=computer_cards, K=2)
        computer_score = caluculate_score(hand=computer_cards)

        print(f"Your cards: {player_cards}, Current Score:{current_player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_cards == [10, 11] or player_cards == [11, 10]:
            print("You've got a Blackjack you win")

        elif computer_cards == [10, 11] or computer_cards == [11, 10]:
            print("Computer has gotten a BlackJack, you lose!")

        elif player_cards != [10, 11] and player_cards != [11, 10]:
            if computer_cards != [10, 11] and player_cards != [11, 10]:
                card_choice = input("Type 'y' to get another card, type 'n' to pass: ")

                if card_choice.lower() == 'y':

                    #creating a new variable final_player_cards and assiging it to the modified player_cards after appending.
                    deal_card(cards_to_be_dealt_to=player_cards, K=1)
                    final_player_cards = player_cards

                    final_player_score = caluculate_score(final_player_cards)


                    print(f"Your cards: {final_player_cards}, Final Score: {final_player_score}")
                    print(f"Computer's first card: {computer_cards[0]}")

                    print(f"Your final hand: {player_cards}, Final Score: {final_player_score}")
                        
                    print(f"Computer's hand: {computer_cards}, Computer Score: {computer_score}")
                        
                    while computer_score < 17:

                        print("The computer had a score less than 17, computer drew a card")

                        deal_card(cards_to_be_dealt_to=computer_cards, K=1)
                        final_computer_cards = computer_cards

                        final_computer_score = caluculate_score(final_computer_cards)
                        computer_score = final_computer_score

                        print(f"Computer's final hand: {final_computer_cards}")
                            
                    else:
                        final_computer_score = computer_score

                    result_declaration(computer_final=final_computer_score, player_final=final_player_score)

                            
                elif card_choice.lower() == 'n':

                    final_player_score = current_player_score
                    final_computer_score = computer_score

                    result_declaration(computer_final=final_computer_score, player_final=final_player_score)


                elif playing.lower() == 'n':
                    break

else:
    quit()
