from level1 import level1
from level2 import level2
from level3 import level3

# Initializing the score variable to 0
score = 0

# Executing each level function sequentially and updating the score
score = level1(score)  # Execute level 1 and update the score
score = level2(score)  # Execute level 2 and update the score
score = level3(score)  # Execute level 3 and update the score