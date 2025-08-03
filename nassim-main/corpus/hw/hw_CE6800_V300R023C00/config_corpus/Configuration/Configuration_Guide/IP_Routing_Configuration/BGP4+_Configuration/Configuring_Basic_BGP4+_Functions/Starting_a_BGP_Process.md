Starting a BGP Process
======================

Starting a BGP Process

#### Prerequisites

Before configuring basic BGP4+ functions, you have completed the following task:

* Set data link layer protocol parameters and IPv6 addresses for interfaces to ensure that the data link layer protocol status of each interface is up.

#### Context

Basic BGP4+ functions must be configured first before you configure BGP4+ for inter-AS communication.

Starting a BGP process is a prerequisite for configuring basic BGP4+ functions. When starting a BGP process on a device, you need to specify the number of the AS to which the device belongs.

![](public_sys-resources/notice_3.0-en-us.png) 

Changing the router ID of BGP will cause the BGP connection between devices to be re-established.



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
   
   By default, BGP automatically selects a router ID in the system view as its router ID. For router ID selection rules in the system view, see the *Command Reference*.
   
   If two devices have different router IDs, an IBGP or EBGP connection can be established between them. If the router IDs are the same, only an EBGP connection can be established.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the IP address of a BGP device's physical interface is used as the router ID and this IP address changes, route flapping occurs. To enhance network stability, configuring the IP address of a loopback interface as the router ID is recommended.
   
   If no interface on a device is configured with an IPv4 address, you need to configure a router ID for the device.
5. (Optional) Terminate the BGP4+ sessions between the device and all its peers.
   
   
   ```
   [shutdown](cmdqueryname=shutdown)
   ```
   
   Frequent BGP4+ route flapping may occur during system upgrade and maintenance. To prevent this from impacting the network, perform this step.
   
   ![](public_sys-resources/notice_3.0-en-us.png) 
   
   After an upgrade or maintenance, run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to restore the BGP4+ sessions; if you do not run this command, BGP4+ functions will not work properly.
6. (Optional) Configure BGP4+ memory protection.
   
   
   ```
   [prefix memory-limit](cmdqueryname=prefix+memory-limit)
   ```
7. (Optional) Configure BGP4+ to minimize the priorities of routes to be advertised to BGP4+ peers when the peers go from down to up.
   
   
   ```
   [advertise lowest-priority all-address-family peer-up](cmdqueryname=advertise+lowest-priority+all-address-family+peer-up+delay) [ delay delay ]
   ```
   
   This command is used in scenarios where route advertisement is delayed to prevent long packet loss during a traffic switchback. If the [**advertise lowest-priority all-address-family peer-up**](cmdqueryname=advertise+lowest-priority+all-address-family+peer-up) command is not run, the routes with unchanged priorities are sent immediately after the peer relationship is established. If the [**advertise lowest-priority all-address-family peer-up**](cmdqueryname=advertise+lowest-priority+all-address-family+peer-up) command is run and a peer relationship is established, BGP advertises routes carrying the lowest priority (largest MED value and smallest Local\_Pref value) to the peer until the specified delay expires. BGP starts to advertise routes with the original priorities only after the delay expires.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To restore the priorities of routes to be advertised to BGP4+ peers when the peers go from down to up, run the [**reset bgp advertise lowest-priority all-address-family peer-up**](cmdqueryname=reset+bgp+advertise+lowest-priority+all-address-family+peer-up) command.
8. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
9. (Optional) Configure BGP to minimize the priorities of BGP routes to be advertised.
   
   
   ```
   [advertise lowest-priority on-startup](cmdqueryname=advertise+lowest-priority+on-startup+delay-time) [ delay-time time-value ]
   ```
   
   If the BGP routes advertised by a device when the device is delivering ARP entries after a restart are selected as optimal routes, traffic loss may occur. To prevent this problem, run the [**advertise lowest-priority on-startup**](cmdqueryname=advertise+lowest-priority+on-startup) command before the device is restarted to configure BGP to minimize the priorities of the BGP routes to be advertised. After the command is run, the MED and Local\_Pref of the BGP routes to be advertised are changed to 4294967295 and 0, respectively, which prevents the BGP routes from being preferentially selected. To configure the device to restore the original priorities of these routes after delivering ARP entries, run the [**reset bgp advertise lowest-priority on-startup**](cmdqueryname=reset+bgp+advertise+lowest-priority+on-startup) command.
   
   Alternatively, you can also run the [**advertise lowest-priority on-startup**](cmdqueryname=advertise+lowest-priority+on-startup+delay-time) **delay-time** *time-value* command before the device restarts to ensure that the priorities of the routes advertised by the device are the lowest among the routes of the same type within the configured delay after the device restarts. ARP entry delivery completes within the delay time. After the delay time expires, the original priorities of the routes advertised by the device are automatically restored. Within the delay, you can also run the [**reset bgp advertise lowest-priority on-startup**](cmdqueryname=reset+bgp+advertise+lowest-priority+on-startup) command to restore the original priorities of the routes advertised by the device.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the [**advertise lowest-priority on-startup**](cmdqueryname=advertise+lowest-priority+on-startup) command is run after BGP configurations are committed, the command configuration takes effect only after the configurations are saved and the [**reboot**](cmdqueryname=reboot) command is run. If the [**advertise lowest-priority on-startup**](cmdqueryname=advertise+lowest-priority+on-startup) command and BGP configurations are committed together, the command configuration takes effect immediately.
10. (Optional) Configure a delay for BGP4+ route advertisement after a device restart.
    
    
    ```
    [advertise delay on-startup delay-time](cmdqueryname=advertise+delay+on-startup+delay-time) time-value
    ```
    
    The [**advertise delay on-startup delay-time**](cmdqueryname=advertise+delay+on-startup+delay-time) configuration takes effect only after it is saved and the [**reboot**](cmdqueryname=reboot) command is run.
    
    After a device is restarted, traffic loss may occur if the device advertises routes during ARP entry delivery. To prevent this issue, you can run the [**advertise delay on-startup delay-time**](cmdqueryname=advertise+delay+on-startup+delay-time) command before restarting the device to configure a delay for advertising BGP4+ routes after the device restarts. The command specifies how long the device must wait after a restart before it starts to advertise BGP4+ routes. To allow the device to advertise BGP4+ routes immediately after ARP entries are delivered, run the [**refresh bgp all export**](cmdqueryname=refresh+bgp+all+export), [**refresh bgp ipv6 all export**](cmdqueryname=refresh+bgp+ipv6+all+export), or [**reset bgp advertise delay on-startup**](cmdqueryname=reset+bgp+advertise+delay+on-startup) command.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```