Starting a BGP Process
======================

Starting a BGP Process

#### Prerequisites

Before configuring basic BGP functions, you have completed the following task:

* Set data link layer protocol parameters and IP addresses for interfaces to ensure that the data link layer protocol status on each interface is up.

#### Context

Building a BGP network can implement communication between different ASs. Configuring basic BGP functions is a prerequisite for such a BGP network, and includes the following steps:

* Create a BGP process: This step is a prerequisite for configuring all BGP functions.
* Establish BGP peer relationships: Devices can exchange BGP routing information only after peer relationships are established between them.
* Import routes: BGP itself cannot discover routes. Instead, it needs to import routes discovered by non-BGP protocols to generate BGP routes.

![](public_sys-resources/note_3.0-en-us.png) 

To facilitate configuration, the commands in the BGP-IPv4 unicast address family view can be run in the BGP view. However, in configuration files, these commands are still displayed in the BGP-IPv4 unicast address family view.

To prevent the commands of the BGP-IPv4 unicast address family from being executed in the BGP view, run the [**bgp default ipv4-unicast-config disable**](cmdqueryname=bgp+default+ipv4-unicast-config+disable) command.

Starting a BGP process is a prerequisite for configuring basic BGP functions. When starting a BGP process on a device, you need to specify the number of the AS to which the device belongs.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enable BGP routing loop detection.
   
   
   ```
   [route loop-detect bgp enable](cmdqueryname=route+loop-detect+bgp+enable)
   ```
   
   After this function is enabled, the device reports an alarm when detecting a BGP routing loop. Because the device cannot determine whether the routing loop is removed, the alarm will not be cleared automatically even if the routing loop is removed. To manually clear the BGP routing loop alarm, run the [**clear route loop-detect bgp alarm**](cmdqueryname=clear+route+loop-detect+bgp+alarm) command.
3. Enable BGP (with the local AS number specified), and enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
4. (Optional) Configure a BGP router ID.
   
   
   ```
   [router-id](cmdqueryname=router-id) ipv4-address
   ```
   
   Configuring a new BGP router ID or changing the existing one will reset the BGP peer relationship between devices.
   
   If two devices have different router IDs, an IBGP or EBGP connection can be established between them. If the router IDs are the same and the [**router-id allow-same enable**](cmdqueryname=router-id+allow-same+enable) command is run, an EBGP connection can be established.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   By default, BGP automatically selects a router ID in the system view as its router ID. If the IP address of a physical interface is used as the router ID, route flapping occurs when this IP address changes. To enhance network stability, configuring the IP address of a loopback interface as the router ID is recommended. For rules in selecting router IDs from the system view, see the [**router-id**](cmdqueryname=router-id) command description.
   
   By default, Cluster\_List comparison takes precedence over router ID comparison during BGP route selection. To enable router ID comparison to take precedence over Cluster\_List comparison during BGP route selection, run the [**bestroute routerid-prior-clusterlist**](cmdqueryname=bestroute+routerid-prior-clusterlist) command.
5. (Optional) Terminate the BGP sessions between the device and all its BGP peers.
   
   
   ```
   [shutdown](cmdqueryname=shutdown)
   ```
   
   
   
   Frequent BGP route flapping may occur during system upgrade and maintenance. To prevent this from impacting the network, perform this step.
   
   ![](public_sys-resources/notice_3.0-en-us.png) 
   
   After an upgrade or maintenance, run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to restore the BGP sessions; if you do not run this command, BGP functions will not work properly.
6. (Optional) Configure BGP memory protection.
   
   
   ```
   [prefix memory-limit](cmdqueryname=prefix+memory-limit)
   ```
