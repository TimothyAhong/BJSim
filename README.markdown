#BJSIM
Python program used to simulate blackjack games. It is an extension of this guy's simulator ...


#WRITING NEW TESTS


#DATA EXPORT
The simulator has the capability to log the information below. Each item (hands, shoes, player_trials and trials) is stored in a seperate csv file. The file format is $name_$hour__$month_$day_$year($computer_name)($thread_number).csv. Enabling and disabling each of the following logs is done by setting the trial.enable_hand_log, trial.enable_shoe_log and trial.enable_trial_log.

* hands(per player) (files per computer per date)
    * trial id
    * player id
    * game id
    * wager
    * bankroll
    * count
    * outcome
    * final player card value

* shoes(per player) (files per computer per date)
    * trial id
    * player id
    * game id
    * hands played
    * hands won
    * shoe number (in current trial)
    * total wagered
    * bankroll at start of shoe
    * net gain/loss
    * percent change

* player_trials(per player) (files per computer per date)
    * trial id
    * player id
    * game id
    * bankroll
    * starting bankroll
    * hands won
    * hands lost
    * hands pushed
    * hands until double
    * hands until ruin

* trials (single file)
    * trial id
    * start time
    * duration(s)
    * decks played

#DISTRIBUTED COMPUTATION
The computation of simulations is highly parallelizable. Currently computation is distributed to the University of Toronto's Engineering Computation Facility or ECF. At the moment it is only distributed to the linux labs which comprise of ~150 machines. The windows labs have roughly the same number of machines however they are i7 3.4GHz with 4GB DDR3, it would be wise to utilize these computers. The filesystem between all the ECF machines is shared as long as you login as the same user. This further simplifies the distribution.

The relavent scripts are under the bash folder. There are script for pushing your local version of bjsimpy to ecf, pull data from ecf and commissioning all the ecf computers to run the simulation.

#STATISTICS IN R
...

#TODO
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


