Verifying the Configuration of IS-IS IPv4 Multi-Topologies Used to Isolate Multicast Services from Unicast Services
===================================================================================================================

After configuring IPv4 IS-IS MT to isolate multicast services from unicast services, check the IS-IS MT configurations.

#### Prerequisites

IPv4 IS-IS MT has been configured to isolate multicast services from unicast services.


#### Procedure

* Run the [**display isis peer**](cmdqueryname=display+isis+peer) [ **verbose** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check information about IS-IS neighbors.
* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **topology** *topology-name* ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] \* command to check IS-IS routing information.
* Run the [**display isis spf-tree**](cmdqueryname=display+isis+spf-tree) [ **systemid** *systemid* ] [ [ **level-1** | **level-2** ] | **topology** *topology-name* ] \* **verbose** [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS SPT information.