#BJSIM
Simulates BJs
#TODO

* scripts
    * script that to screen and ssh into all the ecf machines
        * specify the trial file
        * runs a run python program
            * opens ~5 threads and execute the specified trial file
    * script to push sim files to ecf(pull from git?)

* fatal error
    * what will happen if the deck runs out of cards?
        * maybe requiresShuffle should go true if we are at deckpen + max number of cards that could be dealt(from remaining cards)

* fatal error
    * the count is only updated at the end each turn NOT as the cards are dealt
    * update the count for each player after every card is dealt

* ability to specify full set of tables for each player
    * counting values
    * betting spreads/ramps

* true count for players
    * need to be able to specify how well the player can estimate the deck
        * e.g. nearest deck, nearest half deck, exact # cards

* ability to specify game rules
    * insurace
    * surrender
    * double down
    * split

* R(setup scripts for peeps to use)
    * plotting
    * distribution identification
    * do our dist tests to compare schemes/do 1 sided tests to say if they are better than breaking even


