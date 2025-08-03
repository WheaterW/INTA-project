Configuring the Function to Suppress the Advertisement of Interface Addresses
=============================================================================

This section describes how to configure the function to suppress the advertisement of interface addresses so that interface addresses can be reused.

#### Procedure

* Configuring the function to suppress the advertisement of all interface addresses in an OSPF process
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     The OSPF view is displayed.
  3. Run [**suppress-reachability**](cmdqueryname=suppress-reachability)
     
     
     
     The device is configured to suppress the advertisement of all interface addresses in an OSPF process.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configuring an OSPF interface to suppress the advertisement of interface addresses
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The OSPF interface view is displayed.
  3. Run [**ospf suppress-reachability**](cmdqueryname=ospf+suppress-reachability)
     
     
     
     An OSPF interface to suppress the advertisement of interface addresses is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.