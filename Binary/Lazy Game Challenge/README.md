# Lazy Game Challenge - CTF Challenge Writeup

Challenge: Lazy Game Challenge
Points: 30
Category: Binary

## Objective
The objective of the Lazy Game Challenge is to learn about basic math operations in computer programming. Your task is to discover the hidden flag by understanding and manipulating the math operations used in the game.

## Solution
To successfully complete this challenge, follow these steps:

1. **Connect to the provided instance**: Start by connecting to the instance provided by the challenge. This instance is where the game will be played.

2. **Play the game**: Once you're connected to the instance, play the game. Through trial and error, you can learn about the equation used to calculate points in the game.

3. **Understanding the equation**: During your gameplay, you may notice that points are calculated as follows:
   - If you lose, points = 500 - (your bet).
   - If you win, points = 500 + (your bet) * 2.

4. **Reverse the equation**: To reach a threshold amount of points and discover the flag, you need to reverse the equation and strategize your bets.

5. You can do this by placing a negative bet since double negatives become positives, and this will make you lose the game, adding to your points.

    ```
        bet = -1000000
        If you loose, points = 500 - (-1000000)
    ```

8. The flag format is `CTFlearn{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you discover during your gameplay and mathematical manipulation.

## Flag
The flag for this challenge is in the format: `CTFlearn{XXXXXXXXXX}`.

Enjoy your exploration of basic math operations in binary games, and happy hacking!
