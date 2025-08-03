Verifying the Configuration
===========================

After configuring basic IPv4 IS-IS functions, check information about IS-IS neighbors, interfaces, and routes.

#### Prerequisites

The configurations of basic IPv4 IS-IS functions are complete.


#### Procedure

1. Run the [**display isis name-table**](cmdqueryname=display+isis+name-table) [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check the mapping between the hostname of the local device and the system ID.
2. Run the [**display isis peer**](cmdqueryname=display+isis+peer) [ **verbose** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check information about IS-IS neighbors.
3. Run the [**display isis interface**](cmdqueryname=display+isis+interface) [ **verbose** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check information about IS-IS interfaces.
4. Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] \* command to check information about IS-IS routes.