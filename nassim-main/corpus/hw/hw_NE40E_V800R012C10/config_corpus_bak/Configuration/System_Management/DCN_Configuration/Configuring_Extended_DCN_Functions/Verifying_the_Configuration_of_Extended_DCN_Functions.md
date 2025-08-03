Verifying the Configuration of Extended DCN Functions
=====================================================

After configuring extended DCN functions, verify the configuration.

#### Prerequisites

Extended DCN functions have been configured on all NEs.


#### Procedure

* Run the [**display dcn brief**](cmdqueryname=display+dcn+brief) command to check configurations of the GNE.
* Run the [**display dcn ne-info**](cmdqueryname=display+dcn+ne-info) command to check information about the DCN core routing table.
* Run the [**display dcn interface**](cmdqueryname=display+dcn+interface) [ *interface-type* *interface-number* ] command to check DCN configurations and traffic statistics of an interface.
* Run the [**display dcn mode vlan interface**](cmdqueryname=display+dcn+mode+vlan+interface) command to view information about sub-interfaces 4094.
* Run the [**display dcn element-info**](cmdqueryname=display+dcn+element-info) command to view details about all NEs that use sub-interfaces 4094 for DCN communication.