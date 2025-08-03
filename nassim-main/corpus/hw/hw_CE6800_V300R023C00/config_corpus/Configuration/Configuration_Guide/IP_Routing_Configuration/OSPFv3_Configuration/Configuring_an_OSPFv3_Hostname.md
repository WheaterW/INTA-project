Configuring an OSPFv3 Hostname
==============================

Configuring an OSPFv3 Hostname

#### Prerequisites

Before configuring an OSPFv3 hostname, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

To facilitate network planning, configure hostnames to identify devices.

Either dynamic or static OSPFv3 hostnames can be configured. In dynamic mode, a hostname is configured on and advertised by the local device. The mapping between the local device's router ID and hostname can be queried on the remote device that has successfully learned this dynamic hostname. Conversely, in static mode, a hostname is configured on the local device for the neighbor with a specified router ID (in the IP address format), which is then mapped with the router ID of the neighbor. The mapping can then be queried on the local device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Configure a dynamic OSPFv3 hostname.
   
   
   ```
   [hostname](cmdqueryname=hostname) host-name
   ```
   
   If the *host-name* parameter is specified, the value of *host-name* is advertised as the dynamic hostname. If only the [**hostname**](cmdqueryname=hostname) command is run and *host-name* is not specified, the device name specified in the [**sysname**](cmdqueryname=sysname) command is advertised as the dynamic hostname.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run any of the following commands to check dynamic OSPFv3 hostnames:

* [**display ospfv3 hostname-table**](cmdqueryname=display+ospfv3+hostname-table)
* [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **lsdb** [**area** *area-id* ] [ **originate-router** *advertising-router-id* | **hostname** *hostname* | **self-originate** ] [ { **grace** | **inter-prefix** | **inter-router** | **intra-prefix** | **link** | **network** | **router** | **router-information** } [*link-state-id* ] ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]
* [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **lsdb** [ **originate-router** *advertising-router-id* | **self-originate** ] { **external** | **router-information** } [ *link-state-id* ] [ **resolve-hostname** ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]
* [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **lsdb** [**area** *area-id* ] [ **originate-router** { *advertising-router-id* } | **self-originate** ] [ { **grace** | **inter-prefix** | **inter-router** | **intra-prefix** | **link** | **network** | **router** | **router-information** } [*link-state-id* ] ] [ **resolve-hostname** ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]