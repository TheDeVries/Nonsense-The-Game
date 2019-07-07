# Nonsense: The Game
## CS 110 Final Project
### Fall 2018

[https://github.com/binghamtonuniversity-cs110/final-project-fall18-the](#)

[link to demo presentation slides](#)

### Team: __THE__
* Michael Spano
* Kevin Apyapong
* Brian DeVries

***

## Project Description
 __Nonsense: The Game__ is a 5-minigame survival gauntlet that gets progressively more demented as it continues. Gameplay is as follows: The player is led through an assortment of games and scenarios that are rotated according to a randomized timer. Success in each scene will raise the player’s score. Failure will increase the insanity meter, resulting in a series of undesirable graphical, audio, and logical distortions. It’s game over once the insanity meter reaches 6.
 
***

 This was the final project for my first CS class and my team and I worked on it over October-December 2018. The process of turning it in involved a presentation before the professor and TAs that determined what the top three projects of the class were. Ours, even in all its buginess, earned us second place out of roughly 30-40 teams. There were a couple of planned updates that were never included in the submitted version, but have been made since then. One of these is the inclusion of a set of insanity-based transition screens, available in this version.

***

## How to Play
 Download the most recent versions of python and pygame, then run main.py.

***

## Known Bugs

* General Problems
    * Insanity transitions include an invisible frame, causing an unwanted black screen to quickly flash
    * Game design typically makes it impossible to pass 9 levels

* Club Level
    * Arrow Spawn Lag
    * Failure upon arrow press despite it overlapping the landing pads
    * Dialogue from previous instance is still used
    * Dialogue file options are not reset ??

* Platform Level
    * Once beaten, level is always reloaded and enemies do not respawn.
    * Needs more graphical and sound improvements

* Spaceshooter Level
   * Flashing graphics
   * Ineffective game design, but works otherwise

* Maze Level
   * Using debug mode to pass level still causes insanity to increase

* Typing Level
    * Boring
       
***

## Program Design
* Additional Libraries:
    * None
* Class Interface:
    * A simple drawing that shows the class relationships in your code (see the sample Proposal document for an example).
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* List of Classes:
    * Controller Class: Randomly chooses a new scene based off of the levels that have already been completed. Used to display insanity, score, clock, and handle related effects.
    * Club Class: Contains the game loop for club level
      * Model Classes include Character, Arrows, and Dialogue
    * Typing Class: Contains the game loop for typing level
      * No Model Classes
    * Platformer Class: Contains the game loop for platformer level
      * Model Classes include: Player_Platform, Enemy, Player_Death, Dragon, Explosion, Fireball, and Platforms_Map
    * Maze Class: Contains the game loop for maze level
      * Model Classes include: Player, insanity5face
    * Space Class: Contains the game loop for space shooter level
      * Model Classes include: Hero, Enemy, HeroBlast, and Explosion
***

## Tasks and Responsibilities
### Software Lead - Brian DeVries
* Create Club and Typing Levels
* Verify Overall Project and Teamwork Quality

### Front End Specialist - Kevin Apyapong
* Create Spaceshooter Level
* Verify Front-End Quality

### Back End Specialist - Michael Spano
* Create Maze and Platform Levels
* Verify Back-End Quality

## Testing
   * We ran our code after every update and verified that it worked by using the print function or observing visual feedback. By doing this after each update, we would know which code wasn't working as soon as it was added.
