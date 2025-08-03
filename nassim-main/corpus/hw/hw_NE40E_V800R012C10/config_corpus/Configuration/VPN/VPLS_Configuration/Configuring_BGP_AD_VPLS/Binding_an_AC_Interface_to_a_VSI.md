Binding an AC Interface to a VSI
================================

The view in which an AC interface is bound to a VSI depends on the type of link between the PE and CE.

#### Context

Depending on the type of link between a PE and a CE, the binding scenarios are as follows:

* Binding an Ethernet interface to a VSI: applies to scenarios where a PE uses a GE interface to connect to a CE.
* Binding an Ethernet sub-interface to a VSI: applies to scenarios where a PE uses a GE sub-interface to connect to a CE.
* Binding a VLANIF interface to a VSI: applies to scenarios where a PE uses a VLANIF interface to connect to a CE.
* Binding an L2VE sub-interface to a VSI: applies to scenarios where a PE uses an L2VE sub-interface to connect to a CE.
* Binding an Eth-Trunk interface to a VSI: applies to scenarios where a PE uses an Eth-Trunk interface to connect to a CE.
* Binding an Eth-Trunk sub-interface to a VSI: applies to scenarios where a PE uses an Eth-Trunk sub-interface to connect to a CE.
* Binding a dot1q VLAN tag termination sub-interface to a VSI: applies to scenarios where a PE uses a dot1q VLAN tag termination sub-interface to connect to a CE.
* Binding a QinQ VLAN tag termination sub-interface to a VSI: applies to scenarios where a PE uses a QinQ VLAN tag termination sub-interface to connect to a CE.
* Binding a QinQ stacking sub-interface to a VSI: applies to scenarios where a PE uses a QinQ stacking sub-interface to connect to a CE.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VPLS applications, different CEs are transparently connected to each other on the same network segment of a LAN through VSIs, and the IP addresses of the CEs therefore must be different. The IP address of the interface connecting a PE to a CE and the IP address of the CE must be on different network segments. Otherwise, the local CE may learn incorrect ARP entries, leading to traffic loss between CEs in the same VSI.



#### Procedure

