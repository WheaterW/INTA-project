Configuring an IPv6 IS-IS Link Group
====================================

Configuring an IPv6 IS-IS Link Group

#### Prerequisites

Before configuring an IPv6 IS-IS link group, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

A link group consists of multiple links that are used for traffic forwarding. If a failure occurs on one or more of the links and the bandwidth of the other links in the group is not sufficient to carry the traffic, the link group automatically increases the cost of the available links. As a result, the routes using the member links in this link group are not preferentially selected and traffic is then switched to a backup link, which prevents traffic loss. If the link failure is cleared, the link group can automatically restore the original link cost so that routes are recalculated and traffic is then forwarded along the optimal route.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an IS-IS process and enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ] [ vpn-instance vpn-instance-name ]
   ```
   
   
   
   *process-id* specifies an IS-IS process ID. If the *process-id* parameter is not specified, the system creates process 1 by default. If a VPN instance is specified, the IS-IS process belongs to this VPN instance. If no VPN instance is specified, the process belongs to the public network instance.
3. Create a link group and enter the IS-IS link group view.
   
   
   ```
   [link-group](cmdqueryname=link-group) group-name
   ```
4. Configure a value for the device to automatically adjust the link costs of member links in the link group.
   
   
   ```
   [cost-offset](cmdqueryname=cost-offset) { cost | max-reachable | maximum }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If **maximum** is specified in the command, the routes using the member links in the link group are used to transmit TE information, but are not selected for traffic forwarding after the link cost is adjusted.
5. Set *min-num* to trigger automatic link cost adjustment when the number of available member links in the link group falls below the configured *min-num*.
   
   
   ```
   [min-members](cmdqueryname=min-members) min-num
   ```
   
   By default, the minimum number of available member links in the link group is 2.
6. Set *revert-num* to trigger automatic link cost restoration when the number of available member links in the link group reaches or exceeds the configured *revert-num*. 
   
   
   ```
   [revert-members](cmdqueryname=revert-members) revert-num
   ```
   By default, the value of *revert-num* is the same as that of *min-num* configured in the previous step. If *min-num* is not configured, the value of *revert-num* is 2.![](public_sys-resources/note_3.0-en-us.png) 
   
   The value of *revert-num* must not be less than that of *min-number*.
7. Exit the IS-IS link group view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Exit the IS-IS view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
10. Switch the interface working mode from Layer 2 to Layer 3.
    
    
    ```
    [undo portswitch](cmdqueryname=undo+portswitch)
    ```
    
    Determine whether to perform this step based on the current interface working mode.
11. Bind the interface to the link group.
    
    
    ```
    [isis ipv6 link-group](cmdqueryname=isis+ipv6+link-group) group-name [ level-1 | level-2 ]
    ```
    
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    To bind multiple interfaces to the link group, repeat Steps 9, 10, and 11.
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display isis link-group**](cmdqueryname=display+isis+link-group) [*process-id* ] [*group-name* ] command to check IS-IS link group information.

Run the [**display isis link-group interface**](cmdqueryname=display+isis+link-group+interface) *interface-type* *interface-number* command to check information about the link group to which a specified IS-IS interface is added.