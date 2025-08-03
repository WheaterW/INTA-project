Associating a BFD Session with a Sub-interface
==============================================

Association between a BFD session and a sub-interface triggers rapid route convergence. Only a single-hop BFD session with a default multicast IP address can be bound to a sub-interface.

#### Usage Scenario

If high reliability is required and sub-interfaces are configured with a large number of services, only a BFD session needs to be configured on an interface not on each sub-interface. The BFD session can be associated with the sub-interface status to allow the sub-interface's protocol status to be synchronized with the interface's protocol status. This association improves service reliability and saves BFD session resources.


#### Pre-configuration Tasks

Before associating a BFD session with a sub-interface, complete the following tasks:

* Enable BFD globally.
* Create a single-hop BFD session, bind it to an interface, and configure the default multicast address for detection.
* Set up the BFD session and ensure that the BFD session is Up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd) *session-name*
   
   
   
   The BFD session view is displayed.
3. Run [**process-interface-status**](cmdqueryname=process-interface-status) [**sub-if**] [ **reboot-no-impact** ]
   
   
   
   The BFD session is associated with the sub-interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a BFD session goes Down, the BFD status on the interface bound to the BFD session and its sub-interfaces also becomes Down.