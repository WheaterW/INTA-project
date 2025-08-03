Configuring RIP-2 Route Summarization
=====================================

Configuring RIP-2 route summarization reduces the routing table size, which improves system performance and network security.

#### Context

On a medium-or large-sized network, the routing table contains a large number of routes. Storing and managing the routes consume a large number of memory resources. To resolve this problem, RIP-2 provides the route summarization function. Route summarization allows multiple routes with the same IP prefix and destination IP address to be summarized into one, which reduces the number of routes in the routing table and minimizes system resource consumption. In addition, if a specific link frequently alternates between Up and Down, the links not involved in the route summarization will not be affected, which prevents route flapping and improves network stability.![](../../../../public_sys-resources/note_3.0-en-us.png) 

RIP-1 does not support route summarization.




#### Procedure

* Enable RIP-2 automatic route summarization.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
     
     
     
     A RIP process is created, and the RIP view is displayed.
  3. Run [**summary**](cmdqueryname=summary) [ **always** ]
     
     
     
     RIP-2 automatic route summarization is enabled.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If you specify **always**, RIP-2 automatic route summarization takes effect, regardless of whether split horizon and poison reverse has been configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure RIP-2 to advertise the summarized route.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**rip summary-address**](cmdqueryname=rip+summary-address) *ip-address* *mask* [ **avoid-feedback** ]
     
     
     
     RIP-2 is configured to advertise the summarized route to the specified IP address.
     
     If you specify **avoid-feedback**, the local interface does not learn the summarized route whose destination address is the same as that the advertised summarized route, which prevents routing loops.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.