Configuring the Router ID
=========================

The router ID uniquely identifies a device in an AS.

#### Usage Scenario

A router ID is a 32-bit IP address that uniquely identifies a router in an Autonomous System (AS). A router ID can be generated as follows:

* Manually configured
* Configured by the protocol
* Automatically selected

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the IP address of a physical interface is configured as the router ID and then the IP address changes, route flapping may occur. Therefore, configuring the IP address of a loopback interface as the router ID is recommended.



#### Pre-configuration Tasks

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**router id**](cmdqueryname=router+id) *router-id*
   
   
   
   The Router ID is specified.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After configuring a router ID, check it.

* Run the [**display router id**](cmdqueryname=display+router+id) command to check the router ID.