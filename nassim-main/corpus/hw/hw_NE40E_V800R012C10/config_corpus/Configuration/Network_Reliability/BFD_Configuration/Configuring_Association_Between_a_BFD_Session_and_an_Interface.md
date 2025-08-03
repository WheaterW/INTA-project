Configuring Association Between a BFD Session and an Interface
==============================================================

You can configure association between a BFD session and an interface to enable the BFD session to quickly detect faults on the interface. One BFD session can be associated with only one interface. That is, if an interface is associated with a BFD session, the interface cannot be associated with another BFD session. Likewise, when a BFD session is associated with an interface, the BFD session cannot be associated with another interface.

#### Usage Scenario

Association between a BFD session and an interface enables the BFD session to quickly detect faults on the interface.

If unidirectional transmission of fault information from a BFD session to an interface is configured: In [Figure 1 Unidirectional fault transmission from a BFD session to an interface](#EN-US_TASK_0172361666__fig_dc_vrp_bfd_cfg_200802), CE1 is directly connected to PE1 and PE3, and CE2 is directly connected to PE2 and PE4. A BFD session is created between PE1 and PE2. When detecting a link fault, the BFD session notifies the OAM management module. This triggers interface1 directly connecting each PE to a CE to go down. The CE can then detect the fault and switch traffic to a backup path, thereby ensuring reliable service transmission.

**Figure 1** Unidirectional fault transmission from a BFD session to an interface![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/1.


  
![](images/fig_dc_vrp_bfd_cfg_200802.png)

#### Pre-configuration Tasks

Before associating a BFD session with an interface, create a BFD session by referring to [Establishing a BFD Session](dc_vrp_bfd_cfg_0006.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**oam-mgr**](cmdqueryname=oam-mgr)
   
   
   
   The OAM management view is displayed.
3. Run [**oam-bind ingress bfd-session**](cmdqueryname=oam-bind+ingress+bfd-session) { *bfd-session-id* | **session-name** *bfd-session-name* } **trigger** **if-down** [ **reboot-impact** ] **egress** **interface** { *interface-name* | *interface-type* *interface-num* }
   
   
   
   The BFD session is configured to transmit fault notification messages to an interface.
   
   When BFD detects a fault, the physical interface bound to the BFD session goes down.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When TE FRR is deployed on a network and the fault detected by BFD is quickly rectified, the physical interface goes up but the BFD session remains down. As a result, some traffic is discarded due to switching failures. To ensure that traffic is quickly switched, run the [**bfd trigger if-down**](cmdqueryname=bfd+trigger+if-down) command to associate the status of the BFD session with the status of the bound physical interface.