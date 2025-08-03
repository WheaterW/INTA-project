Configuring the Network Management Function of OSPF
===================================================

Configuring the Network Management Function of OSPF

#### Prerequisites

Before configuring the network management function of OSPF, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

By using the Simple Network Management Protocol (SNMP), the OSPF management information base (MIB) manages information about messages exchanged between the network management station (NMS) and agents (managed devices). To implement the network management function of OSPF, bind an OSPF process to the OSPF MIB.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Bind an OSPF process to the OSPF MIB.
   
   
   ```
   [ospf mib-binding](cmdqueryname=ospf+mib-binding) process-id
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check whether the OSPF process is bound to the OSPF MIB.