7. (Optional) Configure BGP to minimize the priorities of BGP routes to be advertised.
   
   
   ```
   [advertise lowest-priority on-startup](cmdqueryname=advertise+lowest-priority+on-startup+delay-time) [ delay-time time-value ]
   ```
   
   During ARP entry delivery triggered upon a device restart, if the BGP routes advertised by the device are selected as optimal routes, traffic loss may occur. To prevent this problem, run the **advertise lowest-priority on-startup** command before the device is restarted to configure BGP to minimize the priorities of BGP routes to be advertised to peers. After configuration, the MED and Local\_Pref of the BGP routes are changed to 4294967295 and 0, respectively. This ensures that BGP routes advertised by the device after restart have the lowest priority. To configure the device to restore the original priorities of these routes after delivering ARP entries, run the [**reset bgp advertise lowest-priority on-startup**](cmdqueryname=reset+bgp+advertise+lowest-priority+on-startup) command.
   
   Alternatively, you can also run the [**advertise lowest-priority on-startup**](cmdqueryname=advertise+lowest-priority+on-startup+delay-time) **delay-time** *time-value* command before the device restarts to ensure that the priorities of the routes advertised by the device are the lowest among the routes of the same type within the configured delay after the device restarts. ARP entry delivery completes within the delay time. After the delay time expires, the original priorities of the routes advertised by the device are automatically restored. Within the delay, you can also run the [**reset bgp advertise lowest-priority on-startup**](cmdqueryname=reset+bgp+advertise+lowest-priority+on-startup) command to restore the original priorities of the routes advertised by the device.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the [**advertise lowest-priority on-startup**](cmdqueryname=advertise+lowest-priority+on-startup) command is run after BGP configurations are committed, the command configuration takes effect only after the configurations are saved and the [**reboot**](cmdqueryname=reboot) command is run. If the [**advertise lowest-priority on-startup**](cmdqueryname=advertise+lowest-priority+on-startup) command and BGP configurations are committed together, the command configuration takes effect immediately.
8. (Optional) Configure BGP to minimize the priorities of routes to be advertised to BGP peers when the peers go from down to up.
   
   
   ```
   [advertise lowest-priority all-address-family peer-up](cmdqueryname=advertise+lowest-priority+all-address-family+peer-up+delay) [ delay delay ]
   ```
   
   This command is used in scenarios where route advertisement is delayed to prevent long packet loss during a traffic switchback. If the [**advertise lowest-priority all-address-family peer-up**](cmdqueryname=advertise+lowest-priority+all-address-family+peer-up) command is not run, the routes with unchanged priorities are sent immediately after the peer relationship is established. If the [**advertise lowest-priority all-address-family peer-up**](cmdqueryname=advertise+lowest-priority+all-address-family+peer-up) command is run and a peer relationship is established, BGP advertises routes carrying the lowest priority (largest MED value and smallest Local\_Pref value) to the peer until the specified delay expires. BGP starts to advertise routes with the original priorities only after the delay expires.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To restore the priorities of routes to be advertised to BGP peers when the peers go from down to up, run the [**reset bgp advertise lowest-priority all-address-family peer-up**](cmdqueryname=reset+bgp+advertise+lowest-priority+all-address-family+peer-up) command.
9. (Optional) Configure a delay for BGP route advertisement after a device restart.
   
   
   ```
   [advertise delay on-startup delay-time](cmdqueryname=advertise+delay+on-startup+delay-time) time-value
   ```
   
   The [**advertise delay on-startup delay-time**](cmdqueryname=advertise+delay+on-startup+delay-time) configuration takes effect only after it is saved and the [**reboot**](cmdqueryname=reboot) command is run.
   
   After a device is restarted, traffic loss may occur if the device advertises routes during ARP entry delivery. To prevent this issue, you can run the [**advertise delay on-startup delay-time**](cmdqueryname=advertise+delay+on-startup+delay-time) command before restarting the device to configure a delay for advertising BGP routes after the device restarts. The command specifies how long the device must wait after a restart before it starts to advertise BGP routes. To allow the device to advertise BGP routes immediately after ARP entries are delivered, run the [**refresh bgp all export**](cmdqueryname=refresh+bgp+all+export) or [**reset bgp advertise delay on-startup**](cmdqueryname=reset+bgp+advertise+delay+on-startup) command.
10. (Optional) Configure BGP to record peer state changes and event information.
    
    
    ```
    [peer](cmdqueryname=peer) { ipv4-address | group-name } [log-change](cmdqueryname=log-change)
    ```
    
    System log files serve as an important reference for locating network connectivity and stability problems. If an error occurs on a connection between BGP peers, a corresponding error code and subcode are generated. Upon receiving a Notification message from a peer, the local device records the error code and subcode carried in the received message, and the state of the FSM on the local device changes. As a result, the connection between the local device and peer is terminated. If an error occurs on the local device, the state of the FSM on the local device changes, and the local device sends a Notification message to the peer.
    
    By default, BGP records peer state changes and event information in system log files. The recorded information includes BGP error codes and subcodes, changes in the state of the BGP FSM, and whether Notification messages are sent.
    
    If you do not need BGP to record peer state changes or event information, run the [**undo peer log-change**](cmdqueryname=undo+peer+log-change) command. After the [**undo peer log-change**](cmdqueryname=undo+peer+log-change) command is run, BGP records only the last peer state change in a log file. You can run the [**display bgp peer**](cmdqueryname=display+bgp+peer) **log-info** command to view this log.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```