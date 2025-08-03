Configuring MAC Address Safety
==============================

You can limit the number of MAC addresses to be learned and the rate of MAC address learning and specify the action to be taken when MAC address learning in the VSI exceeds the limit.

#### Context

After a VSI receives a frame, if an entry that matches the destination address cannot be found in the MAC address table, the frame is regarded as an unknown frame. Unknown frames can be unknown unicast frames, unknown multicast frames, or unknown multicast frames.

A provider edge (PE) processes broadcast packets in the following mode, and the processing mode is unchangeable:

* If a PE receives broadcast packets from a local user, the PE forwards the packets to other AC interfaces and other PEs on the same VPLS network.
* If a PE receives broadcast packets from a remote PE, the PE forwards the packets only to AC interfaces on the same VPLS network.
* A PE discards excess broadcast packets.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If the VSI has already learned MAC addresses before MAC address learning limits are configured, run the [**reset mac-address**](cmdqueryname=reset+mac-address) command in the system view to clear those addresses; otherwise, MAC address learning cannot be accurately limited.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ]
   
   
   
   The VSI view is displayed.
3. Run [**mac-limit**](cmdqueryname=mac-limit) { **action** { **discard** | **forward** } | **maximum** *maxValue* **rate** *interval* } \*
   
   
   
   MAC address learning limits are configured for the VSI.
   
   
   
   When *max* and *interval* are both set to **0**, the maximum number of MAC addresses to be learned and the highest rate of MAC address learning are not limited.
   
   After MAC address learning limits are configured, the system checks the number of learned MAC addresses before learning a new MAC address. If the number of learned MAC addresses reaches the limit, the system does not learn the new MAC address.
   
   **discard** indicates that packets with new MAC addresses are discarded after the number of learned MAC addresses reaches the limit. **forward** indicates that packets with new MAC addresses are forwarded after the number of learned MAC addresses reaches the limit, but the new MAC addresses are not added to the MAC address table.
4. Run [**unknown-frame**](cmdqueryname=unknown-frame) { **unicast** { **broadcast** | **drop** [ **mac-learning** ] } | **multicast** { **broadcast** | **drop** } }
   
   
   
   The processing mode for received unicast or multicast unknown frames is configured for the VSI.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.