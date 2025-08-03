Configuring the Network Management Function of OSPF
===================================================

OSPF supports the network management function. You can bind the OSPF MIB to an OSPF process and configure trap and log functions.

#### Usage Scenario

Through the Simple Network Management Protocol (SNMP), the OSPF Management Information Base (MIB) manages information exchanged between the NMS and agents.


#### Pre-configuration Tasks

Before configuring the network management function of OSPF, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf mib-binding**](cmdqueryname=ospf+mib-binding) *process-id*
   
   
   
   The OSPF process is bound to the MIB.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command to check the OSPF MIB binding information.