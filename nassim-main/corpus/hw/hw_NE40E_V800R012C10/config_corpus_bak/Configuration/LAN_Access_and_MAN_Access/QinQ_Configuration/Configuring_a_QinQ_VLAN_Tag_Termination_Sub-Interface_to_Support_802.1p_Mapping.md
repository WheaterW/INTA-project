Configuring a QinQ VLAN Tag Termination Sub-Interface to Support 802.1p Mapping
===============================================================================

After tags are terminated on the PEs, packets are sent to the carrier IP or MPLS network. To ensure inclusion of all the required Quality of Service (QoS) information in the packets, the 802.1p values in outer and inner tags must be mapped to the DSCP fields or the EXP fields.

#### Usage Scenario

* QinQ VLAN tag termination can be used to implement the 802.1p and DSCP remark.
  
  Relevant standards specify that the six bits of the Type of Service (ToS) field in an IPv4 packet header serve as the DiffServ Code Point (DSCP). DSCP provides a reference for differentiated services (DiffServ) and is used for QoS guarantee on the IP network.
  
  With QinQ VLAN tag termination, a tagged packet is terminated on the PE before it is sent to the carrier IP network. In this scenario, you need to configure the mapping relationship between the 802.1p values in outer and inner tags and the DSCP field to ensure that all the required QoS information is included in the packet.
* QinQ VLAN tag termination can be used to implement the 802.1p and EXP remark.
  
  The EXP field in an MPLS packet is used for Class of Service (CoS) to implement traffic control on the gateway.
  
  With QinQ VLAN tag termination, a tagged packet is terminated on the PE before it is sent to the carrier MPLS network. In this scenario, you need to configure the mapping relationship between the 802.1p values in outer and inner tags and the EXP field to ensure that all the required QoS information is included in the packet.

#### Pre-configuration Tasks

Before you configure a VLAN tag termination sub-interface to transmit IP services, plan user VLANs so that packets received by the VLAN tag termination sub-interface carry one or two VLAN tags.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
   
   
   
   The view of an Ethernet sub-interface on the user side of a PE is displayed.
3. Run [**encapsulation**](cmdqueryname=encapsulation) **qinq-termination** [ **local-switch** | **rt-protocol** ]
   
   
   
   The encapsulation type is configured as QinQ VLAN tag termination for the sub-interface.
   
   
   
   * Specify **local-switch** so that the QinQ VLAN tag termination sub-interface supports local switching.
   * Specify **rt-protocol** so that the QinQ VLAN tag termination sub-interface supports routing protocols.
4. Run [**qinq termination pe-vid**](cmdqueryname=qinq+termination+pe-vid) *pe-vid* [ **to** *high-pe-vid* ] **ce-vid** *ce-vid* [ **to** *high-ce-vid* ]
   
   
   
   The VLAN tag termination function is configured for the QinQ VLAN tag termination sub-interface.
   
   
   
   If **rt-protocol** is specified, the QinQ VLAN tag termination sub-interface terminates double-tagged packets whose inner and outer tags contain only single VLAN IDs (not VLAN ranges).
5. Run [**qinq 8021p-mode**](cmdqueryname=qinq+8021p-mode) { **trust** { **ce-vid-8021p** | **pe-vid-8021p** } | *precedence-value* }

#### Verifying the Configuration

After a QinQ VLAN tag termination sub-interface is configured to support 802.1p mapping, run the [**display qinq information termination**](cmdqueryname=display+qinq+information+termination) [ **interface** *interface-type interface-number* [ .*subinterface-number* ] ] command on the PE to check detailed configurations on the QinQ VLAN tag termination sub-interface.