Maintaining Differentiated Flow Scheduling
==========================================

Maintaining Differentiated Flow Scheduling

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after they are cleared. Exercise caution when clearing the statistics.



#### Procedure

* Clears statistics about mice flows on an interface where differentiated flow scheduling is enabled. (This command is available only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.)
  
  
  ```
  [reset mice-elephant-flow statistics](cmdqueryname=reset+mice-elephant-flow+statistics) [ interface { interface-name | interface-type interface-number } ]
  ```