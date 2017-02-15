# Foosball Elo Calculator
An Elo calculator using the Bonzini USA ranking system.

The default Elo rating for each player is set at 1000 and the K-factor is set at 50 (the impact of games won and lost.)

# General 

1. Elo for doubles play is calculated by using the average rating for each side.
2. Generally, teams that are expected to win based on higher Elo will earn a lower amount of Elo points for a win and loser more points for a loss.  The reverse works for teams that are underdogs in a match; a win would earn more Elo points for that team.  
3. Players that have less than 10 games played will receive a provisional rating.  The Elo system works best when more games are played, resulting in a more accurate Elo score.
4. You can never lose Elo points for a win and you can never gain Elo points for a loss.

For further documentation on the rating system, please see: www.bonziniusa.com/foosball/tournament/TournamentRankingSystem.html
