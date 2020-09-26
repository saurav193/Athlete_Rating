# Athlete_Rating

## Abstract details

### Young Investigator Award Competition:

1. The current method of rating snowboarding athletes does not consider the relative importance of competitiveness of different competitions in the same level. This study aims to solve this by considering ranks and scores for all players in all the competitions in each level and develop an adjusted score based on their original score in the competitions. The current method assigns fixed weightage for each level of the competition - World Championships(1000), North American Tournaments(800) and Canadian Tournaments(500). Also there are fixed points associated with each rank in a particular competition. Therefore the problem arises when a player with a low score top rank in a competition and gets the same point as another player with a high score who ranks second, given that competition was much tougher with many good athletes. So we use the Moguls data from 2002 to 2019 for all 3 levels of competitions. Then we take into account all the competitions on each level and make assumed normal distributions of scores for each ranks 1 - 30 for men and 1 - 20 for women. From these distributions, we compute the z-scores corresponding to each original score for each player. Then we adjust the original scores with for each rank, based on these z-scores. This allows us to compare different players having the same rank based on this adjusted scores. Also this allows us to compare the performance of the same player across different competitions irrespective of their ranks. The next part of our study was to enable comparisons across different levels of the competitions. For this, we considered only the players who played on multiple levels in the same season. Modelling their scores with a mixed linear model approach, provided the difference between intercept of the scores of 2 levels. This difference was used to adjust the scores across different levels of competitions. Therefore it is now possible to compare scores for a world championship with a north american cup directly from this adjusted scores rather than the fixed weightage method used earlier. This approach is based completely on the data available and does not assume any fixed weightage. We can use this approach for any other discipline of snowboarding like halfpipe, etc. Once this method is applied it will be possible to directly compare the scores of players across levels and across disciplines of snowboarding.

