Understanding the BGP Confederation
===================================

In addition to RRs, BGP confederations can help reduce the number of IBGP connections to be established in an AS. A BGP confederation divides an AS into several sub-ASs. Fully meshed IBGP connections are established in each sub-AS and fully meshed EBGP connections between sub-ASs. [Figure 1](#EN-US_CONCEPT_0000001176663657__fig_dc_vrp_bgp_feature_001001) shows the network diagram of a BGP confederation.

**Figure 1** Network diagram of a BGP confederation  
![](figure/en-us_image_0000001176663727.png)

For a BGP speaker (for example, a BGP device in AS 100) that does not belong to a confederation, multiple sub-ASs (AS 65001, AS 65002, and AS 65003) in the same confederation are considered as a whole. External devices do not need to know the status of internal sub-ASs, the confederation ID that identifies the confederation is set to the AS number. As shown in [Figure 1](#EN-US_CONCEPT_0000001176663657__fig_dc_vrp_bgp_feature_001001), AS 200 is used as a confederation ID.

In [Figure 1](#EN-US_CONCEPT_0000001176663657__fig_dc_vrp_bgp_feature_001001), multiple BGP devices reside in AS 200. To reduce the number of IBGP connections to be established, three sub-ASs: AS 65001, AS 65002, and AS 65003 are deployed. Full-mesh IBGP connections are established between the three devices in AS 65001.

#### Applications and Limitations

The confederation needs to be configured on each device, and the device that joins the confederation must support the confederation function.

BGP speakers need to be reconfigured when a network working in non-confederation mode is switched to confederation mode. As a result, the logical topology changes accordingly.

On large-scale BGP networks, both the RR and confederation solutions can be used.