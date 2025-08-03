Checking VBST Statistics
========================

Checking VBST Statistics

#### Context

You can view the VBST running information and statistics on VBST BPDUs. If the number of topology changes increases, network flapping occurs.


#### Procedure

* Run the [**display stp**](cmdqueryname=display+stp) **vlan** [ *vlan-id* ] **information** [ **brief** | **global** ] command to check the status, statistics, and global summary of the spanning tree.
* Run the [**display stp**](cmdqueryname=display+stp) **vlan** [ *vlan-id* ] [**bridge**](cmdqueryname=bridge) { **root** | **local** } command to check the spanning tree status of the local bridge and root bridge.
* Run the [**display stp vlan instance**](cmdqueryname=display+stp+vlan+instance) command to check the mappings between instances and VLANs.
* Run the [**display stp**](cmdqueryname=display+stp) **vlan** [ *vlan-id* ] **bpdu statistics** command to check statistics about sent and received BPDUs.
* Run the [**display stp**](cmdqueryname=display+stp) **vlan** [ *vlan-id* ] **tc-bpdu statistics** command to check statistics about TC/TCN BPDUs sent and received by ports.
* Run the [**display stp**](cmdqueryname=display+stp) **vlan** [ *vlan-id* ] **topology-change** command to check statistics about topology changes.
* Run the [**display vbst local**](cmdqueryname=display+vbst+local) { **instance** [ **vlan** *vlan-id* ] | **port** **port-id** *port-id* | **port-instance** **port-id** *port-id* | **portlist** } command to check information in the VBST internal data area.
* Run the [**display stp**](cmdqueryname=display+stp) **brief** command to check brief information about the spanning tree.
* Run the [**display vbst port-vlan statistics**](cmdqueryname=display+vbst+port-vlan+statistics) command to check PV statistics on a VBST-enabled device.
* Run the [**display stp**](cmdqueryname=display+stp) **vlan** *vlan-id* **v-vbst** command to check the V-VBST calculation result of the spanning tree in a specified VLAN.