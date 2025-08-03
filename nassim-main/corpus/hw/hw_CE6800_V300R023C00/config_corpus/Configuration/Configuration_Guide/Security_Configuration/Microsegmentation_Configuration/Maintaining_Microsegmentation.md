Maintaining Microsegmentation
=============================

Maintaining microsegmentation includes clearing microsegmentation statistics and EPG statistics.

#### Clearing Statistics

To re-collect microsegmentation statistics, run the commands listed in the table below to clear existing statistics.

![](../public_sys-resources/caution_3.0-en-us.png) 

Statistics cannot be restored after they are cleared. Exercise caution when clearing them.


**Table 1** Clearing statistics
| Operation | Command |
| --- | --- |
| Clear packet statistics of a segment policy. | **[**reset segment-policy statistics**](cmdqueryname=reset+segment-policy+statistics)**  **policy-name** [ **class** **class-name** ] **slot** **slot-id** |
| Clear EPG statistics. | **[**reset traffic-segment statistics**](cmdqueryname=reset+traffic-segment+statistics)**  { **segment-id** **id-value**  | **segment-name** **name**  } **slot** *slot-id* |