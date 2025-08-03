Configuring a Mirrored Port
===========================

To analyze the traffic sent or received by an interface, you can configure this interface as a mirrored port.

#### Context

Local mirroring can be implemented in both common mode and mirroring instance mode. The characteristics of the two modes are as follows:

* The common mode supports interface-based mirroring, whereas the mirroring instance mode supports board-based mirroring.
* Both modes allow you to limit the rate of mirrored traffic. In common mode, the rate limit needs to be configured on a specified interface. In mirroring instance mode, a shared CAR can be configured for a specified mirroring instance and then applied to different interfaces bound to the mirroring instance. As such, the mirroring instance mode offers simpler configuration and higher forwarding performance.
* The mirroring instance mode supports instance sharing, so that multiple interfaces can share the same mirroring instance. This enables more interfaces to support port mirroring in scenarios with limited mirroring specifications.

**Table 1** Interfaces supporting local mirroring
| Interface Type | Mirrored Port | Observing Port |
| --- | --- | --- |
| Layer 3 Ethernet main interfaces (including Eth-Trunk interfaces) | Supported | Supported |
| BAS interfaces | Supported  NOTE:  A VE interface functioning as a BAS interface only supports local flow mirroring in loopback scenarios. | Not supported |
| Ethernet sub-interfaces (including Eth-Trunk sub-interfaces) | Supported NOTE:  A sub-interface supports the mirroring function even when configured as a dot1q, EVC, BAS, dot1q VLAN tag termination, or QinQ VLAN tag termination sub-interface. | Supported  NOTE:  A sub-interface functioning as a BAS, dot1q VLAN tag termination or QinQ VLAN tag termination sub-interface does not support observing port configuration.  An EVC sub-interface can be configured as an observing port only when it adopts the untag or dot1q encapsulation mode.  If an Eth-Trunk interface is configured as an observing port, downstream mirroring is performed, and packets are mirrored from their Layer 3 headers, the mirroring starts from the first member interface. Other traffic is mirrored among member interfaces in load balancing mode, which depends on the configured load balancing mode and hash factors. |
| POS interfaces | Supported | Supported |
| IP-Trunk interfaces | Supported | Supported |
| Serial interfaces | Supported | Not supported |
| ATM main interfaces | Supported | Not supported |
| ATM sub-interfaces | Supported | Not supported |
| MP-Group interfaces | Supported | Not supported |



#### Procedure

* Mirroring in common mode
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**observe user-defined-filter**](cmdqueryname=observe+user-defined-filter) *id* { **offset** *offset-value* **value** *value* *value-mask* } &<1-4>
     
     
     
     A user-defined any-byte matching rule is configured for mirrored packets.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  4. According to observation requirements, run the corresponding command for configuration.
     
     
     + Run the [**port-mirroring**](cmdqueryname=port-mirroring) { **inbound** [ **cpu-packet** ] | **outbound** } [ **user-defined-filter** *user-defined-filter-id* ] command to configure the mirroring function on the interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If **cpu-packet** is specified, only the packets sent from the interface to the CPU are mirrored.
     + Run the [**port-mirroring**](cmdqueryname=port-mirroring) { **inbound** | **outbound** } **vlan** *vlan-id1* [ **to** *vlan-id2* ] command to configure VLAN-based mirroring.
     + Run the [**port-mirroring**](cmdqueryname=port-mirroring) { **inbound** | **outbound** } **pe-vid** *low-vid* [ **to** *high-vid* ] **ce-vid** *ce-vlan-id-begin* [ **to** *ce-vlan-id-end* ] command to configure mirroring based on the ranges of inner and outer VLAN IDs.
  5. (Optional) Run [**port-mirroring without-linklayer-header**](cmdqueryname=port-mirroring+without-linklayer-header)
     
     
     
     The mirrored port is configured to mirror packets from their Layer 3 headers.
     
     
     
     If this command is run on the mirrored port, the [**port-observing observe-index**](cmdqueryname=port-observing+observe-index) *observe-index* **without-filter** command needs to be run on the corresponding observing port.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Mirroring in mirroring instance mode
  1. To configure mirroring in mirroring instance mode for an EVC Layer 2 sub-interface, perform the following operations:
     
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**mirror instance**](cmdqueryname=mirror+instance) *instance-name* **location**
        
        A mirroring instance is created.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number**.subnum* **mode** **l2**
        
        The EVC Layer 2 sub-interface view is displayed.
     5. According to the traffic encapsulation type of the EVC Layer 2 sub-interface, run the corresponding command to observe the traffic of the sub-interface:
        + If the traffic encapsulation type is QinQ, run the [**port-mirroring instance**](cmdqueryname=port-mirroring+instance) *instance-name* { **inbound** | **outbound** } **pe-vid** *pe-vlan-id* **ce-vid** *ce-vlan-id-begin* [ **to** *ce-vlan-id-end* ] **identifier** { **none** | **pe-vid** | **ce-vid** | **pe-ce-vid** } [ **group** *group-name* ] command.
        + If the traffic encapsulation type is dot1q, run the [**port-mirroring instance**](cmdqueryname=port-mirroring+instance) *instance-name* { **inbound** | **outbound** } **vid** *vlan-id-begin* [ **to** *vlan-id-end* ] **identifier** { **none** | **vid** } [ **group** *group-name* ] command.
        + If the traffic encapsulation type is Untag or Default, run the [**port-mirroring instance**](cmdqueryname=port-mirroring+instance) *instance-name* { **inbound** | **outbound** } [ **group** *group-name* ] command.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  2. To configure mirroring in mirroring instance mode for a BD, perform the following operations:
     
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**mirror instance**](cmdqueryname=mirror+instance) *instance-name* **location**
        
        A mirroring instance is created.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     4. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
        
        The BD view is displayed.
     5. Run [**port-mirroring instance**](cmdqueryname=port-mirroring+instance) *instance-name* { **inbound** | **outbound** } [ **group** *group-name* ]
        
        The traffic in the BD is observed.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.