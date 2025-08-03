Setting an Aging Time for Dynamic Member Ports
==============================================

Setting an Aging Time for Dynamic Member Ports

#### Context

A device sets an aging time for a member port depending on the type of the MLD message received:

* If the member port receives a Report message from a downstream host, the device determines the aging time of this port as follows: Robustness variable x Interval at which General Query messages are sent + Maximum response time.
* If the member port receives a Done message from a downstream host, the device determines the aging time of this port as follows: Interval at which Group-Specific Query messages are sent x Robustness variable.

When deploying a Layer 2 multicast network, ensure that all Layer 2 multicast devices use the same parameter values (especially the General Query interval of MLD snooping) to calculate the aging time of dynamic member ports. Otherwise, Layer 2 multicast services cannot run properly.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Set an aging time for dynamic member ports as required.
   
   
   * Set a General Query interval for MLD snooping.
     ```
     [mld snooping query interval](cmdqueryname=mld+snooping+query+interval) query-interval
     ```
     
     By default, the General Query interval for MLD snooping is 125s.
   
   
   * Set a robustness variable for MLD snooping.
     ```
     [mld snooping robust-count](cmdqueryname=mld+snooping+robust-count) robust-count
     ```
     
     By default, the robustness variable of MLD snooping is 2.
   
   
   * Set a maximum response time for MLD snooping.
     ```
     [mld snooping query max-response-time](cmdqueryname=mld+snooping+query+max-response-time) max-response-time
     ```
     
     By default, the maximum response time of MLD snooping is 10s.
   
   
   * Set a Group-Specific Query interval for MLD snooping.
     ```
     [mld snooping query last-member-interval](cmdqueryname=mld+snooping+query+last-member-interval) lastmember-queryinterval
     ```
     
     By default, the Group-Specific Query interval of MLD snooping is 1s.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```