(Optional) Configuring an MPLS MTU for an Interface
===================================================

If an MPLS MTU needs to be configured for an interface, the related configuration needs to be performed on all nodes.

#### Context

LDP selects the minimum value among MTUs on all outbound interfaces of an LSP. On the ingress, MPLS uses the minimum MTU to determine the maximum size of each MPLS packet that can be forwarded without being fragmented. The MPLS MTU helps prevent forwarding failures on transit nodes.

The relationships between the MPLS MTU and interface MTU are as follows:

* If the MPLS MTU is not configured on an interface, the interface MTU is used.
* If both an MPLS MTU and an interface MTU are set on an interface, the smaller value between them is used.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The MPLS MTU of an interface can take effect only after the MTU signaling function is enabled.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of an MPLS-enabled interface is displayed.
3. Run [**mpls mtu**](cmdqueryname=mpls+mtu) *mtu*
   
   
   
   An MPLS MTU is set for an interface.
4. (Optional) Run [**interface-mtu check-mode**](cmdqueryname=interface-mtu+check-mode+ip+label-contained-length) { **ip** | **label-contained-length** } **slot** *slot-id* An interface MTU check mode is configured.
   
   Choose an MTU check mode based on scenarios:
   * **ip**: applies to IP forwarding scenarios.
   * **label-contained-length**: applies to MPLS forwarding scenarios.
   
   The device checks a packet's size based on the configured check mode and fragments a packet if its size exceeds the interface MTU.
   
   In VS mode, this command is supported only by the admin VS.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.