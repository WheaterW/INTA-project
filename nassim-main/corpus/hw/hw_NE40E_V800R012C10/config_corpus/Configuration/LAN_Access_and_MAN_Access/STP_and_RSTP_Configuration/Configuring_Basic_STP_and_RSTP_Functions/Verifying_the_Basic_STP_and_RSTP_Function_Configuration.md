Verifying the Basic STP/RSTP Function Configuration
===================================================

After basic STP/Rapid Spanning Tree Protocol (RSTP) functions are configured, you can view the information such as the port role and port status to check whether the spanning tree calculation is correctly performed.

#### Prerequisites

All configurations of basic STP/RSTP functions are complete.


#### Procedure

* Run the [**display stp**](cmdqueryname=display+stp) [ **interface** *interface-type interface-number* ] [ **brief** ] command to view spanning-tree status and statistics.
* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] **abnormal-interface** command to view information about abnormal interfaces running the Spanning Tree Protocol (STP).