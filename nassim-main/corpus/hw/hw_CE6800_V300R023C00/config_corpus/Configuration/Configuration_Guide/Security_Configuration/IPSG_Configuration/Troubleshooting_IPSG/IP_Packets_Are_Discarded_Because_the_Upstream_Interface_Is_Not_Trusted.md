IP Packets Are Discarded Because the Upstream Interface Is Not Trusted
======================================================================

IP Packets Are Discarded Because the Upstream Interface Is Not Trusted

#### Fault Symptom

After IPSG is enabled in a VLAN, none of the hosts in the VLAN can access the Internet, and IP packets from these hosts are discarded.

In [Figure 1](#EN-US_TASK_0000001563889229__fig731121412439), PC1 and PC2 belong to VLAN 10, and Interface1 allows packets from VLAN 10. The static binding entries of PC1 and PC2 have been configured on DeviceA, and IPSG has been enabled in VLAN 10. The PCs can communicate with each other, but cannot access the Internet. The following uses PC1 as an example.

* PC1 sends a packet to the Internet. When the packet reaches Interface1 on DeviceA, DeviceA detects that the packet matches a binding entry, and forwards it.
* A packet is sent from the Internet to PC1. When the packet reaches Interface3 (which belongs to VLAN 10) on DeviceA, DeviceA detects that the packet does not match any binding entry, and discards the packet.

**Figure 1** Network diagram for scenarios where IP packets are discarded because the upstream interface is not trusted  
![](figure/en-us_image_0000001563769621.png)
#### Possible Causes

The upstream interface is not configured as a trusted interface in the IPSG-enabled VLAN.



#### Procedure

1. Check whether the upstream interface belongs to the IPSG-enabled VLAN.
   
   
   ```
   [display ip source check user-bind status static](cmdqueryname=display+ip+source+check+user-bind+status+static) [ { interface interface-type interface-number | ip-address ip-address | mac-address mac-address | vlan  vlan-id } * ] [ valid | invalid ] [ slot slot-id ]
   ```
2. If the upstream interface belongs to the VLAN, configure the interface as a trusted interface; otherwise, the return packets will be discarded because they do not match the binding entries.
   
   
   1. Enter the system view.
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enable DHCP globally.
      ```
      [dhcp enable](cmdqueryname=dhcp+enable)
      ```
   3. Enable DHCP snooping globally.
      ```
      [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
      ```
   4. Configure Interface3 as a trusted interface in the interface view.
      ```
      [dhcp snooping trusted](cmdqueryname=dhcp+snooping+trusted)
      ```