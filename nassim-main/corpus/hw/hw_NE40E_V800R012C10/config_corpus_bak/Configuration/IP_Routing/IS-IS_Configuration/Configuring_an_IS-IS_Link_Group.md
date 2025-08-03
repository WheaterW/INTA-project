Configuring an IS-IS Link Group
===============================

If one of the links that are used for traffic forwarding fails, traffic may get lost. To prevent this problem, you can configure a link group.

#### Usage Scenario

A link group consists of multiple links that are used for traffic forwarding. If a failure occurs on one or more of the links and the bandwidth of the other links in the group is not sufficient to carry the traffic, the link group automatically increases the cost of the available links. As a result, the routes using the member links in this link group are not preferentially selected and traffic is then switched to a backup link, which prevents traffic loss. If the link failure is cleared, the link group can automatically restore the original link cost so that routes are recalculated and traffic is then forwarded along the optimal route.


#### Pre-configuration Tasks

Before configuring an IS-IS link group, [configure basic IS-IS functions (IPv4)](dc_vrp_isis_cfg_1000.html) or [configure basic IS-IS functions (IPv6)](dc_vrp_isis_cfg_1023.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**link-group**](cmdqueryname=link-group) *group-name*
   
   
   
   A link group is created, and the IS-IS link group view is displayed.
4. (Optional) Run [**cost-offset**](cmdqueryname=cost-offset) { *cost* | **max-reachable** | **maximum** }
   
   
   
   The device is configured to automatically adjust the link costs of member links in the link group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If **maximum** is specified in the command and automatic cost adjustment is triggered, the links in the link group are used to transmit TE information, but not selected for traffic forwarding.
5. (Optional) Run [**min-members**](cmdqueryname=min-members) *min-num*
   
   
   
   The device is configured to automatically adjust the costs of all links in the link group when the number of available member links in the link group falls below *min-num*.
6. (Optional) Run [**revert-members**](cmdqueryname=revert-members) *revert-num*
   
   
   
   The device is configured to automatically restore the original costs of all links in the link group when the number of member links in the link group is greater than or equal to *revert-num*.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The value of *revert-num* must be greater than or equal to that of *min-number*.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the IS-IS link group view.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the IS-IS view.
9. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
10. Run 
    
    
    
    The interface is bound to the link group.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    To bind multiple interfaces to the link group, repeat steps 9 and 10.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

An IS-IS link group has been configured.

* Run the [**display isis link-group**](cmdqueryname=display+isis+link-group) [*process-id* ] [*group-name* ] command to check IS-IS link group information.
* Run the [**display isis link-group interface**](cmdqueryname=display+isis+link-group+interface) *interface-type* *interface-number* command to check information about the link group to which an IS-IS interface is added.