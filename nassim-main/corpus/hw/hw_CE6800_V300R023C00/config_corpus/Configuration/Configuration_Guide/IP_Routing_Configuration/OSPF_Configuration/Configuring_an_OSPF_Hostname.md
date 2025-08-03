Configuring an OSPF Hostname
============================

Configuring an OSPF Hostname

#### Prerequisites

Before configuring an OSPF hostname, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

To facilitate network planning, configure hostnames to identify devices. Either dynamic or static OSPF hostnames can be configured. In dynamic mode, a hostname is configured on and advertised by the local device. The mapping between the local device's router ID and hostname can be queried on the remote device that has successfully learned this dynamic hostname.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Enable the opaque LSA capability.
   
   
   ```
   [opaque-capability enable](cmdqueryname=opaque-capability+enable)
   ```
   
   By default, the opaque LSA capability is disabled.
4. Configure a dynamic OSPF hostname.
   
   
   ```
   [hostname](cmdqueryname=hostname) [ host-name ]
   ```
   
   If the *host-name* parameter is specified, the value of *host-name* is advertised as the dynamic hostname. If only the [**hostname**](cmdqueryname=hostname) command is run and *host-name* is not specified, the device name specified in the [**sysname**](cmdqueryname=sysname) command is advertised as the dynamic hostname.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run any of the following commands to check dynamic OSPF hostnames:

* [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **hostname-table**
* [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **lsdb** [ **router** | **network** | **summary** | **asbr** | **ase** | **nssa** | **opaque-link** | **opaque-area** ] [ *link-state-id* ] [ **originate-router** [ *advertising-router-id* ] | **self-originate** | **hostname** *hostname* ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]
* [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **lsdb** [ **router** | **network** | **summary** | **asbr** | **ase** | **nssa** | **opaque-link** | **opaque-area** ] [ *link-state-id* ] [ **originate-router** [ *advertising-router-id* ] | **self-originate** ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ] [ **resolve-hostname** ]