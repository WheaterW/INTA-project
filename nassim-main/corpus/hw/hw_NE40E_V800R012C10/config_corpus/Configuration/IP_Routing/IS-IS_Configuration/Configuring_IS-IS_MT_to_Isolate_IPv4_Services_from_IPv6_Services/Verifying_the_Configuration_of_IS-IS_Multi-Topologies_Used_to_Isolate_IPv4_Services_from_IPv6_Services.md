Verifying the Configuration of IS-IS Multi-Topologies Used to Isolate IPv4 Services from IPv6 Services
======================================================================================================

After configuring IPv4 IS-IS MT to isolate IPv4 services from IPv6 services, check the configuration about IS-IS multi-topologies.

#### Prerequisites

IPv4 IS-IS MT has been configured to isolate IPv4 services from IPv6 services.


#### Procedure

* Run the [**display isis peer**](cmdqueryname=display+isis+peer) [ **verbose** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check information about IS-IS neighbors.
* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** | **ipv6**] [ **topology** *topology-name* ] [ **verbose** | [ **level-1** | **level-2** ] ] command to check IS-IS routing information.
* Run the [**display isis spf-tree**](cmdqueryname=display+isis+spf-tree) [ **systemid** *systemid* ] [ [ **level-1** | **level-2** ] | **ipv6** | **topology** *topology-name* ] \* **verbose** [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS SPT information.