Verifying the Configuration
===========================

After carrier's carrier is configured, you can view public network routes on the PEs and CEs of Level 1 and Level 2 carriers, VPN routes on the PEs of these carriers, and LDP LSP establishment status.

#### Prerequisites

Carrier's carrier (solution 2) has been configured.


#### Procedure

* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check the VPN routing tables on the PEs of both Level 1 and Level 2 carriers.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check the public network routing tables on the PEs and CEs of both Level 1 and Level 2 carriers.
* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) **vpn-instance** *vpn-instance-name* **protocol** **ldp** [ **include** *ip-address* *mask-length* ] [ **outgoing-interface** { *interface-name* | *interface-type* *interface-number* } ] [ **in-label** *in-label-value* ] [ **nexthop** *nexthop-value* ] [ **lsr-role** { **ingress** | **transit** | **egress** } ] [ **in-label** *in-label-value* ] [ **verbose** ] command to check whether LDP LSPs are established on the Level 1 carrier CE.