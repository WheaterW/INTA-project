Configuring AVP Attributes of L2TP Packets
==========================================

The control messages used to connect tunnels contain multiple AVP attributes. You can configure the AVP attributes of packets to adjust L2TP connections.

#### Context

Different AVP attributes contain different information. You can configure the AVP attributes of L2TP packets to store the AVP information, thereby controlling the transmission of packets. Perform the following operations on the NE40E:


#### Procedure

* Configure a VE interface to encapsulate attributes strictly based on the interface name.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**access attribute virtual-ethernet format interface-name**](cmdqueryname=access+attribute+virtual-ethernet+format+interface-name)
     
     
     
     A VE interface is configured to encapsulate attributes strictly based on the interface name.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Encapsulate the AVP 22 attribute into L2TP packets.
  
  
  
  In a scenario where the NE40E functions as a LAC and an L2TP user attempts to go online, you can run the [**l2tp calling-number-avp enable**](cmdqueryname=l2tp+calling-number-avp+enable) command to determine whether to encapsulate the AVP 22 attribute into ICRQ packets to be sent by the LAC.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2tp calling-number-avp enable**](cmdqueryname=l2tp+calling-number-avp+enable)
     
     
     
     The AVP 22 attribute is added to L2TP packets.
  3. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
     
     
     
     The L2TP group view is displayed.
  4. (Optional) Run any of the following commands to configure the LAC to encapsulate the AVP 22 attribute into ICRQ packets to be sent in a specified format:
     
     
     + To configure the LAC to encapsulate the AVP 22 attribute in version 1 format into ICRQ packets to be sent, run the [**calling-number-avp format**](cmdqueryname=calling-number-avp+format) **version1** **[ include** **option82 ]** command.
     + To configure the LAC to encapsulate the AVP 22 attribute into ICRQ packets to be sent using a user-defined format, run the [**calling-number-avp format**](cmdqueryname=calling-number-avp+format) **{ include** [ **delimiter** *delimiter* ] { **option82** [ **delimiter** *delimiter* ] | **mac** [ **delimiter** *delimiter* ] | **interface** [ **delimiter** *delimiter* ] | **domain** [ **delimiter** *delimiter* ] | **sysname** [ **delimiter** *delimiter* ] | **vlan** [ **delimiter** *delimiter* ] | **pevlan** [ **delimiter** *delimiter* ] | **cevlan** [ **delimiter** *delimiter* ] | **agent-circuit-id** [ **delimiter** *delimiter* ] | **agent-remote-id** [ **delimiter** *delimiter* ] }\* } command.
     + (Optional) To configure the LAC to encapsulate the AVP 22 attribute into ICRQ packets to be sent in the version3 format, run the [**calling-number-avp format version3**](cmdqueryname=calling-number-avp+format+version3) command.
  5. (Optional) Run [**calling-number-avp format llid**](cmdqueryname=calling-number-avp+format+llid)
     
     
     
     The device is configured to encapsulate LLID information into the AVP 22 attribute of packets to be sent to the LNS.
  6. (Optional) Run [**calling-number-avp format radius-force**](cmdqueryname=calling-number-avp+format+radius-force)
     
     
     
     The Calling-Station-Id is added to the AVP 22 attribute of the packets delivered by the RADIUS server on the LAC to the LNS.
  7. (Optional) Set the offset of the inner VLAN ID encapsulated into ICRQ packets.
     
     
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
        
        The interface view is displayed.
     3. Run [**bas**](cmdqueryname=bas)
        
        The BAS interface view is displayed.
     4. Run [**calling-number-avp cevlan-offset**](cmdqueryname=calling-number-avp+cevlan-offset) *offset-value*
        
        The offset of the inner VLAN ID encapsulated into ICRQ packets is set.
        
        If packets sent from different DSLAMs have the same CE-VLAN ID and the CE-VLAN ID must be identified in the ICRQ packets to be sent by the LAC, configure an offset for the CE-VLAN ID.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        This configuration takes effect only after the device is configured to encapsulate the CV-VLAN ID into the AVP 22 attribute of ICRQ packets using the [**calling-number-avp format**](cmdqueryname=calling-number-avp+format) **include** **cevlan** [ **delimiter** *delimiter* ] command.
     5. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  8. (Optional) Run [**avp calling-number interface-format exclude sub-slot**](cmdqueryname=avp+calling-number+interface-format+exclude+sub-slot)
     
     
     
     The device is configured not to encapsulate the subslot ID into interface description of the AVP 22 attribute of L2TP packets.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Hide AVPs in transmission.
  
  
  
  The L2TP protocol uses AVPs to send and negotiate L2TP attributes. For security purposes, you can hide AVPs in transmission.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
     
     
     
     The L2TP group view is displayed.
  3. Run [**tunnel avp-hidden**](cmdqueryname=tunnel+avp-hidden)
     
     
     
     AVPs are hidden in transmission.
     
     
     
     The function to hide AVPs in transmission takes effect only when tunnel authentication is enabled on both ends of a tunnel.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After AVPs are hidden in transmission, if AAA authentication is used for a tunnel, the two ends must use the same password.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable AVP 46 for a tunnel.
  
  
  
  After AVP 46 is enabled for a tunnel, the cause of tunnel teardown is added to the STOPCCN packets sent from the LAC to the LNS.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
     
     
     
     The L2TP group view is displayed.
  3. Run [**tunnel avp46**](cmdqueryname=tunnel+avp46)
     
     
     
     AVP 46 is enabled for the tunnel.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the AVP 47 attribute into L2TP packets.
  
  
  
  After the AVP 47 attribute is configured, the LAC marks the outer DSCP value of the L2TP packets so that the packets with different DSCP values have different priorities.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
     
     
     
     The L2TP group view is displayed.
  3. Run [**set-dscp-outer**](cmdqueryname=set-dscp-outer) [ **lns** ] *dscp-value*
     
     
     
     The outer DSCP value of L2TP packets is configured so that the LAC can negotiate with the peer device (LNS) for the AVP 47 attribute.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the access line AVP attribute of ICRQ packets.
  
  
  
  If you need a device to carry the access line AVP in an ICRQ packet or parse the access line AVP in an ICRQ packet, configure the following functions as required.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run **[**l2tp-group**](cmdqueryname=l2tp-group)** **group-name**
     
     
     
     An L2TP group is created.
  3. On the LAC, run [**lac avp access-line-info include**](cmdqueryname=lac+avp+access-line-info+include) { *agent-circuit-id* | *agent-remote-id* | *actual-data-rate-upstream* | *actual-data-rate-downstrea*m }
     
     
     
     The access line AVP is specified to be carried in ICRQ packets.
  4. On the LNS, run [**lns avp access-line-info allow**](cmdqueryname=lns+avp+access-line-info+allow) { *agent-circuit-id* | *agent-remote-id* | *actual-data-rate-upstream* | *actual-data-rate-downstream* }
     
     
     
     The LNS is configured to parse the access line AVP in ICRQ packets and encapsulate the parsing result into RADIUS attributes of packets to be sent to the RADIUS server.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.