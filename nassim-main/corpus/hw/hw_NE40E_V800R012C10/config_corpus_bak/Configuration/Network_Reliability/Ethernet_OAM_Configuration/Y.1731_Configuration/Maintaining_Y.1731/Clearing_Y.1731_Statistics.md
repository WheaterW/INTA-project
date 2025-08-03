Clearing Y.1731 Statistics
==========================

Before collecting statistics about Y.1731 packets within a specified period, you must clear the existing statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Y.1731 statistics cannot be restored after being cleared. Exercise caution when clearing Y.1731 statistics.



#### Procedure

* Clear statistics aboutpoint-to-multipoint single-ended frame loss measurement.
  
  
  
  Run the [**reset y1731 statistic-type**](cmdqueryname=reset+y1731+statistic-type) **single-loss** **test-id** *test-id* command in the user view.
* Clear statistics about point-to-multipoint two-way frame delay measurement.
  
  
  
  Run the [**reset y1731 statistic-type**](cmdqueryname=reset+y1731+statistic-type) **twoway-delay** **test-id** *test-id* command in the user view.
* Clear statistics about point-to-multipoint one-way frame delay measurement.
  
  
  
  Run the [**reset y1731 statistic-type**](cmdqueryname=reset+y1731+statistic-type) **oneway-delay** **test-id** *test-id* command in the user view.
* Clear statistics about point-to-multipoint single-ended SLM.
  
  
  
  Run the [**reset y1731 statistic-type**](cmdqueryname=reset+y1731+statistic-type) **single-synthetic-loss** **test-id** *test-id* command in the user view.
* Run [**commit**](cmdqueryname=commit)
  
  
  
  The configuration is committed.