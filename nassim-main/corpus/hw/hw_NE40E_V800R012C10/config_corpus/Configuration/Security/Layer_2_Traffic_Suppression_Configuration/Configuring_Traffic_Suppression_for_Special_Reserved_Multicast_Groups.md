Configuring Traffic Suppression for Special Reserved Multicast Groups
=====================================================================

This section describes how to configure traffic suppression for special reserved multicast groups in order to reduce the traffic burden on a network.

#### Usage Scenario

A growing number of special reserved multicast group packets in the broadcast domain consume a large amount of network resources, which severely affects service running. To address this issue, you can configure traffic suppression for such packets, thereby reducing the multicast traffic volume to a proper range.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**standard-group mac-address suppression enable**](cmdqueryname=standard-group+mac-address+suppression+enable)
   
   
   
   Traffic suppression is enabled for special reserved multicast groups.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.