Configuring EVPN VPWS in CCC Mode
=================================

CCC requires manual configuration by network administrators and is best suited for small networks with simple topologies. Because CCC does not require signaling negotiation or control packet exchange, it consumes relatively few resources. However, CCC has poor scalability and is difficult to maintain.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001399437280__fig35341857155312), two CEs connect to the same PE. A local CCC EVPN VPWS connection needs to be deployed between CE1 and CE2 for them to communicate.

**Figure 1** Configuring a local CCC EVPN VPWS connection  
![](figure/en-us_image_0000001399758420.png)

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Configure an EVPL instance and create a local CCC EVPN VPWS connection.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id* command to create an EVPL instance and enter its view.
   3. Run the [**ccc**](cmdqueryname=ccc) **interface** { *interface-name* | *acIfType* *acIfNum* } **out-interface** { *out-interface-name* | *outAcIfType* *outAcIfNum* } command to create a local CCC EVPN VPWS connection.
      
      
      
      Here, you only need to configure the inbound and outbound interfaces of the local CCC connection on the PE. Because a local CCC connection is bidirectional, only one connection is required.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

A local CCC EVPN VPWS connection has been configured.

* Run the [**display bgp evpn evpl**](cmdqueryname=display+bgp+evpn+evpl) command to check all EVPL instance information.