* Bind an Ethernet interface to a VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of the AC interface (Ethernet interface) used by the PE to directly connect to the CE is displayed.
  3. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* [ **access-port** ]
     
     
     
     The Ethernet interface is bound to a VSI.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind an Ethernet sub-interface to a VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
     
     
     
     The view of the AC interface (sub-interface) used by the PE to directly connect to a CE is displayed.
  3. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
     
     
     
     The VLAN encapsulation type is set on the sub-interface.
  4. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
     
     
     
     The Ethernet sub-interface is bound to a VSI.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind a VLANIF interface to a VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface vlanif**](cmdqueryname=interface+vlanif) *vlan-id*
     
     
     
     The VLANIF interface view is displayed.
  3. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
     
     
     
     The VLANIF interface is bound to a VSI.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind an L2VE sub-interface to a VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number.subinterface-number*
     
     
     
     The VE sub-interface view is displayed.
  3. Run [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id*
     
     
     
     The VLAN ID of the VE sub-interface is configured.
  4. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
     
     
     
     The L2VE sub-interface is bound to a VSI.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind an Eth-Trunk interface to a VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     
     
     An Eth-Trunk interface is created.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface to be added to the Eth-Trunk interface is displayed.
  5. Run [**eth-trunk**](cmdqueryname=eth-trunk) *trunk-id*
     
     
     
     The interface is added to the Eth-Trunk interface.
     
     
     
     An interface to be added to an Eth-Trunk interface cannot have Layer 3 configurations (such as IP addresses) or services.
     
     One Ethernet interface can be added only to one Eth-Trunk interface. Before adding an Ethernet interface to an Eth-Trunk interface, ensure that the Ethernet interface does not belong to any Eth-Trunk interface.
     
     The types of the interfaces on both ends of an Eth-Trunk member link must be the same.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     
     
     The Eth-Trunk interface view is displayed.
  8. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* [ **access-port** ]
     
     
     
     The Eth-Trunk interface is bound to a VSI.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind an Eth-Trunk sub-interface to a VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     
     
     An Eth-Trunk interface is created.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface to be added to the Eth-Trunk interface is displayed.
     
     
     
     An Eth-Trunk member interface cannot be configured with a static MAC address.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The member interfaces of a trunk interface cannot be Eth-Trunk interfaces.
  5. Run [**eth-trunk**](cmdqueryname=eth-trunk) *trunk-id*
     
     
     
     The interface is added to the Eth-Trunk interface.
     
     
     
     An interface to be added to an Eth-Trunk interface cannot have Layer 3 configurations (such as IP addresses) or services.
     
     One Ethernet interface can be added only to one Eth-Trunk interface. Before adding an Ethernet interface to an Eth-Trunk interface, ensure that the Ethernet interface does not belong to any Eth-Trunk interface.
     
     The types of the interfaces on both ends of an Eth-Trunk member link must be the same.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id interface-number*
     
     
     
     The Eth-Trunk sub-interface view is displayed.
  8. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
     
     
     
     The VLAN encapsulation type is set on the sub-interface.
  9. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
     
     
     
     The Eth-Trunk sub-interface is bound to a VSI.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Bind a dot1q VLAN tag termination sub-interface to a VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
     
     
     
     The view of the AC interface (sub-interface) used by the PE to directly connect to a CE is displayed.
  3. Run [**encapsulation**](cmdqueryname=encapsulation) **dot1q-termination** [ **rt-protocol** ]
     
     
     
     The encapsulation type is configured to be dot1q VLAN tag termination for the sub-interface.
     
     
     
     **rt-protocol** must be specified if you want the dot1q VLAN tag termination sub-interface to support routing protocols.
  4. Run [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* [ **to** *high-pe-vid* ] [ **vlan-group** *group-id* ]
     
     
     
     The sub-interface is configured to terminate single-tagged packets.
     
     
     
     After you specify **rt-protocol**, the dot1q VLAN tag termination sub-interface can terminate only packets carrying a fixed-value VLAN tag.
  5. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
     
     
     
     The dot1q VLAN tag termination sub-interface is bound to a VSI.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind a QinQ VLAN tag termination sub-interface to a VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
     
     
     
     The view of the AC interface (sub-interface) used by the PE to directly connect to a CE is displayed.
  3. Run [**encapsulation**](cmdqueryname=encapsulation) **qinq-termination** [ **local-switch** | **rt-protocol** ]
     
     
     
     The encapsulation type is configured to be QinQ VLAN tag termination for the sub-interface.
     
     
     
     In the preceding command:
     + Specify **local-switch** if you want the QinQ VLAN tag termination sub-interface to support local switching.
     + Specify **rt-protocol** if you want the QinQ VLAN tag termination sub-interface to support routing protocols.
  4. Run [**qinq termination pe-vid**](cmdqueryname=qinq+termination+pe-vid) *pe-vid* [ **to** *high-pe-vid* ] **ce-vid** *ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ]
     
     
     
     The sub-interface is configured to terminate QinQ packets.
     
     
     
     After you specify **rt-protocol**, the QinQ VLAN tag termination sub-interface can terminate only double-tagged packets whose inner and outer tags are specific VLAN IDs.
  5. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
     
     
     
     The QinQ VLAN tag termination sub-interface is bound to a VSI.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind a QinQ stacking sub-interface to a VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
     
     
     
     The view of the AC interface (sub-interface) used by the PE to directly connect to a CE is displayed.
  3. Run [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid) *low-ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ]
     
     
     
     A QinQ stacking sub-interface is configured.
     
     
     
     If you want to run the [**qinq stacking vid**](cmdqueryname=qinq+stacking+vid) command on different sub-interfaces of an Ethernet interface, you must specify different **ce-vid** values for the sub-interfaces.
     
     + If you have run the [**vlan-group**](cmdqueryname=vlan-group) command to configure a VLAN group on a sub-interface, you must specify **vlan-group** in the **qinq stacking vid** command.
     + If you have not run the [**vlan-group**](cmdqueryname=vlan-group) command to configure a VLAN group on a sub-interface, you cannot specify **vlan-group** in the **qinq stacking vid** command.
  4. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
     
     
     
     The QinQ stacking sub-interface is bound to a VSI.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.