Verifying the IS-IS SR-MPLS BE Tunnel Configuration
===================================================

After configuring an SR-MPLS BE tunnel, verify the configuration of the SR-MPLS BE tunnel.

#### Prerequisites

The SR-MPLS BE functions have been configured.


#### Procedure

After completing the configurations, you can run the following commands to check the configurations.

* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ { **level-1** | **level-2** } | **verbose** | { **local** | *lsp-id* | **is-name** *symbolic-name* } ] \* [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.
* Run the [**display segment-routing prefix mpls forwarding**](cmdqueryname=display+segment-routing+prefix+mpls+forwarding) command to check the label forwarding information base for Segment Routing.