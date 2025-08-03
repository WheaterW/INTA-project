Creating a Multicast NAT Outbound Group
=======================================

In multicast NAT, input and output multicast streams are associated through a multicast NAT instance. If multiple input multicast streams need to be switched at the same time, create a multicast NAT instance group, add the multicast streams to the multicast NAT instance group, create a multicast NAT outbound group, add output multicast streams to the group, and then bind the multicast NAT outbound group to the multicast NAT instance group.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast-nat outbound-group**](cmdqueryname=multicast-nat+outbound-group) **id** *outbound-group-id* [ **name** *outbound-group-name* ]
   
   
   
   A multicast NAT outbound group is created, and its view is displayed.
3. Run [**assign outbound**](cmdqueryname=assign+outbound) **id** *outbound-id* [ **name** *outbound-name* ] **part** *part-id* [ **type** { **video-stream** | **audio-stream** | **ancillary-data** } ]
   
   
   
   An output multicast stream is added to the multicast NAT outbound group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.