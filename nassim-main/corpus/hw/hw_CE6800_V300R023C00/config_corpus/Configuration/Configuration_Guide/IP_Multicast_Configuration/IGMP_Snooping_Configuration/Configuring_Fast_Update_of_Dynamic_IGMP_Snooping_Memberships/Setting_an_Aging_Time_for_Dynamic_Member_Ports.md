Setting an Aging Time for Dynamic Member Ports
==============================================

Setting an Aging Time for Dynamic Member Ports

#### Context

A device sets an aging time for a member port depending on the type of the IGMP message received:

* If a Report message is received from a downstream host, the device determines the aging time of the member port as follows: Robustness variable x General Query interval + Maximum response time.
* If a Leave message is received from a downstream host, the device determines the aging time of the member port as follows: Robustness variable x Group-Specific Query interval.

When deploying a Layer 2 multicast network, ensure that all Layer 2 multicast devices use the same parameter values (especially the General Query interval of IGMP snooping) to calculate the aging time of dynamic member ports. Otherwise, Layer 2 multicast services cannot run properly.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Set a General Query interval for IGMP snooping.
   
   
   ```
   [igmp snooping query interval](cmdqueryname=igmp+snooping+query+interval) QueryIntervalValue
   ```
   
   By default, the General Query interval of IGMP snooping is 60 seconds.
4. Set a robustness variable for IGMP snooping.
   
   
   ```
   [igmp snooping robust-count](cmdqueryname=igmp+snooping+robust-count) robust-count-value
   ```
   
   By default, the robustness variable of IGMP snooping is 2.
5. Set a maximum response time for IGMP snooping.
   
   
   ```
   [igmp snooping query max-response-time](cmdqueryname=igmp+snooping+query+max-response-time) QueryRspIntValue
   ```
   
   By default, the maximum response time of IGMP snooping is 10 seconds.
6. Set a Group-Specific Query interval for IGMP snooping.
   
   
   ```
   [igmp snooping query last-member-interval](cmdqueryname=igmp+snooping+query+last-member-interval) LastMemQIValue
   ```
   
   By default, the Group-Specific Query interval of IGMP snooping is 1 second.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```