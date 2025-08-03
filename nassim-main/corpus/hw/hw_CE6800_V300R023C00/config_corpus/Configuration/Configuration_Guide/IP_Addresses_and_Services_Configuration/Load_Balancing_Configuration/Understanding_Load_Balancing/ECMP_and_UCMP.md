ECMP and UCMP
=============

Route load balancing can be further classified as equal-cost multi-path (ECMP) or unequal cost multipath (UCMP).

#### ECMP

ECMP evenly balances traffic among multiple equal-cost paths to the same destination, irrespective of bandwidth. Equal-cost paths have the same cost to the destination.

When these paths have very different bandwidths, the bandwidth utilization is low. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001564121201__fig_load-balance_feature_00601), traffic is balanced among three paths, with the bandwidth of 10 Mbit/s, 20 Mbit/s, and 30 Mbit/s, respectively. If ECMP is used, the total bandwidth can reach 30 Mbit/s, but the highest bandwidth utilization can only reach 50%.

**Figure 1** ECMP networking  
![](figure/en-us_image_0000001564121249.png)

#### UCMP

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001564121201__fig_load-balance_feature_00602), UCMP proportionally balances traffic among multiple equal-cost paths to the same destination based on different bandwidths, improving bandwidth utilization.

**Figure 2** UCMP networking  
![](figure/en-us_image_0000001512682002.png)