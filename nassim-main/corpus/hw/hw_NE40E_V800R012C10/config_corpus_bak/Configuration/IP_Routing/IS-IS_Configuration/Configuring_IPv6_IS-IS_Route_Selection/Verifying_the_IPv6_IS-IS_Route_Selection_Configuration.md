Verifying the IPv6 IS-IS Route Selection Configuration
======================================================

After configuring IPv6 IS-IS route selection, check the configurations.

#### Procedure

* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv6** ] [ **topology** *topology-name* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* [ | **count** ] command to check IS-IS routing information.
* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ { **level-1** | **level-2** } | **verbose** | { **local** | *lsp-id* | **is-name** *symbolic-name* } ] \* [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check information about the IS-IS LSDB.