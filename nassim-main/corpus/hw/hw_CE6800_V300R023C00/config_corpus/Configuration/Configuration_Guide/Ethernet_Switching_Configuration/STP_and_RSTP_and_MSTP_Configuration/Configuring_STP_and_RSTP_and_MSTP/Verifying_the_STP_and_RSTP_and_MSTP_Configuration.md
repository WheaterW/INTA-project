Verifying the STP/RSTP/MSTP Configuration
=========================================

Verifying the STP/RSTP/MSTP Configuration

#### Procedure

* Run the [**display stp**](cmdqueryname=display+stp) [ **instance** *instance-id* ] [ **interface** *interface-type* *interface-number* | **slot** *slot-id* ] [ **brief** ] command to check the spanning tree status and statistics.
* Run the [**display stp**](cmdqueryname=display+stp) [ **instance** *instance-id* ] **abnormal-interface** command to check information about abnormal interfaces that run STP, RSTP, or MSTP.
* Run the [**display stp active**](cmdqueryname=display+stp+active) command to check the status of and statistics on spanning trees of all up interfaces.
* Run the [**display stp bridge**](cmdqueryname=display+stp+bridge) { **local** | **root** } command to check details about the spanning tree of the local or root bridge.
* Run the [**display stp global**](cmdqueryname=display+stp+global) command to check the global STP, RSTP, or MSTP information.
* Run the [**display stp vlan**](cmdqueryname=display+stp+vlan) *vlan-id* [ **blocked-interface** ] command to check the spanning tree status of interfaces in the specified VLAN.