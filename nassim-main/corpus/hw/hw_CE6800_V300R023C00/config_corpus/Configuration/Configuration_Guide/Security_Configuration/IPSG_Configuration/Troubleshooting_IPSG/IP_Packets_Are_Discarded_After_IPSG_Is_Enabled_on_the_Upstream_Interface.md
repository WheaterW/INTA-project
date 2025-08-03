IP Packets Are Discarded After IPSG Is Enabled on the Upstream Interface
========================================================================

IP Packets Are Discarded After IPSG Is Enabled on the Upstream Interface

#### Fault Symptom

After IPSG is enabled on the interfaces connected to hosts, none of the hosts can access the Internet, and IP packets from authorized hosts are discarded.

In [Figure 1](#EN-US_TASK_0000001513049274__fig684201975516), static binding entries are configured on DeviceA for PC1 and PC2, IPSG is enabled on Interface1, Interface2, and Interface3, and the PCs can communicate with each other. However, the PCs cannot access the Internet. The following uses PC1 as an example.

* PC1 sends a packet to the Internet. When the packet reaches Interface1 on DeviceA, DeviceA detects that the packet matches a binding entry, and forwards it.
* A packet is sent from the Internet to PC1. When the packet reaches Interface3 on DeviceA, DeviceA detects that the packet does not match any binding entry, and discards the packet.

**Figure 1** Network diagram for scenarios where IP packets are discarded after IPSG is enabled on the upstream interface  
![](figure/en-us_image_0000001513169258.png)
#### Possible Causes

IPSG is enabled on the upstream interface, but this interface is not configured as a trusted interface.



#### Procedure

1. Check whether IPSG is enabled on Interface3.
   
   
   ```
   [display ip source check user-bind status static](cmdqueryname=display+ip+source+check+user-bind+status+static) [ { interface interface-type interface-number | ip-address ip-address | mac-address mac-address | vlan  vlan-id } * ] [ valid | invalid ] [ slot slot-id ] 
   ```
2. If IPSG is enabled on the interface, that is, **ipv4 source check user-bind enable** is displayed in the command output, disable IPSG in the interface view.
   
   
   ```
   [undo ipv4 source check user-bind enable](cmdqueryname=undo+ipv4+source+check+user-bind+enable)
   ```