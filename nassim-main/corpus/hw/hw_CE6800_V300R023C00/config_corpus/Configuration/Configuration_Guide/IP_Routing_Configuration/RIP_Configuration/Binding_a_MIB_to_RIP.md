Binding a MIB to RIP
====================

Binding a MIB to RIP

#### Context

You can view and configure RIP on the network management system (NMS) after a management information base (MIB) is bound to RIP.

RIP MIB uses SNMP to manage and exchange multicast information between the NMS and managed devices.


#### Prerequisites

Before binding RIP to a MIB, you have completed the following tasks:

* Assign an IP address to each interface to ensure that neighboring nodes are reachable at the network layer.
* [Configuring Basic RIP Functions](vrp_rip_cfg_0008.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Bind MIB to a RIP process used to receive SNMP requests.
   
   
   ```
   [rip mib-binding](cmdqueryname=rip+mib-binding) process-id
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check valid configurations on a RIP routing device.