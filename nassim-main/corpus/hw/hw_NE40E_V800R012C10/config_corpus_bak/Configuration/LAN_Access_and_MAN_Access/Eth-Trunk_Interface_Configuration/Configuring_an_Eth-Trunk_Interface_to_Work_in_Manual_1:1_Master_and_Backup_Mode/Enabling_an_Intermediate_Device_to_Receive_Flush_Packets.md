Enabling an Intermediate Device to Receive Flush Packets
========================================================

Link reliability can be implemented between master and backup links only after intermediate devices are enabled to receive Flush packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   A control VLAN is created, and its view is displayed.
   
   
   
   This VLAN is used to forward the Flush packets sent by the local and remote devices' Eth-Trunk interfaces in manual 1:1 master/backup mode. Therefore, the VLAN ID must be the same as the ID of the VLAN that sends Flush packets.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed. The intermediate devices' interfaces that connect to the Eth-Trunk interfaces at both ends of the Eth-Trunk link as well as the intermediate devices' interfaces that connect to each other must all be specified.
5. Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The interface is switched to Layer 2 mode.
6. Run [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) { { *vlan-id1* [ **to** *vlan-id2* ] }&<1-10> | **all** }
   
   
   
   The interface is configured to allow packets from the control VLAN to pass through.
   
   
   
   The VLAN IDs of received and sent Flush packets must be the same.
7. Run [**smart-link flush enable control-vlan**](cmdqueryname=smart-link+flush+enable+control-vlan) *vlan-id*
   
   
   
   The interface is enabled to receive SmartLink Flush packets.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.