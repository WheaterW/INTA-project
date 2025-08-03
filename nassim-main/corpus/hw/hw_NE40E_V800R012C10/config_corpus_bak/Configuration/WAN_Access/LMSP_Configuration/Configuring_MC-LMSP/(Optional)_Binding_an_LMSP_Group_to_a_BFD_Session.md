(Optional) Binding an LMSP Group to a BFD Session
=================================================

(Optional)_Binding_an_LMSP_Group_to_a_BFD_Session

#### Context

To monitor an MC-LMSP group, a BFD session monitors an mPW between the working and protection interfaces on the AC side, and the MC-LMSP group is bound to another BFD session. If faults occur, the working and protection devices can use BFD to notify each other of the faults and implement rapid traffic switchovers between the working and protection devices.

Perform the following steps on the working or protection interface of an LMSP group:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run the following commands:
   
   
   ```
   [controller cpos](cmdqueryname=controller+cpos) cpos-number
   ```
   
   The working interface view or the protection interface view is displayed.
3. Bind an LMSP group to a BFD session.
   
   
   
   This configuration procedure is based on a scenario where BFD is configured to track the status of the working interface and quickly transmit the status to the device where the protection interface resides. The procedure for configuring BFD to track the protection interface and quickly transmit the status to the device where the working interface resides is similar.
   
   1. Establish an mPW between MC-LMSP-enabled devices. For the configuration procedure, see the chapter "Configuration PW Redundancy" in VPN in the Configuration Guide.
   2. Run the [**bfd**](cmdqueryname=bfd) *cfg-name* **bind pw interface** *interface-type* *interface-number* **track-interface interface** *interface-type* *interface-number* command on the device with a working interface to configure a BFD session to monitor the mPW and bind the BFD session to the working interface.
   3. Run the [**bfd**](cmdqueryname=bfd) *cfg-name* **bind pw interface** *interface-type* *interface-number* **select-board** *slot-id* command on the device with a protection interface to specify the interface board where the BFD session is configured to monitor the mPW.
   4. Run the [**aps track bfd-session**](cmdqueryname=aps+track+bfd-session) **session-name** *bfd-session-name* command on the device with the protection interface to bind the interface to the BFD session.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**undo aps group**](cmdqueryname=undo+aps+group) command deletes the LMSP group configurations and removes the binding between the LMSP group and a BFD session if configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.