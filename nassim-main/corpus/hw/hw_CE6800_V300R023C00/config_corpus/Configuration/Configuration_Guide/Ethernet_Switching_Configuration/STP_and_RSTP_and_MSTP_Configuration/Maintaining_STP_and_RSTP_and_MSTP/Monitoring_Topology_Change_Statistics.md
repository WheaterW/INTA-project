Monitoring Topology Change Statistics
=====================================

Monitoring Topology Change Statistics

#### Context

Statistics about topology changes can be viewed. If these statistics increase, it can be determined that network flapping occurs.


#### Procedure

* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] [**topology-change**](cmdqueryname=topology-change) command to check topology change statistics.
* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] [ **interface** *interface-type interface-number* | **slot** *slot-id* ] **tc-bpdu statistics** command to check the statistics for sent and received TC/TCN BPDUs.