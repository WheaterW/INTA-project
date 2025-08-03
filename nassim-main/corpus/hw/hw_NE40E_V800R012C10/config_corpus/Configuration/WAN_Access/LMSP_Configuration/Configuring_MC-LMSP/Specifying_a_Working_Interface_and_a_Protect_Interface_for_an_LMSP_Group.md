Specifying a Working Interface and a Protect Interface for an LMSP Group
========================================================================

A working interface and a protection interface must be specified and added to an LMSP group before other LMSP configurations are performed.

#### Context

An LMSP group includes one working interface and one protection interface. An LMSP group is the smallest unit protected by LMSP. The communication messages between the working interface and the protection interface are transmitted within the LMSP group. Specifying a working interface and a protection interface and adding them to an LMSP group are the prerequisites for LMSP operation. The working interface is connected to a working link and the protection interface is connected to a protection link. When an LMSP group works in 1:1 mode, the working interface transmits traffic, but the protection interface does not. The protection interface takes over traffic after LMSP switching is performed. When an LMSP group works in 1+1 mode, both the working and protection interfaces transmit traffic. The receive end receives traffic only from the working link.

Perform the following steps on the routers where the MC-LMSP working and protection interface are located separately:


#### Procedure

1. Specify an LMSP working interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run the following commands to display the interface view:
      
      
      ```
      [controller cpos](cmdqueryname=controller+cpos) cpos-number
      ```
   3. Run [**aps group**](cmdqueryname=aps+group) *aps-group-id*
      
      
      
      An LMSP group is created, and an interface is added to the LMSP group.
   4. Run [**aps working**](cmdqueryname=aps+working) *peer-ip* *local-ip*
      
      
      
      The interface added to the LMSP group is specified as a working interface.
2. Specify an LMSP protection interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run the following commands to display the interface view:
      
      
      ```
      [controller cpos](cmdqueryname=controller+cpos) cpos-number
      ```
   3. Run [**aps group**](cmdqueryname=aps+group) *aps-group-id*
      
      
      
      An LMSP group is created, and an interface is added to the LMSP group.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The working and protection interfaces must be added to a single LMSP group.
   4. Run [**aps protect**](cmdqueryname=aps+protect) *peer-ip* *local-ip*
      
      
      
      The interface added to the LMSP group is specified as a protection interface.
   5. (Optional) Run [**aps signal-low-priority**](cmdqueryname=aps+signal-low-priority)
      
      
      
      The low-priority signal failure code for a switching request carried in the K byte is specified on the protection interface.
3. In MC-LMSP 1+1 unidirectional mode, run:
   
   
   ```
   [hold-up](cmdqueryname=hold-up)
   ```
   
   The interface is configured to remain Up.
   
   This command is used on the working and protection interfaces of the LMSP group that works in MC-LMSP 1+1 unidirectional mode.
   
   MC-LMSP 1+1 needs to be associated with dual bypass PWs. In MC-LMSP 1+1 unidirectional mode, if an AC-side interface is Down, one of the bypass PWs associated with the interface will be deleted. Then traffic will not be forwarded by the deleted bypass PW. To address this problem, the [**hold-up**](cmdqueryname=hold-up) command must be run on an MC-LMSP interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After this command has been run, the alarm functions do not take effect on the LMSP group interface, the link indicator on the LMSP group interface is always on, and the interface remains Up even when no fiber is attached to it.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

In an MC-LMSP scenario, run the [**aps authenticate**](cmdqueryname=aps+authenticate) command to configure a PGP authentication string.