Configuring a VXLAN Service Access Point
========================================

Configuring a VXLAN Service Access Point

#### Prerequisites

If the simplified mode is used for configuration, complete [Configuring a BD Profile in Simplified Mode](../vrp/dc_vrp_vxlan_cfg_bdprofile01.html).


#### Context

A Layer 2 sub-interface used as a service access point can have different encapsulation types configured to transmit various types of data packets. This type of sub-interface can transmit data packets through a BD after it is associated with the BD. [Table 1](#EN-US_TASK_0000001176743947__en-us_task_0139427606_tab_1) describes the encapsulation types.

**Table 1** Traffic encapsulation types
| Traffic Encapsulation Type | Description |
| --- | --- |
| **dot1q** | In Layer 2 forwarding scenarios, this type of sub-interface can accept packets with multiple VLAN tags. In Layer 3 forwarding scenarios, this type of sub-interface can accept only double-tagged packets for the following: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K; it can accept only double- and triple-tagged packets for the following: CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, CE6863E-48S8CQ.  If such a sub-interface receives single-tagged VLAN packets, it accepts only those packets whose VLAN tag matches the specified VLAN tag. If the sub-interface receives VLAN packets with double or more VLAN tags, it accepts only those packets whose outer VLAN tag matches the specified VLAN tag.   * When performing VXLAN encapsulation on original packets, the sub-interface removes the outmost VLAN tags of these packets if it is not configured with dot1q transparent transmission and retains the inner and outer VLAN tags of these packets if it is configured with dot1q transparent transmission. * When performing VXLAN decapsulation on packets, the sub-interface adds specified VLAN tags to these packets if it is not configured with dot1q transparent transmission and retains the VLAN tags of these packets if it is configured with dot1q transparent transmission.  When setting the encapsulation type to **dot1q**, note the following:  * The VLAN ID encapsulated by a Layer 2 sub-interface cannot be the same as that permitted by the Layer 2 main interface of the sub-interface. * The VLAN IDs encapsulated by a Layer 2 sub-interface and a Layer 3 sub-interface cannot be the same. * The VLAN ID ranges specified for different dot1q Layer 2 sub-interfaces of the same main interface cannot overlap.   NOTE:  Dot1q sub-interfaces bound to the same BD must have the same traffic behavior type. On the same VXLAN network, the traffic behavior types of dot1q sub-interfaces in the same BD but on different devices must also be the same. |
| **untag** | This type of sub-interface accepts only packets that do not carry VLAN tags.   * When performing VXLAN encapsulation on original packets, the sub-interface does not add any VLAN tags to them. * When performing VXLAN decapsulation on packets, the sub-interface removes the VLAN tags before forwarding the packets if the inner packets carry one or two VLAN tags and transparently transmits the packets if the packets carry more than two VLAN tags.  When setting the encapsulation type to **untag**, note the following:  * Ensure that the corresponding physical interface of the Layer 2 sub-interface does not have any configuration, and that it is removed from the default VLAN. * Untagged Layer 2 sub-interfaces can be created only on Layer 2 physical interfaces and Eth-Trunk interfaces. * Only one untagged Layer 2 sub-interface can be created on a main interface. * After an untagged sub-interface is bound to a BD, a dot1q transparent transmission sub-interface (with the [**rewrite no-action**](cmdqueryname=rewrite+no-action) command configuration) or QinQ transparent transmission sub-interface (without the [**rewrite pop double**](cmdqueryname=rewrite+pop+double) command configuration) can no longer be bound to the BD. Similarly, if such a dot1q or QinQ sub-interface is bound to a BD, an untagged sub-interface can no longer be bound to the BD. |
| **qinq** | In Layer 2 forwarding scenarios, this type of sub-interface can accept packets with multiple VLAN tags. In Layer 3 forwarding scenarios, this type of sub-interface can accept only double-tagged packets for the following: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K; it can accept only double- and triple-tagged packets for the following: CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, CE6863E-48S8CQ.   * When performing VXLAN encapsulation on original packets, the sub-interface retains all VLAN tags of the packets if it is configured with QinQ transparent transmission and removes the outermost two VLAN tags if it is not configured with QinQ transparent transmission. * When performing VXLAN decapsulation on packets, the sub-interface directly forwards the packets without changing the VLAN tags if it is configured with QinQ transparent transmission and adds specified double VLAN tags to the packets before forwarding them if it is not configured with QinQ transparent transmission.  When a Layer 2 sub-interface configured with the encapsulation type of **default**, dot1q transparent transmission (with the [**rewrite no-action**](cmdqueryname=rewrite+no-action) command configuration), or QinQ transparent transmission (without the [**rewrite pop double**](cmdqueryname=rewrite+pop+double) command configuration) is bound to a BD, this BD does not support VBDIF interfaces or ARP broadcast suppression. NOTE:  QinQ sub-interfaces bound to the same BD must have the same traffic behavior type. On the same VXLAN network, the traffic behavior types of QinQ sub-interfaces in the same BD but on different devices must also be the same.   The outer VLAN ID encapsulated for a QinQ Layer 2 sub-interface cannot be the same as the default VLAN ID or that allowed by the corresponding Layer 2 main interface. |
| **default** | This type of sub-interface accepts all packets, regardless of whether they carry VLAN tags.  For VXLAN packet encapsulation or decapsulation, this type of sub-interface does not perform any VLAN tag-related action (tag addition, replacement, or removal) on the original packets. The **default** traffic encapsulation type has the following restrictions:  * The main interface where the involved sub-interface resides cannot be added to any VLAN. * Only Layer 2 physical interfaces and Eth-Trunk interfaces can have **default** Layer 2 sub-interfaces created. * Only one default Layer 2 sub-interface can be created on a main interface. After a default Layer 2 sub-interface is created, other types of Layer 2 sub-interfaces cannot be created on the interface. |


![](../public_sys-resources/note_3.0-en-us.png) 

When receiving a double-tagged VLAN packet, a device preferentially selects a QinQ sub-interface to process the packet. If no QinQ sub-interface matches the packet, the device selects a dot1q sub-interface. For example, assume that both a QinQ sub-interface and a dot1q sub-interface are configured, VLAN ID 10 is configured for the dot1q sub-interface, and VLAN IDs 10 and 20 are configured as the outer VLAN ID and inner VLAN ID, respectively, for the QinQ sub-interface. In this case, if a packet with the outer VLAN ID 10 and inner VLAN ID 20 is received, the QinQ sub-interface is preferentially selected to process the packet. If a packet with the outer VLAN ID 10 and an inner VLAN other than 20 is received, the dot1q sub-interface is selected to process the packet.

[Table 2](#EN-US_TASK_0000001176743947__table5290164311710) and [Table 3](#EN-US_TASK_0000001176743947__table11150163212192) describe the mutual exclusiveness between two Layer 2 sub-interfaces to be bound to the same BD.

* N: The two Layer 2 sub-interfaces cannot be bound to the same BD.
* Y: The two Layer 2 sub-interfaces can be bound to the same BD.

**Table 2** Mutual exclusiveness between two Layer 2 sub-interfaces belonging to the same interface and to be bound to the same BD
| Layer 2 Sub-interface Type | Default | Untagged | Dot1q VLAN Tag Termination | Dot1q Transparent Transmission | QinQ VLAN Tag Termination | QinQ Transparent Transmission |
| --- | --- | --- | --- | --- | --- | --- |
| Default | N | N | N | N | N | N |
| Untagged | N | N | Y | N | Y | N |
| Dot1q VLAN Tag Termination | N | Y | Y | N | Y | N |
| Dot1q Transparent Transmission | N | N | N | N | N | Y |
| QinQ VLAN Tag Termination | N | Y | Y | N | Y | N |
| QinQ Transparent Transmission | N | N | N | Y | N | Y |


**Table 3** Mutual exclusiveness between two Layer 2 sub-interfaces belonging to different interfaces and to be bound to the same BD
| Layer 2 Sub-interface Type | Default | Untagged | Dot1q VLAN Tag Termination | Dot1q Transparent Transmission | QinQ VLAN Tag Termination | QinQ Transparent Transmission |
| --- | --- | --- | --- | --- | --- | --- |
| Default | Y | Y | Y | Y | N | N |
| Untagged | Y | Y | Y | N | Y | N |
| Dot1q VLAN Tag Termination | Y | Y | Y | N | Y | N |
| Dot1q Transparent Transmission | Y | N | N | Y | N | Y |
| QinQ VLAN Tag Termination | N | Y | Y | N | Y | N |
| QinQ Transparent Transmission | N | N | N | Y | N | Y |

If one or more VLANs are used for service access, you can bind these VLANs to a BD to enable transmission of data packets through the BD.

A service access point needs to be configured on a Layer 2 gateway.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enable underlay network-based load balancing for VXLAN BUM packets. (Supported only by the CE6863H, CE6863H-K, CE6881H, and CE6881H-K.)
   
   
   ```
   [assign forward nvo3 bum ecmp hash enable](cmdqueryname=assign+forward+nvo3+bum+ecmp+hash+enable)
   ```
   
   By default, VXLAN BUM packets cannot be balanced based on the underlay network.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * BUM traffic load balancing over VXLAN tunnels cannot be used together with IGMP snooping over VXLAN or IPv4 Layer 3 multicast over VXLAN. That is, the [**assign forward nvo3 bum ecmp hash enable**](cmdqueryname=assign+forward+nvo3+bum+ecmp+hash+enable) command is mutually exclusive with the [**igmp snooping enable**](cmdqueryname=igmp+snooping+enable) command in the system view and the [**igmp enable**](cmdqueryname=igmp+enable) command in the VBDIF interface view.
   * For the CE6863H, CE6863H-K, CE6881H-K, and CE6881H, the [**assign forward nvo3 bum ecmp hash enable**](cmdqueryname=assign+forward+nvo3+bum+ecmp+hash+enable) command is mutually exclusive with the **[**local-preference enhanced**](cmdqueryname=local-preference+enhanced)** command in the ECMP load balancing view.
3. Create a BD and enter its view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
   
   By default, no BD is created.
4. (Optional) Configure a description for the BD.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   
   By default, no description is configured for a BD.
5. Configure a service access point.
   
   
   * Configure a Layer 2 sub-interface as a service access point.
     1. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
        ```
     2. (Optional) Configure VXLAN access through Layer 2 sub-interfaces on an STP network.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        [loop-protect l2-subinterface enable](cmdqueryname=loop-protect+l2-subinterface+enable)
        [quit](cmdqueryname=quit)
        ```
        
        When Layer 2 sub-interfaces on a legacy STP network are used for VXLAN access, loops may occur on the STP network. To prevent loops, run the [**loop-protect l2-subinterface enable**](cmdqueryname=loop-protect+l2-subinterface+enable) command on the main interface where Layer 2 sub-interfaces reside. This enables Layer 2 sub-interfaces to inherit the blocked/forwarding status of the main interface.
        
        ![](../public_sys-resources/note_3.0-en-us.png) 
        
        Before running the **loop-protect l2-subinterface enable** command, configure STP on the main interface.
     3. Create a Layer 2 sub-interface and enter its view.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number.subnum mode l2
        ```
        
        By default, no Layer 2 sub-interface is created.
        
        ![](../public_sys-resources/note_3.0-en-us.png) 
        
        Before running this command, ensure that the Layer 2 main interface on which a Layer 2 sub-interface is to be created does not have the [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel** command configuration. If this configuration exists, run the [**undo port link-type**](cmdqueryname=undo+port+link-type) command to delete the configuration.
     4. Configure an encapsulation type to determine the type of data packet that can pass through the Layer 2 sub-interface.
        
        Dot1q type:
        
        ```
        [encapsulation](cmdqueryname=encapsulation) dot1q [ vid pe-vid ]
        ```
        
        QinQ type:
        
        ```
        [encapsulation](cmdqueryname=encapsulation) qinq [ vid pe-vid ce-vid ce-vid ]
        ```
        
        Untagged type:
        
        ```
        [encapsulation](cmdqueryname=encapsulation) untag
        ```
        
        Default type:
        
        ```
        [encapsulation](cmdqueryname=encapsulation) default
        ```
        
        By default, no encapsulation type is configured.
        
        ![](../public_sys-resources/note_3.0-en-us.png) 
        
        You are advised to configure the same traffic encapsulation type on the endpoint devices of a tunnel.
     5. (Optional) Configure a dot1q sub-interface to transparently transmit received packets.
        ```
        [rewrite no-action](cmdqueryname=rewrite+no-action)
        ```
        
        By default, a Layer 2 dot1q sub-interface removes VLAN tags from received packets, instead of transparently transmitting them.
     6. (Optional) Configure a dot1q sub-interface to change the VLAN tags to be added in the decapsulation process.
        ```
        [rewrite egress vid](cmdqueryname=rewrite+egress+vid) vlan-id
        ```
        
        By default, when packets are decapsulated on a Layer 2 sub-interface that uses dot1q encapsulation, the VLAN tag to be added is the same as the VLAN tag to be removed when packets are encapsulated. You can run this command to change the VLAN tag to be added in the decapsulation process, so that packets sent and received by the Layer 2 sub-interface use different VLAN tags.
        
        ![](../public_sys-resources/note_3.0-en-us.png) 
        
        This command can be run only on Layer 2 dot1q VLAN tag termination sub-interfaces. It cannot be run on Layer 2 dot1q transparent transmission sub-interfaces (with the [**rewrite no-action**](cmdqueryname=rewrite+no-action) command configuration).
        
        The value of **vid** in this command must be different from **vid** specified in the [**encapsulation**](cmdqueryname=encapsulation) **dot1q** **vid** *pe-vid* command.
     7. (Optional) Configure a QinQ sub-interface to remove double VLAN tags from received packets.
        ```
        [rewrite pop double](cmdqueryname=rewrite+pop+double)
        ```
        
        By default, a Layer 2 QinQ sub-interface does not remove double VLAN tags from received packets, and transparently transmits the packets without any modification.
        
        This step is mandatory if the current access point needs to forward Layer 3 service traffic.
     8. Add a Layer 2 sub-interface to a BD so that the sub-interface can transmit data packets through this BD.
        ```
        [bridge-domain](cmdqueryname=bridge-domain) bd-id
        ```
        
        By default, a Layer 2 sub-interface is not added to any BD.
   * Configure a VLAN as a service access point.
     1. Enter the view of a created BD.
        ```
        [bridge-domain](cmdqueryname=bridge-domain) bd-id
        ```
     2. (Optional) Bind the BD to a BD profile.
        ```
        [binding bridge-domain profile](cmdqueryname=binding+bridge-domain+profile) profileId
        ```
        
        Perform this step when the simplified mode is used for configuration. The BD is then automatically bound to a VLAN, and you do not need to perform Step c.
     3. Bind one or more VLANs to the BD.
        ```
        [l2 binding vlan](cmdqueryname=l2+binding+vlan) vlan-id
        ```
        
        By default, VLANs are not bound to any BD.
   * Configure VLANs as service access points in batches.
     1. Enter the BD range view.
        ```
        [bridge-domain range](cmdqueryname=bridge-domain+range) { bdIdBgn [ to bdIdEnd ] } &<1-10>
        ```
     2. Bind the BD range to a BD profile.
        ```
        [binding bridge-domain profile](cmdqueryname=binding+bridge-domain+profile) profileId
        ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```