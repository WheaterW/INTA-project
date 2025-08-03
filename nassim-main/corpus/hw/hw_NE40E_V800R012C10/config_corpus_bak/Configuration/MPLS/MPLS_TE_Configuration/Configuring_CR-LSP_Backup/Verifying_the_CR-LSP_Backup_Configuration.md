Verifying the CR-LSP Backup Configuration
=========================================

After configuring CR-LSP backup, you can view information about backup CR-LSPs.

#### Prerequisites

CR-LSP backup has been configured.


#### Procedure

* Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command to check information about a tunnel interface on the ingress of a tunnel.
* Run the [**display mpls te hot-standby state**](cmdqueryname=display+mpls+te+hot-standby+state) { **all** [ **verbose** ] | **interface** *tunnel-interface-name* } command to check information about the hot-standby status.