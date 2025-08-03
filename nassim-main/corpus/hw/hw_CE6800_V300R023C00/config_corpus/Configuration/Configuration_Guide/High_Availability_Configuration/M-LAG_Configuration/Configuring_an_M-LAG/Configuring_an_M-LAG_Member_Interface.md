Configuring an M-LAG Member Interface
=====================================

Configuring an M-LAG Member Interface

#### Prerequisites

The links connecting a user-side device to each of the M-LAG member devices have been configured as Eth-Trunks.


#### Context

Some service interfaces on the M-LAG master and backup devices are bundled into an M-LAG member interface, respectively. Both devices use these interfaces to establish Eth-Trunks with a user-side device, implementing cross-device link aggregation.

To improve system reliability and prevent incorrect connections during M-LAG configuration or loops, you are advised to configure the Eth-Trunks between M-LAG member devices and the user-side device to work in LACP mode. In an M-LAG in active/standby mode, the Eth-Trunks between M-LAG member devices and the user-side device need to work in manual load balancing mode.


#### Procedure

* (Recommended in dual-active mode) If the Eth-Trunks work in LACP mode, perform the following operations:
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of an Eth-Trunk interface that needs to be configured as the M-LAG member interface.
     
     
     ```
     [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id
     ```
  3. Configure the Eth-Trunk interface to work in LACP mode.
     
     
     ```
     [mode](cmdqueryname=mode) { [lacp-static](cmdqueryname=lacp-static) | [lacp-dynamic](cmdqueryname=lacp-dynamic) }
     ```
     
     By default, an Eth-Trunk interface works in manual load balancing mode.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     The dynamic LACP mode applies only to a scenario where the device is connected to a server. In other scenarios, you are advised to configure the static LACP mode. If the dynamic LACP mode is used, loops may occur on the network.
  4. Bind the user-side Eth-Trunk interface to a DFS group. This operation is equivalent to configuring the Eth-Trunk interface as an M-LAG member interface.
     
     
     ```
     [dfs-group](cmdqueryname=icssearchname) dfs-group-id [m-lag](cmdqueryname=icssearchname) m-lag-id 
     ```
     
     By default, a user-side Eth-Trunk interface is not bound to a DFS group.
     
     
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + A Layer 3 Eth-Trunk main interface cannot function as an M-LAG member interface.
     + The M-LAG member devices must be configured with the same M-LAG ID, and the configurations (including the M-LAG mode) of the interfaces configured with the same M-LAG ID must also be the same to ensure normal traffic forwarding.
  5. (Optional) Add the Eth-Trunk interface to the STP process with a specified ID.
     
     
     ```
     [stp binding process](cmdqueryname=stp+binding+process) process-id
     ```
     
     This command is applicable only to the V-STP mode. After STP multi-process is enabled, M-LAG member interfaces can be managed in different processes. As devices perform spanning tree calculation based on processes, the interfaces that are not in a certain process do not participate in the spanning tree calculation of this process. Instead, M-LAG member interfaces need to be added to specified STP processes.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + Network loops may occur if M-LAG member interfaces in different processes belong to the same broadcast domain and peer-link interfaces are blocked. To address this problem, assign M-LAG member interfaces in different processes to different broadcast domains.
     + Before switching the process of an M-LAG member interface, run the **shutdown** command to shut down the interface and do not configure services on it. After the processes of M-LAG member interfaces on the M-LAG master and backup devices are successfully switched, run the **undo shutdown** command to enable the interfaces and configure services on them.
  6. (Optional) Configure the M-LAG LACP system priority and system ID.
     
     
     1. (Optional) Exit the Eth-Trunk interface view.
        ```
        [quit](cmdqueryname=quit)
        ```
     2. Configure the M-LAG LACP system priority.
        ```
        [lacp m-lag priority](cmdqueryname=lacp+m-lag+priority) priority 
        ```
        
        By default, the M-LAG LACP system priority is 32768 in the system view, and there is no default M-LAG LACP system priority in the Eth-Trunk interface view.
     3. Configure the M-LAG LACP system ID.
        ```
        [lacp m-lag system-id](cmdqueryname=lacp+m-lag+system-id) mac-address
        ```
        
        By default, the M-LAG LACP system ID in the system view is the MAC address of the Ethernet management interface on the device, and there is no default M-LAG LACP system ID in the Eth-Trunk interface view.
        
        You are advised to use the smaller MAC address on the M-LAG master and backup devices as the M-LAG LACP system ID.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + You can configure the M-LAG LACP system priority and system ID in both the system view and Eth-Trunk interface view.
     + The M-LAG LACP system priority and system ID configured in the system view take effect on all Eth-Trunk interfaces. The M-LAG LACP system priority and system ID configured in the view of an Eth-Trunk interface take effect only on the Eth-Trunk interface.
     + If the system priority and system ID are configured only in the system view, the M-LAG master device automatically synchronizes its M-LAG LACP system priority and system ID to the M-LAG backup device when the DFS group pairing is successful. You do not need to manually configure the M-LAG LACP system priority and system ID for the backup device.
     + If the system priority and system ID are configured in both the system view and a specified Eth-Trunk interface view, the configuration in the Eth-Trunk interface view takes effect. When the DFS group pairing is successful, the M-LAG master device does not synchronize the M-LAG LACP system priority and system ID of the Eth-Trunk interface to the M-LAG backup device. Therefore, the same M-LAG LACP system priority and system ID must be configured on both the M-LAG master and backup devices.
     + The M-LAG LACP system priority and system ID are valid for an M-LAG composed of Eth-Trunks in LACP mode.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* If the Eth-Trunks work in manual load balancing mode, perform the following operations:
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of an Eth-Trunk interface that needs to be configured as the M-LAG member interface.
     
     
     ```
     [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id
     ```
  3. Bind the user-side Eth-Trunk interface to a DFS group. This operation is equivalent to configuring the Eth-Trunk interface as an M-LAG member interface.
     
     
     ```
     [dfs-group](cmdqueryname=icssearchname) dfs-group-id [m-lag](cmdqueryname=icssearchname) m-lag-id [ active-standby ]
     ```
     
     By default, a user-side Eth-Trunk interface is not bound to a DFS group.
     
     
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + A Layer 3 Eth-Trunk main interface cannot function as an M-LAG member interface.
     + The M-LAG member devices must be configured with the same M-LAG ID, and the configurations (including the M-LAG mode) of the interfaces configured with the same M-LAG ID must also be the same to ensure normal traffic forwarding.
     + If the **active-standby** parameter is not specified, the M-LAG mode is set to dual-active. If the **active-standby** parameter is specified, the M-LAG mode is set to active/standby.
     + Before configuring the M-LAG active/standby mode, run the [**m-lag active-standby election**](cmdqueryname=m-lag+active-standby+election) command in the DFS group view to configure the type of packets for electing the M-LAG master and backup member interfaces.
  4. (Optional) Add the Eth-Trunk interface to the STP process with a specified ID.
     
     
     ```
     [stp binding process](cmdqueryname=stp+binding+process) process-id
     ```
     
     This command is applicable only to the V-STP mode. After STP multi-process is enabled, M-LAG member interfaces can be managed in different processes. As devices perform spanning tree calculation based on processes, the interfaces that are not in a certain process do not participate in the spanning tree calculation of this process. Instead, M-LAG member interfaces need to be added to specified STP processes.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + Network loops may occur if M-LAG member interfaces in different processes belong to the same broadcast domain and peer-link interfaces are blocked. To address this problem, assign M-LAG member interfaces in different processes to different broadcast domains.
     + Before switching the process of an M-LAG member interface, run the **shutdown** command to shut down the interface and do not configure services on it. After the processes of M-LAG member interfaces on the M-LAG master and backup devices are successfully switched, run the **undo shutdown** command to enable the interfaces and configure services on them.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  A static MAC address can be configured for an M-LAG member interface. When the M-LAG member interface fails, the static MAC address configured on the faulty member interface still points to the member interface, and the dynamic MAC address learned by the faulty member interface is synchronized to the peer-link interface.