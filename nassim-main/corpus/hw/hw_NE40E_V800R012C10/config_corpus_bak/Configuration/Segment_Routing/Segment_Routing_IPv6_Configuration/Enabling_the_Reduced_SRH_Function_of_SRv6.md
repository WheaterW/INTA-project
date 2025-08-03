Enabling the Reduced SRH Function of SRv6
=========================================

With the reduced SRH function of SRv6, the first SID in an SRH does not need to be encapsulated, reducing the SRv6 packet size.

#### Usage Scenario

An SRH consumes a large number of bits. During SRH encapsulation, the SRv6 source node encapsulates the first SID to be processed into the destination address (DA) field of the IPv6 header. Therefore, the first SID in the SRH is meaningless for forwarding. To reduce the SRH size, the SRv6 source node can encapsulate a reduced SRH that does not contain the first SID to be processed. If an SRH contains only one SID, the SRH does not need to be encapsulated, as defined by relevant standards.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   SRv6 is enabled, and the SRv6 view is displayed.
3. Run [**reduce-srh enable**](cmdqueryname=reduce-srh+enable)
   
   
   
   The reduced-SRH function is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.