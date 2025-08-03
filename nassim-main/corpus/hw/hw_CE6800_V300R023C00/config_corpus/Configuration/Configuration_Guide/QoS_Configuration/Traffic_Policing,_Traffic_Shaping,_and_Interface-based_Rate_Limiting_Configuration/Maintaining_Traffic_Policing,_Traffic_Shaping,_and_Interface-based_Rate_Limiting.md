Maintaining Traffic Policing, Traffic Shaping, and Interface-based Rate Limiting
================================================================================

Maintaining Traffic Policing, Traffic Shaping, and Interface-based Rate Limiting

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

Flow-based traffic statistics cannot be restored after they are cleared. Exercise caution when running the below commands.



#### Procedure

* Clear the statistics about packets forwarded and discarded on a specified interface for which traffic policing is configured to implement interface-based rate limiting.
  
  
  ```
  [reset qos car statistics](cmdqueryname=reset+qos+car+statistics) interface { interface-type interface-number | interface-name } inbound
  ```
  
  Traffic policing cannot be configured on the CE6885-LL (low latency mode). Therefore, this command cannot be configured.
* Clear queue-based traffic statistics.
  
  
  ```
  [reset qos queue statistics](cmdqueryname=reset+qos+queue+statistics) { interface { interface-type interface-number | interface-name } | slot slot-id }
  ```