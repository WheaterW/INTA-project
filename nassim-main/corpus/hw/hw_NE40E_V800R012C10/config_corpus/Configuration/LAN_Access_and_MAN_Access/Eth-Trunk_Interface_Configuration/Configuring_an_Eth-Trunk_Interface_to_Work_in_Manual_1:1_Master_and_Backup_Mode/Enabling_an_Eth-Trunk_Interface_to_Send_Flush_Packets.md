Enabling an Eth-Trunk Interface to Send Flush Packets
=====================================================

If an Eth-Trunk interface is enabled to send Flush packets, after the master and backup interfaces are switched, the new master interface sends Flush packets to instruct the peer end to age MAC addresses. This function prevents data interruption caused by asynchronous MAC addresses.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   A control VLAN is created, and its view is displayed.
   
   
   
   This VLAN is used to control the sending of Flush packets on the local and remote devices' Eth-Trunk interfaces in manual 1:1 master/backup mode. Therefore, the VLAN ID must be the same as the ID of the VLAN that sends Flush packets.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
   
   
   
   The view of the Eth-Trunk interface in manual 1:1 master/backup mode is displayed.
5. Run [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) { { *vlan-id1* [ **to** *vlan-id2* ] }&<1-10> | **all** }
   
   
   
   The interface is configured to allow packets from the control VLAN to pass through.
   
   
   
   The VLAN IDs of received and sent Flush packets must be the same.
6. Run [**smart-link flush send vlan**](cmdqueryname=smart-link+flush+send+vlan) *vlan-id*
   
   
   
   The Eth-Trunk interface is enabled to send SmartLink Flush packets.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.