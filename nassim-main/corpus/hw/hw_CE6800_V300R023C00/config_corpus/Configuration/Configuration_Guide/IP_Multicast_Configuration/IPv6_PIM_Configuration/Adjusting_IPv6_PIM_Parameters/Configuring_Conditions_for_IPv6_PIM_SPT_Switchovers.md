Configuring Conditions for IPv6 PIM SPT Switchovers
===================================================

Configuring Conditions for IPv6 PIM SPT Switchovers

#### Prerequisites

Before configuring conditions for IPv6 PIM SPT switchovers, enable IPv6 multicast routing in the public network instance.


#### Context

A high volume of multicast data traffic may overload an RP and thereby cause faults. To reduce the burden of the RP, you can configure conditions for a receiver DR to initiate an SPT switchover towards the source.

By default, a receiver DR initiates an SPT switchover towards the source after receiving the first copy of multicast data packets. You can configure a traffic rate threshold on a receiver DR to trigger an SPT switchover or prevent the DR from triggering an SPT switchover.


#### Default Configuration

[Table 1](#EN-US_TASK_0000001618336281__tab_01) lists the default configuration of SPT switchover conditions.

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
2. Create an ACL6 and enter the ACL6 view.
   
   
   ```
   [acl ipv6](cmdqueryname=acl+ipv6) { name basic-acl6-name basic | [ number ] basic-acl6-number }
   ```
3. Configure a rule for the ACL6.
   
   
   ```
   [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment | source { source-ipv6-address { prefix-length | source-wildcard } | source-ipv6-address/prefix-length | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
   ```
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the IPv6 PIM view.
   
   
   ```
   [pim ipv6](cmdqueryname=pim+ipv6) [ vpn-instance vpn-instance-name ]
   ```
6. Configure SPT switchover conditions.
   
   
   ```
   [spt-switch-threshold](cmdqueryname=spt-switch-threshold) { traffic-rate | infinity } [ group-policy { basic-acl6-number | acl6-name acl6-name } [ order order-value ] ]
   ```
   
   
   
   The ACL6 takes effect as follows:
   
   * If a multicast group matches an ACL6 rule and the action is **permit**, the device applies the specified rate threshold to this group.
   * If a multicast group matches an ACL6 rule and the action is **deny**, the device performs an SPT switchover immediately.
   * If a multicast group does not match any ACL6 rule or if the specified ACL6 does not exist or does not contain rules, the device performs an SPT switchover immediately.
7. (Optional) Set the interval for checking the multicast data forwarding rate.
   
   
   ```
   [timer spt-switch](cmdqueryname=timer+spt-switch) interval
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```