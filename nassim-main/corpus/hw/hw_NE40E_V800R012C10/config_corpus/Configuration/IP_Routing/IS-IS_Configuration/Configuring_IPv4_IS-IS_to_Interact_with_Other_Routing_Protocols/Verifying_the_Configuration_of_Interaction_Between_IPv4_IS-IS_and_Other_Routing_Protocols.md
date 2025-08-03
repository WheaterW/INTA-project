Verifying the Configuration of Interaction Between IPv4 IS-IS and Other Routing Protocols
=========================================================================================

After configuring IS-IS to import routes from other protocols, check the configurations.

#### Procedure

* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ { **level-1** | **level-2** } | **verbose** | { **local** | *lsp-id* | **is-name** *symbolic-name* } ] \* [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.
* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] \* command to check IS-IS routing information.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **ip-prefix** *ip-prefix-name* [ **verbose** ] command to check the IP routing table.