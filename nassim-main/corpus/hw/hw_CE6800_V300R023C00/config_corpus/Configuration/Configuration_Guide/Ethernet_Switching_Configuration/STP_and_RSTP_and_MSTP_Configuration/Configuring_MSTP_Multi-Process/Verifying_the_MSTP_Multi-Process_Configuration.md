Verifying the MSTP Multi-Process Configuration
==============================================

Verifying the MSTP Multi-Process Configuration

#### Procedure

* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] [ **interface** *interface-type* *interface-number* | **slot** *slot-id* ] [ **brief** ] command to check the spanning tree status and statistics.
* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] **abnormal-interface** command to check information about abnormal interfaces that run MSTP.
* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] **active** command to check the status of and statistics on spanning trees of all up interfaces.
* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] **bridge** { **local** | **root** } command to check details about the spanning tree of the local or root bridge.
* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] **global** command to check the global MSTP information.
* Run the [**display stp vlan**](cmdqueryname=display+stp+vlan) *vlan-id* [ **blocked-interface** ] command to check the spanning tree status of interfaces in the specified VLAN.