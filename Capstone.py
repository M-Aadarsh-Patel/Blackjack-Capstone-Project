import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def result_declaration(computer_final, player_final):
    if player_final < computer_final < 21:
        print(f"The computer had a score of {computer_final}, Your score is {player_final}, the computer won!, You lost")

    elif computer_final >= 21 and player_final < 21:
        print(f"The computer had a score {computer_final}, You win!!")

    elif player_final >= 21 and computer_final < 21:
        print(f"You had a score of {player_final}, You lose!")

    elif computer_final < player_final < 21:
        print(f"you had a score of {player_final} which is greater than the computer's score of {computer_final}, You win!!")

    elif computer_final and player_final >= 21:
        print(f"It's a draw!! (computer's score: {computer_final}, Your score {player_final})")


def caluculate_score(hand):
    score = sum(hand)
    if score == 21:
        return 0
    else:
       return score


while True:

    playing = input("Do you want to play a game of Blackjack? (Type 'y' or 'n') ")

    if playing.lower() == 'y':
        player_cards = random.choices(cards, weights=None, cum_weights=None, k=2)
        current_player_score = caluculate_score(hand=player_cards)

        computer_cards = random.choices(cards, weights=None, cum_weights=None, k=2)
        computer_score = caluculate_score(hand=computer_cards)
        

        print(f"Your cards: {player_cards}, Current Score:{current_player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        card_choice = input("Type 'y' to get another card, type 'n' to pass: ")

        if card_choice.lower() == 'y':
            chosen_card = random.choice(cards)

            #creating a new variable final_player_cards and assiging it to the modified player_cards after appending.
            player_cards.append(chosen_card)
            final_player_cards = player_cards

            final_player_score = caluculate_score(final_player_cards)


            print(f"Your cards: {final_player_cards}, Final Score: {final_player_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            print(f"Your final hand: {player_cards}, Final Score: {final_player_score}")
            
            print(f"Computer's hand: {computer_cards}, Computer Score: {computer_score}")
            
            if computer_score < 17:

                print("The computer had a score less than 17, computer drew a card")

                computer_cards.append(random.choice(cards))
                final_computer_cards = computer_cards

                final_computer_score = caluculate_score(final_computer_cards)

                print(f"Computer's final hand: {final_computer_cards}")

                
                result_declaration(computer_final=final_computer_score, player_final=final_player_score)
                    
            else:
                final_computer_score = computer_score

                result_declaration(computer_final=final_computer_score, player_final=final_player_score)

               
        if card_choice.lower() == 'n':

            final_player_score = current_player_score
            final_computer_score = computer_score

            result_declaration(computer_final=final_computer_score, player_final=final_player_score)


    if playing.lower() == 'n':
        break

else:
    quit()
