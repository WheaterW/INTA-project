Verifying the Configuration
===========================

After configuring carrier's carrier, you can check information about public network routes on PEs and CEs of Level 1 and Level 2 carriers, VPN routes on the PEs, and LDP LSPs.

#### Prerequisites

Carrier's carrier (solution 2) has been configured.


#### Procedure

* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check the VPN routing tables on the PEs of the Level 1 and Level 2 carrier networks.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check the public network routing tables on the PEs and CEs of the Level 1 and Level 2 carrier networks.
* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command to check LDP LSP establishment status on the CEs of the Level 1 carrier network.