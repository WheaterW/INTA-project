Configuring RIP Network Management
==================================

By binding RIP and MIBs, you can view and configure RIP
through the NMS.

#### Usage Scenario

Through Simple Network Management
Protocol (SNMP), the RIP Management Information Base (MIB) manages
multicast information exchanged between the NMS and agents.


#### Pre-configuration Tasks

Before controlling
RIP configuration through an SNMP agent, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring
  nodes are reachable at the network layer.
* [Configuring Basic RIP Functions](dc_vrp_rip_cfg_0003.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip mib-binding**](cmdqueryname=rip+mib-binding) *process-id*
   
   
   
   The MIB is bound to the RIP process ID, and the ID of the
   RIP process that accepts SNMP requests is specified.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the following
commands to check the previous configuration.

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the valid parameters on the device.