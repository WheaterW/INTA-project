Configuring the Access Side
===========================

You can configure IGMP snooping over EVPN MPLS on the access side of an EVPN that carries multicast services for various scenarios.

#### Context

The configurations required for various scenarios are as follows:

* A CE is single-homed to a source PE or dual-homed to source PEs on the multicast source side. In this scenario, no additional configuration is required on the access side. IGMP signaling synchronization based on BGP EVPN IGMP Join Synch routes needs to be configured in a BD.
* A CE is single-homed to a receiver PE on the access side. In this scenario, no additional configuration is required on the access side. IGMP signaling synchronization based on BGP EVPN IGMP Join Synch routes needs to be configured in a BD.
* A CE is dual-homed to receiver PEs on the access side. In this scenario, IGMP signaling synchronization based on BGP EVPN IGMP Join Synch routes needs to be configured in a BD, the EVI-RT extended community attributes of IGMP Join Synch routes need to be associated with the BD, and the DF status ignoring function needs to be enabled on non-DF nodes.
* A CE is dual-homed to receiver PEs on the access side, and Layer 2 multicast services on the access side access Layer 3 multicast services. In this scenario, IGMP and PIM-SM need to be enabled on a VBDIF interface, IGMP signaling synchronization based on BGP EVPN IGMP Join Synch routes needs to be configured in a BD, the EVI-RT extended community attributes of IGMP Join Synch routes need to be associated with the BD, and the DF status ignoring function needs to be enabled on non-DF nodes.


#### Procedure

* A CE is single-homed to a receiver PE on the access side.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**igmp-snooping signal-synch enable**](cmdqueryname=igmp-snooping+signal-synch+enable)
     
     
     
     IGMP signaling synchronization based on BGP EVPN IGMP Join Synch routes is enabled.
  4. (Optional) Run [**evi vpn-target**](cmdqueryname=evi+vpn-target) *vrfRt* [ *vrfRtType* ]
     
     
     
     The EVI-RT extended community attribute is associated with IGMP Join Synch routes in the BD.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* A CE is dual-homed to receiver PEs on the access side.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**igmp-snooping signal-synch enable**](cmdqueryname=igmp-snooping+signal-synch+enable)
     
     
     
     IGMP signaling synchronization based on BGP EVPN IGMP Join Synch routes is enabled.
  4. Run [**igmp-snooping signal-ignore-df enable**](cmdqueryname=igmp-snooping+signal-ignore-df+enable)
     
     
     
     DF status ignorance is enabled for BDs on the non-DF node.
  5. Run [**evi vpn-target**](cmdqueryname=evi+vpn-target) *vrfRt* [ *vrfRtType* ]
     
     
     
     The EVI-RT extended community attribute is associated with IGMP Join Synch routes in the BD.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* A CE is dual-homed to receiver PEs on the access side, and Layer 2 multicast services on the access side access Layer 3 multicast services.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**undo igmp-snooping proxy**](cmdqueryname=undo+igmp-snooping+proxy)
     
     
     
     IGMP snooping proxy is disabled in the BD.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface vbdif**](cmdqueryname=interface+vbdif) *bd-id*
     
     
     
     The VBDIF interface view is displayed.
  6. Run [**pim sm**](cmdqueryname=pim+sm)
     
     
     
     PIM is enabled.
  7. Run [**igmp enable**](cmdqueryname=igmp+enable)
     
     
     
     IGMP is enabled.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  9. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  10. Run [**igmp-snooping signal-synch enable**](cmdqueryname=igmp-snooping+signal-synch+enable)
      
      
      
      IGMP signaling synchronization based on BGP EVPN IGMP Join Synch routes is enabled.
  11. Run [**igmp-snooping signal-ignore-df enable**](cmdqueryname=igmp-snooping+signal-ignore-df+enable)
      
      
      
      DF status ignorance is enabled for BDs on the non-DF node.
  12. Run [**evi vpn-target**](cmdqueryname=evi+vpn-target) *vrfRt* [ *vrfRtType* ]
      
      
      
      The EVI-RT extended community attribute is associated with IGMP Join Synch routes in the BD.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.