Configuring an EFM OAM Working Mode for an Interface
====================================================

An EFM OAM working mode is an attribute of an interface enabled with EFM OAM. An interface works in either active or passive mode.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

An EFM OAM working mode can be configured for an interface only when EFM OAM has been globally enabled and EFM OAM has not been enabled on the interface. After EFM OAM is enabled on the interface, the EFM OAM working mode of the interface cannot be changed.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface at one end of a link is displayed.
3. Run [**efm mode**](cmdqueryname=efm+mode) { **active** | **passive** }
   
   
   
   An EFM OAM working mode is configured for the interface.
   
   
   
   At least one of two interfaces at both ends of a link must be configured to work in active mode.
   * If an interface is configured to work in active mode, it initiates the peer discovery process after being enabled with EFM OAM.
   * If an interface is configured to work in passive mode, it does not initiate the peer discovery process but waits for OAM PDUs from the remote interface.
   
   If two interfaces at both ends of a link are configured to work in active mode, link detection can also be performed. If they are configured to work in passive mode, link detection cannot be performed.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.