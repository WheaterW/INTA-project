Verifying the Configuration
===========================

After enabling IS-IS to import routes from other protocols, check the IS-IS and IP routing tables.

#### Procedure

* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ { **level-1** | **level-2** } | **verbose** | { **local** | *lsp-id* | **is-name** *symbolic-name* } ] \* [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.
* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv6** ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* command to check IS-IS routing information.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **ipv6-prefix** *ipv6-prefix-name* [ **verbose** ] command to check the IP routing table.