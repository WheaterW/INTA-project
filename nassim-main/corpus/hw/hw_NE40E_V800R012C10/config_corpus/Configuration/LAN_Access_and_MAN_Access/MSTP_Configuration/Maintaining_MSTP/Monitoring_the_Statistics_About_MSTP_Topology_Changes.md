Monitoring the Statistics About MSTP Topology Changes
=====================================================

The statistics about Multiple Spanning Tree Protocol (MSTP) topology changes can be viewed. If the statistics increase, network flapping occurs.

#### Procedure

* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] **topology-change** command to view the statistics about MSTP topology changes.
  
  
  
  In the case of a process with a non-zero ID, run the [**stp process**](cmdqueryname=stp+process) *process-id* command to create a process before running the preceding command.
* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] [ **interface** *interface-type interface-number* | **vsi** *vsi-name* **pw** *pw-name* | **slot** *slot-id* ] **tc-bpdu statistics** command to view the statistics about Topology Change/Topology Change Notification (TC/TCN) packets.
  
  
  
  In the case of a process with a non-zero ID, run the [**stp process**](cmdqueryname=stp+process) *process-id* command to create a process before running the preceding command.