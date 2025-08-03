ARP Entry Limit
===============

After Address Resolution Protocol (ARP) entry limit is enabled, the device limits the number of ARP entries that an interface can learn, to prevent ARP entry overflow and improve ARP entry security.

#### Background Information

If a device receives excessive ARP packets in a short period, the device's buffer will overflow, interrupting services of authorized users. This problem can be solved by configuring an ARP entry limit on the device. After ARP entry limit is configured, the device limits the number of ARP entries that each interface can learn, preventing ARP entry overflow and improving ARP entry security.

* Ethernet, GE, and Eth-Trunk interfaces can be Layer 2 or Layer 3 interfaces. *vlan-id* cannot be configured for Layer 3 interfaces, but must be configured for Layer 2 interfaces.
* Ethernet, GE, and Eth-Trunk sub-interfaces can be common sub-interfaces or QinQ sub-interfaces. When the sub-interface is a common sub-interface, *vlan-id* cannot be configured. When the sub-interface is a QinQ sub-interface, *vlan-id* must be configured. In this case, *vlan-id* specifies the outer VLAN ID of the QinQ sub-interface.

#### Procedure

* Configure ARP entry limit for a physical interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The physical interface view is displayed.
  3. Run [**arp-limit**](cmdqueryname=arp-limit) **vlan** *vlan-id1* [ **to** *vlan-id2* ] **maximum** *limitnum*
     
     
     
     ARP entry limit is configured for the physical interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure ARP entry limit for a VLANIF interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **vlanif** *interface-number*
     
     
     
     The VLANIF interface view is displayed.
  3. Run [**arp-limit**](cmdqueryname=arp-limit) **maximum** *limitnum*
     
     
     
     ARP entry limit is configured for the VLANIF interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure ARP entry limit for a sub-interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [.*subnumber* ]
     
     
     
     The sub-interface view is displayed.
  3. Run [**arp-limit**](cmdqueryname=arp-limit) **vlan** *vlan-id1* [ **to** *vlan-id2* ] **maximum** *limitnum*
     
     
     
     ARP entry limit is configured for the sub-interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.