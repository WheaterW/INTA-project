Configuring the Network Management Function of OSPFv3
=====================================================

Configuring the Network Management Function of OSPFv3

#### Prerequisites

Before configuring the network management function of OSPFv3, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

OSPFv3 supports the network management function. By using the Simple Network Management Protocol (SNMP), the OSPFv3 management information base (MIB) is associated with an OSPFv3 process to manage multicast information and messages exchanged between the network management station (NMS) and agents (managed devices).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Bind an OSPFv3 process to the OSPFv3 MIB.
   
   
   ```
   [ospfv3 mib-binding](cmdqueryname=ospfv3+mib-binding) process-id
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check whether the OSPFv3 process is bound to the MIB.