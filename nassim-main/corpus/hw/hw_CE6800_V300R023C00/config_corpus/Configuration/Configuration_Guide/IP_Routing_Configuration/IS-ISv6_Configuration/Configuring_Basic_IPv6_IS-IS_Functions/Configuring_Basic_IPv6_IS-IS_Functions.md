Configuring Basic IPv6 IS-IS Functions
======================================

Configuring Basic IPv6 IS-IS Functions

#### Prerequisites

Before configuring basic IPv6 IS-IS functions, you have completed the following task:

* Configure IPv6 addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an IS-IS process, and enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ] [ vpn-instance vpn-instance-name ]
   ```
   
   
   
   *process-id* specifies an IS-IS process ID. If the *process-id* parameter is not specified, the system creates process 1 by default. If a VPN instance is specified, the IS-IS process belongs to this VPN instance; otherwise, the IS-IS process belongs to a public network instance.
3. (Optional) Configure a description for the IPv6 IS-IS process.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
4. Set a NET.
   
   
   ```
   [network-entity](cmdqueryname=network-entity) net-addr
   ```
   
   Before IS-IS can start, a NET (a special form of the NSAP) must be configured for the IS-IS process in the IS-IS view.
   
   Generally, you only need to configure one NET for an IS-IS process. However, if an area needs to be redefined (for example, merged with other areas or divided into sub-areas), configure multiple NETs to ensure proper routing. As a maximum of three area addresses can be configured for an IS-IS process, you can configure a maximum of three NETs for the IS-IS process. If you need to configure multiple NETs, ensure that their system IDs are the same.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to convert loopback interface addresses into NETs to ensure that each NET is unique on the network. If NETs are not unique, route flapping can easily occur.
   
   When establishing a Level-2 neighbor relationship between two devices, IS-IS does not check whether the area addresses of the two devices are the same. If a Level-1 neighbor relationship needs to be established, the area addresses of the two devices must be the same; otherwise, the Level-1 neighbor relationship fails to be established.
5. Enable IPv6 for the IS-IS process.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable) [ topology { compatible [ enable-mt-spf ] | ipv6 | standard } ]
   ```
   
   By default, IPv6 is not enabled for an IS-IS process.
6. (Optional) Set a level for the device.
   
   
   ```
   [is-level](cmdqueryname=is-level) { level-1 | level-1-2 | level-2 }
   ```
   
   
   By default, the level of the device is Level-1-2. You are advised to set a level for the routing device based on network planning.
   * A Level-1 device can establish neighbor relationships with only Level-1 and Level-1-2 devices in the local area, and maintains only a Level-1 LSDB.
   * A Level-2 device can establish neighbor relationships with other Level-2 devices and with Level-1-2 routing devices in other areas and maintains only a Level-2 LSDB.
   * A routing device capable of establishing neighbor relationships with both Level-1 and Level-2 routing devices is known as a Level-1-2 routing device. Such a device can establish Level-1 neighbor relationships with Level-1 and other Level-1-2 routing devices in the local area, and can also establish Level-2 neighbor relationships with Level-2 and Level-1-2 routing devices in other areas. Each Level-1 routing device can be connected to another area only through a Level-1-2 routing device. Each Level-1-2 routing device maintains a Level-1 LSDB (for intra-area routing) and a Level-2 LSDB (for inter-area routing).![](public_sys-resources/note_3.0-en-us.png) 
     
     If the level of an IS-IS routing device is changed during network operation, the current IS-IS process may be restarted and the IS-IS neighbor relationship may be disconnected. To prevent these issues, you are recommended to change the level only when configuring IS-IS.
     
     Keep the default level (Level-1-2) of the device if you want to change the level of its interfaces. If you set Level-1 or Level-2 for the device, its interfaces can establish only the corresponding level of neighbor relationships with others.
7. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
9. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
10. Enable IPv6 IS-IS on the interface.
    
    
    ```
    [isis ipv6 enable](cmdqueryname=isis+ipv6+enable) [ process-id ]
    ```
11. (Optional) Set a level for the interface.
    
    
    ```
    [isis circuit-level](cmdqueryname=isis+circuit-level) [ level-1 | level-1-2 | level-2 ]
    ```
    
    By default, the level of an interface is Level-1-2.
    
    By default, both Level-1 and Level-2 neighbor relationships will be established between two Level-1-2 devices. To allow two Level-1-2 devices to establish only a Level-1 or Level-2 neighbor relationship, change the interface level at both ends as required.
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display isis peer**](cmdqueryname=display+isis+peer) [ **verbose** ] [ *process-id* | **vpn-instance** *vpn-instance-name* | **interface** *interface-type* *interface-number* ] [ **peer-system-id** *system-id* ] command to check IPv6 IS-IS neighbor information.
* Run the [**display isis interface**](cmdqueryname=display+isis+interface) [ **verbose** ] [ **vpn-instance** *vpn-instance-name* ] command to check information about IPv6 IS-IS interfaces.
* Run the [**display isis**](cmdqueryname=display+isis) *process-id* **route** **ipv6** [ *ipv6-address* [ *prefix-length* ] | { **level-1** | **level-2** } | **verbose** ] \* command to check IPv6 IS-IS routing information.