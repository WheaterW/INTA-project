Configuring Route Summarization
===============================

When a large-scale OSPF network is deployed, you can configure route summarization to reduce routing entries.

#### Context

Route summarization on a large-scale OSPF network reduces routing entries, minimizes system resource consumption, and maintains system performance. In addition, if a specific link frequently alternates between Up and Down, the links not involved in the route summarization will not be affected, which prevents route flapping and improves network stability.


#### Procedure

* Configure ABR route summarization.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     The OSPF view is displayed.
  3. Run [**area**](cmdqueryname=area) *area-id*
     
     
     
     The OSPF area view is displayed.
  4. Run [**abr-summary**](cmdqueryname=abr-summary) *ip-address* *mask* [ [ **advertise** | [ **cost** { *cost-value* | **inherit-minimum** } ] | [ ****hold-max-cost******interval** ] | [ **generate-null0-route** ] ] \* | [ **not-advertise** | [ **cost** { *cost-value* | **inherit-minimum** } ] | [ ****hold-max-cost******interval** ] ] \* | [ **generate-null0-route** | [ **advertise** ] | [ **cost** { *cost-value* | **inherit-minimum** } ] | [ ****hold-max-cost******interval** ] ] \* ]
     
     
     
     OSPF ABR route summarization is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure ASBR route summarization.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     The OSPF view is displayed.
  3. Run [**asbr-summary**](cmdqueryname=asbr-summary) *ip-address* *mask* [ [ **not-advertise** | **generate-null0-route** ] | **tag** *tag-value* | **cost** *cost-value* | **distribute-delay** *interval* ] \*
     
     
     
     OSPF route summarization is configured on the ASBR.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After route summarization is configured, the routing table of the local OSPF device remains unchanged. The routing table on an OSPF neighbor, however, contains only one summary route and no specific routes. This summary route stays in the routing table until all the summarized specific routes on the network are withdrawn.