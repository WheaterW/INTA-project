Configuring VPLS E-Tree
=======================

In a VPLS domain, you can configure VPLS E-Tree to control communication between AC-side users.

#### Prerequisites

Before configuring VPLS E-Tree, complete the following tasks:

* Set data link layer protocol parameters and IP addresses for interfaces to ensure that the data link layer protocol status on each interface is up.
* Configure LDP VPLS.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section applies only to the M2K and M2K-B models.

In a VPLS domain, AC interfaces bound to the same VSI can communicate with one another. It is necessary to enhance user data security and minimize mutual influence between users by controlling communication between AC interfaces.

VPLS E-Tree provides a method to isolate AC interfaces on different devices by setting the AC interface attribute to root or leaf.

* Root AC interface: can communicate with leaf AC interfaces and other root AC interfaces.
* Leaf AC interface: can communicate only with root AC interfaces.


#### Procedure

* Configure static VPLS E-Tree.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ]
     
     
     
     The view of the created VSI is displayed.
  3. Run [**e-tree**](cmdqueryname=e-tree) **static**
     
     
     
     E-Tree is enabled for VPLS, and the E-Tree view is displayed.
  4. Run [**root-vlan**](cmdqueryname=root-vlan) *root-vlan* **leaf-vlan** *leaf-vlan*
     
     
     
     The root VLAN and leaf VLAN for E-Tree are configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In the same VPLS domain, VSIs on all PEs must use the same root VLAN and leaf VLAN. Otherwise, traffic cannot be isolated.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit from the E-Tree view.
  6. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
     
     
     
     LDP is configured as the signaling type for the VSI.
  7. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
     
     
     
     An ID is configured for the VSI.
  8. Run [**peer**](cmdqueryname=peer) *peer-address*
     
     
     
     A peer is configured for the VSI.
  9. (Optional) Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name*
     
     
     
     The VSI-LDP-PW view is displayed.
  10. (Optional) Run [**e-tree mode**](cmdqueryname=e-tree+mode) { **compatible** | **optimized** }
      
      
      
      Static VPLS E-Tree in compatible or optimization mode is configured.
  11. (Optional) Run [**e-tree leaf**](cmdqueryname=e-tree+leaf)
      
      
      
      The PW attribute is set to leaf.
      
      
      
      [**e-tree leaf**](cmdqueryname=e-tree+leaf) can be configured only when the PW is in compatible mode. If the peer device of a PW does not support E-Tree services, the local PE does not send packets received from the peer PE to the AC interface with the local leaf attribute.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If only static VPLS E-Tree in common mode is configured, steps 9, 10, and 11 are not required.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure AC interface attributes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The user-side interface view is displayed.
  3. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
     
     
     
     The Layer 2 interface is bound to the VSI.
  4. (Optional) Run [**l2 binding e-tree leaf**](cmdqueryname=l2+binding+e-tree+leaf)
     
     
     
     The AC interface is configured as a leaf interface. By default, the attribute of an AC interface is root. After an AC interface is configured as a leaf interface, the AC interface can only communicate with the root interface, but cannot communicate with other leaf interfaces.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring VPLS E-Tree, verify the configuration.

* Run the [**display vsi e-tree**](cmdqueryname=display+vsi+e-tree) command to check information about all VSIs with E-Tree enabled.