Creating a Multicast NAT Instance Group
=======================================

In multicast NAT, input and output multicast streams are associated through a multicast NAT instance. If multiple input multicast streams need to be switched at the same time, create a multicast NAT instance group and add the multicast streams to the multicast NAT instance group.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast-nat instance-group**](cmdqueryname=multicast-nat+instance-group) **id** *instance-group-id* [ **name**  *instance-group-name* ]
   
   
   
   A multicast NAT instance group is created, and the multicast NAT instance group view is displayed.
3. Run [**assign instance**](cmdqueryname=assign+instance) **id** *instance-id* [ **name**  *instance-name* ] **part** *part-id* [ **type** { **video-stream** | **audio-stream** | **ancillary-data** } ]
   
   
   
   A multicast NAT instance is added to the multicast NAT instance group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.