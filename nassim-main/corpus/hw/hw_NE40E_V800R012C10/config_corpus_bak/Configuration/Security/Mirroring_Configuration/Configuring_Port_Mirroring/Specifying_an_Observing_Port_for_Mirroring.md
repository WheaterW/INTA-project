Specifying an Observing Port for Mirroring
==========================================

This section describes how to specify an observing port for mirroring. You can then associate this port with the corresponding mirrored port.

#### Context

You can use either of the following methods to specify an observing port for mirroring:

* Specify an observing port for board-based mirroring.With this method, the mirrored traffic of the entire interface board on the NE40E is sent only to the same observing port.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The observing port specified for board-based mirroring can be configured on either the local or non-local interface board.
  
  The mirroring instance mode supports only board-based mirroring.

* Specify an observing port for interface-based mirroring.
  
  With this method, the mirrored traffic of an interface on the NE40E is sent to the specified observing port.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Packets on an interface can be mirrored to an observing port on any interface board. This means that the observing port can reside on the same interface board as the mirrored port or reside on another interface board. In scenarios where observing ports are specified for both interface-based mirroring and board-based mirroring, if the observing port specified for interface-based mirroring is up, this port takes effect. However, if this port is down, the observing port specified for board-based mirroring takes effect.

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

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
   
   
   
   Specify an observing port for board-based mirroring or interface-based mirroring as required.
   
   
   
   1. Specify an observing port for board-based mirroring.
      
      
      * Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the slot view.
      * Run the [**mirror to observe-index**](cmdqueryname=mirror+to+observe-index) *observe-index* command to specify an observing port for board-based mirroring.
   2. Specify an observing port for interface-based mirroring.
      
      
      * Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
      * Run the [**port-mirroring to**](cmdqueryname=port-mirroring+to) **observe-index** *observe-index* command to specify an observing port for the upstream and downstream packets of the mirrored port.
      * Run the [**port-mirroring to**](cmdqueryname=port-mirroring+to) **observe-index** *observe-index* &<2-8> [ **inbound | outbound** ] command to specify multiple observing ports for the upstream or downstream packets of the mirrored port.
      * Run the [**port-mirroring to**](cmdqueryname=port-mirroring+to) **null0** command to specify the observing port null0 for the upstream and downstream packets of the mirrored port.
      * Run the [**port-mirroring to**](cmdqueryname=port-mirroring+to) **observe-index** *observe-index* { **inbound | outbound** } command to specify an observing port for the upstream or downstream packets of the mirrored port.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The upstream and downstream packets of the mirrored port can be mirrored to either the same observing port or different observing ports. If observing ports for upstream and downstream packets are not both specified, the observing port specified for board-based mirroring is used for the packets whose observing port is not specified.
2. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.