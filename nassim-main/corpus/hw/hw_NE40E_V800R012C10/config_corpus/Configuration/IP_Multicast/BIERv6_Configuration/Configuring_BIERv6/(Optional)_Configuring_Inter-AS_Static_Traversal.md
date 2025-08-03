(Optional) Configuring Inter-AS Static Traversal
================================================

When a BIERv6 network is deployed across ASs, static BFR-neighbors need to be configured so that static BIERv6 BIFT entries are generated. These entries enable traversal to be implemented if BIERv6-incapable nodes exist on an inter-AS path, as long as these nodes support IPv6 unicast forwarding.

#### Context

[Figure 1](#EN-US_TASK_0271431862__fig18735195812346) shows the networking of inter-AS static traversal. In the networking, a BIERv6 next-hop neighbor needs to be manually set for the upstream node of each BIERv6-incapable node. This allows this upstream node to generate a BIERv6 BIFT entry. Currently, the End.BIER SID of a BIERv6-capable next hop can be set based on a specific range of BFR-IDs corresponding to the destination nodes of multicast packets. For example, on PE1, ASBR2's End.BIER SID is manually set as the next hop for the multicast packets destined for PE2 (with BFR-ID 2) and PE3 (with BFR-ID 3).

**Figure 1** Networking of inter-AS static traversal  
![](figure/en-us_image_0282017697.png "Click to enlarge")
#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bier**](cmdqueryname=bier)
   
   
   
   BIER is enabled, and the BIER view is displayed.
3. Run [**sub-domain**](cmdqueryname=sub-domain) *sub-domain-val* **ipv6**
   
   
   
   The sub-domain view is displayed.
4. Run [**protocol**](cmdqueryname=protocol) *static-bift*
   
   
   
   Static BIFT-based forwarding is enabled.
5. Run [**bfr-neighbor**](cmdqueryname=bfr-neighbor) **end-bier** *ipv6-address* **bfr-id** *bfrid-start* [ **to** *bfrid-end* ]
   
   
   
   The End.BIER SID of a BIERv6-capable next hop is set based on a specific range of BFR-IDs corresponding to the destination nodes of multicast packets.
   
   
   
   If the BFR-IDs of the destination nodes are in multiple ranges, repeat this command until all the BFR-IDs are specified.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the sub-domain view.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the BIER view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. (Optional) Repeat [1](#EN-US_TASK_0271431862__step127334244280) to [8](#EN-US_TASK_0271431862__step56492106710) if a BIERv6-incapable node to be traversed has multiple nodes upstream.