import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:

    playing = input("Do you want to play a game of Blackjack? (Type 'y' or 'n') ")

    if playing.lower() == 'y':
        player_cards = random.choices(cards, weights=None, cum_weights=None, k=2)
        current_player_score = player_cards[0] + player_cards[1]

        computer_cards = random.choices(cards, weights=None, cum_weights=None, k=2)
        computer_score = computer_cards[0] + computer_cards[1]
        
        print(f"Your cards: {player_cards}, Current Score:{current_player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        card_choice = input("Type 'y' to get another card, type 'n' to pass: ")

        if card_choice.lower() == 'y':
            chosen_card = random.choice(cards)

            #creating a new variable final_player_cards and assiging it to the modified player_cards after appending.
            player_cards.append(chosen_card)
            final_player_cards = player_cards

            final_player_score = current_player_score + chosen_card


            print(f"Your cards: {final_player_cards}, Final Score: {final_player_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            print(f"Your final hand: {player_cards}, Final Score: {final_player_score}")
            
            print(f"Computer's hand: {computer_cards}, Computer Score: {computer_score}")
            
            if computer_score < 17:

                print("The computer had a score less than 17, computer drew a card")

                computer_cards.append(random.choice(cards))
                final_computer_cards = computer_cards

                final_computer_score = computer_score + computer_cards[2]

                print(f"Computer's final hand: {final_computer_cards}")

                
                if final_player_score < final_computer_score < 21:
                    print(f"The computer had a score of {final_computer_score}, Your score is {final_player_score}, the computer won!, You lost")

                elif final_computer_score >= 21 and final_player_score < 21:
                    print(f"The computer had a score {final_computer_score}, You win!!")

                elif final_player_score >= 21 and final_computer_score < 21:
                    print(f"You had a score of {final_player_score}, You lose!")

                elif final_computer_score < final_player_score < 21:
                    print(f"you had a score of {final_player_score} which is greater than the computer's score of {final_computer_score}, You win!!")

                elif final_computer_score and final_player_score >= 21:
                    print(f"It's a draw!! (computer's score: {final_computer_score}, Your score {final_player_score})")
                    
            else:
                final_computer_score = computer_score

                if final_player_score < final_computer_score < 21:
                    print(f"The computer had a score of {final_computer_score}, Your score is {final_player_score}, the computer won!, You lost")

                elif final_computer_score >= 21 and final_player_score < 21:
                    print(f"The computer had a score {final_computer_score}, You win!!")

                elif final_player_score >= 21 and final_computer_score < 21:
                    print(f"You had a score of {final_player_score}, You lose!")

                elif final_computer_score < final_player_score < 21:
                    print(f"you had a score of {final_player_score} which is greater than the computer's score of {final_computer_score}, You win!!")

                elif final_computer_score and final_player_score >= 21:
                    print(f"It's a draw!! (computer's score: {final_computer_score}, Your score {final_player_score})")

               
        if card_choice.lower() == 'n':

            final_player_score = current_player_score
            final_computer_score = computer_score

            if final_player_score < final_computer_score < 21:
                print(f"The computer had a score of {final_computer_score}, Your score is {final_player_score}, the computer won!, You lost")

            elif final_computer_score >= 21 and final_player_score < 21:
                print(f"The computer had a score {final_computer_score}, You win!!")

            elif final_player_score >= 21 and final_computer_score < 21:
                print(f"You had a score of {final_player_score}, You lose!")

            elif final_computer_score < final_player_score < 21:
                print(f"you had a score of {final_player_score} which is greater than the computer's score of {final_computer_score}, You win!!")

            elif final_computer_score and final_player_score >= 21:
                print(f"It's a draw!! (computer's score: {final_computer_score}, Your score {final_player_score})")


    if playing.lower() == 'n':
        break

else:
    quit()
