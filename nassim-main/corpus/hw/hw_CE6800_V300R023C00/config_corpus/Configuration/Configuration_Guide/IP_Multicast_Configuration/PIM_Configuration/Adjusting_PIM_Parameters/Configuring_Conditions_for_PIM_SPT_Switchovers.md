Configuring Conditions for PIM SPT Switchovers
==============================================

Configuring Conditions for PIM SPT Switchovers

#### Prerequisites

Before configuring conditions for PIM SPT switchovers, enable IPv4 multicast routing in the public network instance.


#### Context

A high volume of multicast data traffic may overload an RP and thereby cause faults. To reduce the burden of the RP, you can configure conditions for a receiver DR to initiate an SPT switchover towards the source.

By default, a receiver DR initiates an SPT switchover towards the source after receiving the first copy of multicast data packets. You can configure a traffic rate threshold on a receiver DR to trigger an SPT switchover or prevent the DR from triggering an SPT switchover.


#### Default Configuration

[Table 1](#EN-US_TASK_0000001846644908__tab_01) lists the default configuration of SPT switchover conditions.

**Table 1** Default configuration of SPT switchover conditions
| Parameter | Default Value |
| --- | --- |
| Group policy that specifies the groups to which the SPT switchover conditions apply | No group policy is configured. The SPT switchover conditions apply to all multicast groups. |
| Interval for checking the multicast data forwarding rate | 15s |



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an ACL and enter the ACL view.
   
   
   ```
   [acl](cmdqueryname=acl) { name basic-acl-name basic | [ number ] basic-acl-number }
   ```
3. Configure an ACL rule.
   
   
   ```
   [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment-type fragment | source { source-ip-address { source-wildcard | 0 | src-netmast } | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
   ```
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
   ```
6. Configure SPT switchover conditions.
   
   
   ```
   [spt-switch-threshold](cmdqueryname=spt-switch-threshold) { traffic-rate | infinity } [ group-policy { basic-acl-number | acl-name acl-name } [ order order-value ] ]
   ```
   
   
   
   The ACL takes effect as follows:
   
   * If a multicast group matches an ACL rule and the action is **permit**, the device applies the specified rate threshold to this group.
   * If a multicast group matches an ACL rule and the action is **deny**, the device performs an SPT switchover immediately.
   * If a multicast group does not match any ACL rule or if the specified ACL does not exist or does not contain rules, the device performs an SPT switchover immediately.
7. (Optional) Set the interval for checking the multicast data forwarding rate.
   
   
   ```
   [timer spt-switch](cmdqueryname=timer+spt-switch) interval
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```