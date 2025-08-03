Configuring an OSPF Hostname
============================

Compared with router IDs, OSPF hostnames are easier to memorize. Therefore, using hostnames to identify Routers can facilitate network management.

#### Usage Scenario

To facilitate network management, configure hostnames to identify Routers.

Either dynamic or static OSPF hostnames can be configured. In dynamic mode, a hostname can be configured on and advertised by the local device. The mapping between the local device's router ID and hostname can then be queried on a remote Router that successfully learns this dynamic hostname.


#### Pre-configuration Tasks

Before configuring a hostname, complete the following tasks:

* Configure an IP address for each interface to ensure that neighboring routers can use the IP addresses to communicate with each other.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**opaque-capability enable**](cmdqueryname=opaque-capability+enable)
   
   
   
   The Opaque-LSA function is enabled.
4. Run [**hostname**](cmdqueryname=hostname) *host-name*
   
   
   
   A dynamic OSPF hostname is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you specify *hostname* in the [**hostname**](cmdqueryname=hostname) command, the value of *hostname* is advertised as the dynamic hostname. However, if *hostname* is not specified in the command, the hostname specified in the [**sysname**](cmdqueryname=sysname) command is advertised as the dynamic hostname.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run either of the following commands to check dynamic OSPF hostnames:

* [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **hostname-table**
* [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **lsdb** [ **router** | **network** | **summary** | **asbr** | **ase** | **nssa** | **opaque-link** | **opaque-area** ] [ *link-state-id* ] [ **originate-router** [ *advertising-router-id* ] | **self-originate** | **hostname** *hostname* ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]
* [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **lsdb** [ **router** | **network** | **summary** | **asbr** | **ase** | **nssa** | **opaque-link** | **opaque-area** ] [ *link-state-id* ] [ **originate-router** [ *advertising-router-id* ] | **self-originate** ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ] [ **resolve-hostname** ]