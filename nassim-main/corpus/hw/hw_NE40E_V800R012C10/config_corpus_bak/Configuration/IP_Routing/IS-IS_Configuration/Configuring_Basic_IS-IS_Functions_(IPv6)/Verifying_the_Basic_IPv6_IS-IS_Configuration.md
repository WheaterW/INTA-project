Verifying the Basic IPv6 IS-IS Configuration
============================================

After configuring basic IPv6 IS-IS features, check information about IS-IS neighbors, interfaces, and routes.

#### Prerequisites

Basic IPv6 IS-IS functions have been configured.


#### Procedure

1. Run the [**display isis name-table**](cmdqueryname=display+isis+name-table) [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check the mapping between the hostname of the local device and the system ID.
2. Run the [**display isis peer**](cmdqueryname=display+isis+peer) [ **verbose** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check information about IS-IS neighbors.
3. Run the [**display isis interface**](cmdqueryname=display+isis+interface) [ [ **verbose** | **traffic-eng** ] \* | **te-tunnel** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check information about IS-IS interfaces.
4. Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] **ipv6** [ **topology** *topology-name* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* [ | **count** ] command to check information about IS-IS routes.