Verifying the Configuration
===========================

After a GRE tunnel is set up, you can check the running status and routing information of the tunnel interface.

#### Prerequisites

A GRE tunnel has been set up.


#### Procedure

* Run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) [ *interface-number* ] command to check the running status of the tunnel interface.
* Run the [**display tunnel gre**](cmdqueryname=display+tunnel+gre) { **backup** | **reassemble board** } command to check the binding information about the GRE service board/reassembly board.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check the routing table.
* Run the [**ping**](cmdqueryname=ping) **-a** *source-ip-address* *host* command to check whether the two ends of the tunnel can ping each other.