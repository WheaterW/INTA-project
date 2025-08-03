Configuring the Network Management Function of OSPFv3
=====================================================

OSPFv3 supports the network management function. You can configure the OSPFv3 Management Information Base (MIB) and bind it to an OSPFv3 process through Simple Network Management Protocol (SNMP). In this manner, the OSPFv3 MIB manages multicast information exchanged between the Network Management Station (NMS) and agents.

#### Pre-configuration Tasks

Before configuring the network management function of OSPFv3, complete the following tasks:

* Configure a link layer protocol.
* Configure IPv6 addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3 mib-binding**](cmdqueryname=ospfv3+mib-binding) *process-id*
   
   
   
   The OSPFv3 process is bound to the MIB.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the following command to check the previous configuration:

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check whether an OSPFv3 process has been bound to the OSPFv3 MIB.