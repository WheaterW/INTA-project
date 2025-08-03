Binding EVPN Instances and VSIs to BDs
======================================

To implement interconnection between an enterprise campus network and a DCN, bind an EVPN instance and a VSI to the same BD created on each of PE1 and PE2.

#### Procedure

* Configure PE1 and PE2.
  1. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  2. Run [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id* **split-horizon-mode**
     
     
     
     A VNI is created and associated with the BD, and forwarding in split horizon mode is enabled.
  3. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name*
     
     
     
     A specified EVPN instance is bound to the BD.
  4. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
     
     
     
     A specified VSI is bound to the BD.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     On a node that provides interworking between VXLAN and VPLS, the BD-bound VSI does not support **pw-tag**, and the PW configured in the VSI must be in Raw mode rather than in Tag mode.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     An interworking node can have only one VSI and one EVPN instance bound to its BD. Specifically, one BD cannot be bound to multiple VSIs or EVPN instances. Additionally, multiple VSIs or EVPN instances cannot be bound to the same BD.
* Bind the AC interface to the BD on PE3.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* [ **pw-tag** *pw-tag-value* ]
     
     
     
     The BD is bound to the VSI.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BD view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
     
     
     
     A Layer 2 sub-interface is created, and its view is displayed.
  6. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The Layer 2 sub-interface is bound to the BD.
     
     
     
     The Layer 2 sub-interface and the VSI are bound to the same BD.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the interface view.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.