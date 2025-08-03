Configuring Basic IS-IS Functions
=================================

Configuring Basic IS-IS Functions

#### Prerequisites

Before configuring basic IS-IS functions, you have completed the following task:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.

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
3. (Optional) Configure a description for the IS-IS process.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
4. Set a NET.
   
   
   ```
   [network-entity](cmdqueryname=network-entity) net-addr
   ```
   
   Before IS-IS can start, a NET (the special form of the NSAP) must be configured for the IS-IS process in the IS-IS view.
   
   The value of *net-addr* is in the format of X... X.XXXX.XXXX.XXXX.00, where X... X indicates an area address, the 12 Xs in the middle indicate the system ID, and 00 indicates the SEL.
   
   In normal cases, you only need to configure one NET for an IS-IS process. However, if an area needs to be redefined (for example, the area needs to be merged with other areas or divided into sub-areas), configure multiple NETs to ensure proper routing. A maximum of three area addresses can be configured for an IS-IS process, and therefore, you can configure a maximum of three NETs for the IS-IS process. If you need to configure multiple NETs, ensure that their system IDs are the same.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to convert loopback interface addresses into NETs to ensure that each NET is unique on the network. If NETs are not unique, route flapping can easily occur.
   
   When establishing a Level-2 neighbor relationship between two routing devices, IS-IS does not check whether their area addresses are the same. If a Level-1 neighbor relationship needs to be established, the area addresses of the two routing devices must be the same; otherwise, the Level-1 neighbor relationship fails to be established.
5. (Optional) Set a level for the routing device.
   
   
   ```
   [is-level](cmdqueryname=is-level) { level-1 | level-1-2 | level-2 }
   ```
   
   
   
   By default, the level of the routing device is Level-1-2.
   
   You are advised to configure a level for the routing device based on network planning.
   * A Level-1 routing device can establish neighbor relationships with only Level-1 and Level-1-2 routing devices in the local area and maintains only a Level-1 LSDB.
   * A Level-2 routing device can establish neighbor relationships with other Level-2 routing devices and with Level-1-2 routing devices in other areas and maintains only a Level-2 LSDB.
   * A routing device capable of establishing neighbor relationships with both Level-1 and Level-2 routing devices is known as a Level-1-2 routing device. This type of routing device can establish Level-1 neighbor relationships with Level-1 and other Level-1-2 routing devices in the local area, and can also establish Level-2 neighbor relationships with Level-2 and Level-1-2 routing devices in other areas. Each Level-1 routing device can only be connected to another area through a Level-1-2 routing device. Each Level-1-2 routing device maintains a Level-1 LSDB (for intra-area routing) and a Level-2 LSDB (for inter-area routing).![](public_sys-resources/note_3.0-en-us.png) 
     
     If the level of an IS-IS routing device is changed during network operation, the current IS-IS process may be restarted and the IS-IS neighbor relationship may be disconnected. To prevent these problems, you are recommended to change the level only when configuring IS-IS.
     
     Changing the level of an IS-IS interface only takes effect on a Level-1-2 IS-IS routing device. Otherwise, the level of the routing device determines the level of the neighbor relationship that can be established.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
8. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
9. Enable IS-IS on the interface.
   
   
   ```
   [isis enable](cmdqueryname=isis+enable) [ process-id ]
   ```
10. (Optional) Set a level for the interface.
    
    
    ```
    [isis circuit-level](cmdqueryname=isis+circuit-level) [ level-1 | level-1-2 | level-2 ]
    ```
    
    
    
    By default, the level of an interface is Level-1-2.
    
    By default, both Level-1 and Level-2 neighbor relationships will be established between two Level-1-2 routing devices. To allow two Level-1-2 routing devices to establish only a Level-1 or Level-2 neighbor relationship, change the interface level at both ends as required.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display isis peer**](cmdqueryname=display+isis+peer) [ **verbose** ] [ *process-id* | **vpn-instance** *vpn-instance-name* | **interface** *interface-type* *interface-number* ] [ **peer-system-id** *system-id* ] command to check IS-IS neighbor information.
* Run the [**display isis interface**](cmdqueryname=display+isis+interface) [ **verbose** ] [ **vpn-instance** *vpn-instance-name* ] command to check information about IS-IS interfaces.
* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] command to check IS-IS routing information.