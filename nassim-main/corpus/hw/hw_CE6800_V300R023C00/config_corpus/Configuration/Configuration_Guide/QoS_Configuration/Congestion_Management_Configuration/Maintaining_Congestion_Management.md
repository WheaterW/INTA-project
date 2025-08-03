Maintaining Congestion Management
=================================

Maintaining Congestion Management

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after they are cleared. Exercise caution when clearing the statistics.



#### Procedure

* Clear queue-based traffic statistics.
  
  
  ```
  [reset qos queue statistics](cmdqueryname=reset+qos+queue+statistics) { interface { interface-type interface-number | interface-name } | slot slot-id }
  ```
* Clear statistics on the buffer usage.
  
  
  ```
  [reset qos buffer-usage](cmdqueryname=reset+qos+buffer-usage) [ slot slot-id | interface { interface-type interface-number | interface-name } ]
  ```
* Clear statistics on discarded incoming packets in the buffer.
  
  
  
  For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
  
  ```
  reset qos buffer ingress-statistics [ [slot](cmdqueryname=slot) slot-id ]
  ```
  
  For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ:
  
  ```
  reset qos buffer ingress-statistics [ interface { interface-type interface-number | interface-name } ]
  ```