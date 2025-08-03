Configuring Dynamic Load Balancing for ECMP
===========================================

Configuring Dynamic Load Balancing for ECMP

#### Context

![](public_sys-resources/note_3.0-en-us.png) 

This configuration is supported only on the CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6885-SAN, and CE8851K.

In traditional static load balancing, the utilization of member links is not considered. This causes traffic to be unevenly load-balanced among the member links. If large data flows are transmitted, congestion or even packet loss occurs on the involved member links.

After dynamic load balancing is enabled, traffic is dynamically load-balanced among ECMP member links, ensuring optimal load balancing among them.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the ECMP view.
   
   
   ```
   [load-balance ecmp](cmdqueryname=load-balance+ecmp)
   ```
3. Configure a dynamic load balancing mode for ECMP.
   
   
   ```
   [ecmp mode](cmdqueryname=ecmp+mode) { spray | fixed | eligible [ flowlet-gap-time flowlet-gap-time ] }
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```