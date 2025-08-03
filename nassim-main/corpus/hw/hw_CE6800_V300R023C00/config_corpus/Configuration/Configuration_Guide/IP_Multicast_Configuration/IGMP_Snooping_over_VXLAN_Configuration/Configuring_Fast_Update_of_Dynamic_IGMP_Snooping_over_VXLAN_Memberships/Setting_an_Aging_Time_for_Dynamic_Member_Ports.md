Setting an Aging Time for Dynamic Member Ports
==============================================

Setting an Aging Time for Dynamic Member Ports

#### Context

A device sets an aging time for a member port depending on the type of IGMP message it receives:

* If the member port receives a Report message from a downstream host, the device determines the aging time of this port as follows: Robustness variable x Interval at which General Query messages are sent + Maximum response time.
* If the member port receives a Leave message from a downstream host, the device determines the aging time of this port as follows: Interval at which Group-Specific Query messages are sent x Robustness variable.

When deploying a Layer 2 multicast network, ensure that all Layer 2 multicast devices use the same parameter values (especially the General Query interval of IGMP snooping) to calculate the aging time of dynamic member ports. Otherwise, Layer 2 multicast services cannot run properly.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Set an aging time for dynamic member ports.
   
   
   
   **Table 1** Setting an aging time for dynamic member ports
   | Operation | Command |
   | --- | --- |
   | Set an interval at which General Query messages are sent for IGMP snooping. | [**igmp snooping query interval**](cmdqueryname=igmp+snooping+query+interval) *QueryIntervalValue* |
   | Set a robustness variable for IGMP snooping. | [**igmp snooping robust-count**](cmdqueryname=igmp+snooping+robust-count) *robust-count-value* |
   | Set a maximum response time for IGMP snooping. | [**igmp snooping query max-response-time**](cmdqueryname=igmp+snooping+query+max-response-time) *QueryRspIntValue* |
   | Set an interval at which Group-Specific Query messages are sent for IGMP snooping. | [**igmp snooping query lastmember-queryinterval**](cmdqueryname=igmp+snooping+query+lastmember-queryinterval) *LastMemQIValue* |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```