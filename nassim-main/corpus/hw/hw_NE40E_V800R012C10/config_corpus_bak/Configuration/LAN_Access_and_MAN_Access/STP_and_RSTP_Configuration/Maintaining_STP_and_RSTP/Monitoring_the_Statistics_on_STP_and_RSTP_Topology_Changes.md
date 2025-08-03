Monitoring the Statistics on STP/RSTP Topology Changes
======================================================

The statistics about STP/Rapid Spanning Tree Protocol (RSTP) topology changes can be viewed. If the statistics increase, network flapping occurs.

#### Procedure

* Run the [**display stp**](cmdqueryname=display+stp) **topology-change** command to view the statistics about STP/RSTP topology changes.
* Run the [**display stp**](cmdqueryname=display+stp) [ **interface** *interface-type interface-number* | **vsi** *vsi-name* **pw** *pw-name* | **slot** *slot-id* ] **tc-bpdu statistics** command to view the statistics about sent and received Topology Change (TC)/Topology Change Notification (TCN) packets.