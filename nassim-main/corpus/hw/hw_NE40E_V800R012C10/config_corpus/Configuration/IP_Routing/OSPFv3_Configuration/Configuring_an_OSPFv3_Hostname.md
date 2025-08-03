Configuring an OSPFv3 Hostname
==============================

Compared with router IDs, OSPFv3 hostnames are easier to memorize. Therefore, using hostnames to identify Routers can facilitate network management.

#### Usage Scenario

To facilitate network management, configure dynamic OSPFv3 hostnames to identify Routers.

Either dynamic or static OSPFv3 hostnames can be configured. In dynamic mode, a hostname can be configured on and advertised by the local device. The mapping between the local device's router ID and hostname can then be queried on a remote Router that successfully learns this dynamic hostname.


#### Pre-configuration Tasks

Before configuring a hostname, complete the following tasks:

* Configure an IP address for each interface to ensure that neighboring routers can use the IP addresses to communicate with each other.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**hostname**](cmdqueryname=hostname) *host-name*
   
   
   
   A dynamic OSPFv3 hostname is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the *host-name* parameter is specified, the value of *host-name* is advertised as the dynamic hostname. If only the [**hostname**](cmdqueryname=hostname) command is run and *host-name* is not specified, the device name specified in the [**sysname**](cmdqueryname=sysname) command is advertised as the dynamic hostname.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the following command to check dynamic OSPFv3 hostnames:

* [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **hostname-table**