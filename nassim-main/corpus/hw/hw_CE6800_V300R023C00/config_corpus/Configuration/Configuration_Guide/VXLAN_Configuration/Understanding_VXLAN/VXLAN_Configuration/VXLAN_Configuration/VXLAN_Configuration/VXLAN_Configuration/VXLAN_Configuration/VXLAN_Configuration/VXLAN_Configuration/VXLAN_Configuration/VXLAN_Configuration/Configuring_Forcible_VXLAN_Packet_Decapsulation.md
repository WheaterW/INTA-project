Configuring Forcible VXLAN Packet Decapsulation
===============================================

Configuring Forcible VXLAN Packet Decapsulation

#### Context

![](../public_sys-resources/note_3.0-en-us.png) 

Forcible VXLAN decapsulation is supported only by the following: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6863E-48S8CQ, CE6855-48XS8CQ, CE6885-SAN.

When a device needs to send VXLAN packets to an analyzer, you can enable forcible VXLAN decapsulation on the inbound interface of the device to reduce the load of the analyzer. As a result, the device sends only original packets to the analyzer.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a VXLAN packet inbound interface.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Enable forcible VXLAN decapsulation.
   
   
   ```
   [vxlan force-decapsulation enable](cmdqueryname=vxlan+force-decapsulation+enable)
   ```
   
   By default, forcible VXLAN decapsulation is disabled on an interface.
4. (Optional) Configure a packet redirection outbound interface after forcible VXLAN decapsulation is performed.
   
   
   ```
   [quit](cmdqueryname=quit)
   [vxlan vni](cmdqueryname=vxlan+vni+force-redirect+interface) vni-id1 [ to vni-id2 ] force-redirect interface { interface-name | interface-type interface-num }
   ```
   
   By default, the original outbound interface is used to forward packets after forcible VXLAN decapsulation is performed.
   
   You can configure a packet redirection outbound interface to enable the analyzer to receive specific original packets. Packets that meet the filtering condition are then redirected to the specified outbound interface after forcible VXLAN decapsulation is performed. This step specifies the binding relationship between the VNI and redirection outbound interface. During forcible VXLAN decapsulation, the device obtains the VNI of VXLAN packets. After VXLAN decapsulation, the original packets are forwarded through the redirection outbound interface and sent to the analyzer.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```