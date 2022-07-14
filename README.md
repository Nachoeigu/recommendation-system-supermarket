# recommendation-system-supermarket
The repository contains a recommendation system, developed with apriori algorithm, for a supermarket in London.


## Some technicals concepts

### Support
Support: Number of transaction of that item / Total transactions. <br>
Support refers to the popularity of an item in the market.
### Confidence
Confidence: Number of transaction of both items / Total transaction of product A. <br>
Confidence is the probability that product B will be purchased if product A is purchased.
### Lift
Lift: Confidence of A -> B   / Support of B <br>
Lift says the likelihood of buying both together is NNNN times more than the likelihood of just buying the the first one (a).  <br>
Lift of greater than 1 means products A and B are more likely to be bought together. <br>
Lift of less than 1 refers to the case where two products are unlikely to be bought together.
### Leverage
Leverage: Computes the difference between the observed frequency of A and B appearing together and the frequency that would be expected if A and B were independent. A leverage value of 0 indicates independence.
### Conviction
Indicates the relationship between the items. If it is = 1, it means they arent associated, but if the higher the value, the strong the relationship.
