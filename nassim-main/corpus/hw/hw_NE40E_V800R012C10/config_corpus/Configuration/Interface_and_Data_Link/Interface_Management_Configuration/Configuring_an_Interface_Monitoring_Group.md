Configuring an Interface Monitoring Group
=========================================

You can configure an interface monitoring group in a dual-device backup scenario to allow the user-side interface status to change with the network-side interface status so that traffic can be switched between the master and backup links.

#### Usage Scenario

When a network-side interface goes Down in a dual-device backup scenario, user-side devices cannot detect the Down event and therefore do not switch traffic to the backup link. As a result, traffic overloads or interruptions occur. To prevent these problems, you can configure an interface monitoring group to monitor the network-side interface status and instruct the user-side interface to change its status accordingly. An interface monitoring group allows traffic to be switched between the master and backup links and prevents traffic overloads or interruptions.

On the network shown in [Figure 1](#EN-US_TASK_0172362610__fig_dc_vrp_ifm_cfg_002801), PE2 backs up PE1. NPE1 through NPEM on the user side is dual-homed to the two PEs to load-balance traffic, and the two PEs are connected to DeviceA through DeviceN on the network side. When only the link between PE1 and DeviceN is available and all the links between PE1 and all the other routers fail, the NPEs do not detect the failure and continue sending packets to DeviceN through PE1. As a result, the link between PE1 and DeviceN becomes overloaded.

**Figure 1** Typical application of an interface monitoring group  
![](images/fig_dc_vrp_ifm_cfg_002801.png "Click to enlarge")  

To resolve this problem, you can configure an interface monitoring group and add multiple network-side interfaces on the PEs to the interface monitoring group. When a link failure occurs on the network side and the interface monitoring group detects that the status of a certain proportion of network-side interfaces changes, the system instructs the user-side interfaces associated with the interface monitoring group to change their status accordingly and allows traffic to be switched between the master and backup links. Therefore, the interface monitoring group can be used to prevent traffic overloads or interruptions.


#### Pre-configuration Tasks

Before configuring an interface monitoring group, configure physical attributes for interfaces on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**monitor-group**](cmdqueryname=monitor-group) *monitor-group-name*
   
   
   
   An interface monitoring group is created, and the interface monitoring group view is displayed.
3. Run [**binding interface**](cmdqueryname=binding+interface) *interface-type* *interface-number* [ **down-weight** *down-weight-value* ]
   
   
   
   An interface is added to the interface monitoring group.
   
   The interface added to an interface monitoring group is called a binding interface. A binding interface is located on the network side and a track interface on the user side. An interface monitoring group monitors the binding interface status and allows the track interfaces to change their status accordingly.
   
   You can repeat this step to add multiple binding interfaces to an interface monitoring group.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit from the interface monitoring group view.
5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the specified interface on the user side is displayed.
6. Run [**track monitor-group**](cmdqueryname=track+monitor-group) *monitor-group-name* [ **trigger-down-weight** *trigger-down-weight-value* ]
   
   
   
   The interface is associated with an interface monitoring group.
   
   
   
   The user-side interface associated with an interface monitoring group is called a track interface.
   
   You can repeat steps 5 and 6 to associate multiple track interfaces to an interface monitoring group.
   
   If the down weight sum of all the binding interfaces in the monitoring group is greater than or equal to the value specified using *trigger-down-weight-value* on the track interface, the track interface goes down, and service traffic is switched to the backup link. Otherwise, the track interface goes up, and service traffic is switched back to the primary link.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit from the interface view.
8. Run [**monitor-group**](cmdqueryname=monitor-group) *monitor-group-name*
   
   
   
   The view of the created interface monitoring group is displayed.
9. (Optional) Run [**trigger-up-delay**](cmdqueryname=trigger-up-delay) *trigger-up-delay-value*
   
   
   
   The delay after which a track interface goes Up is set.
10. Run [**monitor enable**](cmdqueryname=monitor+enable)
    
    
    
    The monitoring function is enabled.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

Run the [**display monitor-group**](cmdqueryname=display+monitor-group) [ *monitor-group-name* ] command to view information about an interface monitoring group.