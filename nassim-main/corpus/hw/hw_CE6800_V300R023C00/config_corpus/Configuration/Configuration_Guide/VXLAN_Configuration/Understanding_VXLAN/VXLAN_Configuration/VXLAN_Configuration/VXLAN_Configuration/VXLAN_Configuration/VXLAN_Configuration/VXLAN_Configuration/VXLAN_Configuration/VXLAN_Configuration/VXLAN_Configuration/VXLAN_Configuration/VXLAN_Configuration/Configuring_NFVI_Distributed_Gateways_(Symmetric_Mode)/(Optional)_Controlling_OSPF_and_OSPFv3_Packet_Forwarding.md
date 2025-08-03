(Optional) Controlling OSPF/OSPFv3 Packet Forwarding
====================================================

(Optional) Controlling OSPF/OSPFv3 Packet Forwarding

#### Context

By default, after receiving an OSPF/OSPFv3 multicast packet through a VXLAN tunnel, a device processes and forwards the packet. Perform this task if the device does not need to establish an OSPF/OSPFv3 neighbor relationship over a VXLAN tunnel or does not need to forward OSPF/OSPFv3 multicast packets.

Perform the following steps on the L2GW/L3GW.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Perform either of the following steps as required:
   
   
   * If the device does not need to establish an OSPF/OSPFv3 neighbor relationship over a VXLAN tunnel but needs to forward OSPF/OSPFv3 multicast packets, run the following command.
     ```
     [assign forward nvo3](cmdqueryname=assign+forward+nvo3) { ospf | ospfv3 } disable
     ```
   * If the device does not need to establish an OSPF/OSPFv3 neighbor relationship over a VXLAN tunnel or forward OSPF/OSPFv3 multicast packets, run the following command.
     ```
     [assign forward nvo3](cmdqueryname=assign+forward+nvo3) { ospf | ospfv3 } packet discard
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```