Specifying a Working Interface and a Protection Interface for an LMSP Group
===========================================================================

A working interface and a protection interface must be specified and added to an LMSP group before other LMSP configurations are performed.

#### Context

An LMSP group includes one working interface and one protection interface, and they are the smallest units protected by LMSP. The communication messages between the working interface and the protection interface are transmitted within the LMSP group. Specifying a working interface and a protection interface and adding them to an LMSP group are the prerequisites for LMSP operation. The working interface is connected to a working link and the protection interface is connected to a protection link. When an LMSP group works in 1:1 mode, the working interface transmits traffic, but the protection interface does not. The protection interface takes over traffic after LMSP switching is performed. When an LMSP group works in 1+1 mode, both the working and protection interfaces transmit traffic. The receive end receives traffic only from the working link.

Perform the following steps on the Router that requires LMSP:


#### Procedure

1. Specify an LMSP working interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* or [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
      
      
      
      The interface view is displayed.
   3. Run [**aps group**](cmdqueryname=aps+group) *aps-group-id*
      
      
      
      An LMSP group is created, and an interface is added to the LMSP group.
   4. Run [**aps working**](cmdqueryname=aps+working)
      
      
      
      The interface added to the LMSP group is specified as a working interface.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      In a single-chassis LMSP scenario, the working and protection interfaces may be on different subcards. If the working interface is abnormal during the restart of the two subcards, neither the configurations on the working interface nor the configurations on the protection interface can be restored.
2. Specify an LMSP protection interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* or [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
      
      
      
      The interface view is displayed.
   3. Run [**aps group**](cmdqueryname=aps+group) *aps-group-id*
      
      
      
      An LMSP group is created, and an interface is added to the LMSP group.
      
      
      
      ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
      
      The working and protection interfaces must be added to a single LMSP group.
   4. Run [**aps protect**](cmdqueryname=aps+protect)
      
      
      
      The interface added to the LMSP group is specified as a protection interface.