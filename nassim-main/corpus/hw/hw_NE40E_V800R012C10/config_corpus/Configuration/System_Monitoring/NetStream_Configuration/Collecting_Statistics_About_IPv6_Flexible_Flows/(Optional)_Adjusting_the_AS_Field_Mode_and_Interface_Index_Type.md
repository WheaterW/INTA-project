(Optional) Adjusting the AS Field Mode and Interface Index Type
===============================================================

For the NSC to properly receive and parse NetStream packets output by the NDE, ensure that the AS field modes and interface index types configured on the NDE and the NSC are the same.

#### Context

The NSC can properly receive and parse NetStream packets output by the NDE only when the AS field modes and interface index types on the NDE and NSC are the same.

* **AS field mode**: The length of the AS field in IP packets can be set to 16 bits or 32 bits. Devices on a network must use the same AS field mode. An AS field mode inconsistency causes NetStream to fail to sample inter-AS traffic.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the 32-bit AS field mode is used, the NMS must be able to identify the 32-bit AS field. Otherwise, the NMS fails to identify inter-AS traffic sent by devices.
* **Interface index**: The NMS uses an interface index carried in a NetStream packet output by the NDE to query information about the interface that sends the packet. The interface index can be 16 or 32 bits long. The NMSs of different vendors may support different interface index lengths. As such, the NDE must use an interface index length that is supported by the NMS. For example, if the NMS can parse 32-bit interface indexes, set the length of the interface indexes carried in the output NetStream packets to 32-bit.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Compared with the default 16-bit interface index, the 32-bit interface index can be identified by more third-party NMSs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip netstream as-mode**](cmdqueryname=ip+netstream+as-mode) { **16** | **32** }
   
   
   
   An AS field mode is set.
3. Run [**ipv6 netstream export index-switch**](cmdqueryname=ipv6+netstream+export+index-switch) { **16** | **32** }
   
   
   
   The length type of the interface index carried in the NetStream packets output by the device is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.