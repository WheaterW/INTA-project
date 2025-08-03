Using GMAC Ping to Check Link Connectivity on a Layer 2 Network
===============================================================

Generic MAC (GMAC) ping applies to a part of or a whole network for monitoring connectivity without configuring a maintenance domain (MD), maintenance association (MA), or maintenance association end point (MEP).

#### Context

GMAC ping has principles similar to those of 802.1ag MAC ping. The difference is that a source device does not need to be a MEP, and a destination device does not need to be a MEP or maintenance association intermediate point (MIP). In other words, GMAC ping can be implemented without the need to configure an MD, MA, or MEP on the source, intermediate, or destination device.

Enable the GMAC ping function on the source and destination devices. The intermediate devices must support the bridge forwarding function.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ping mac enable**](cmdqueryname=ping+mac+enable)
   
   
   
   The GMAC ping function is enabled globally.
   
   
   
   If the GMAC ping function is enabled:
   
   * A source device starts the GMAC ping function by sending a loopback message (LBM) to a destination device.
   * After receiving the LBM, the destination device replies to the source device with a loopback reply (LBR).
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
4. (Optional) In a VLAN scenario: Run [**ping mac**](cmdqueryname=ping+mac) *mac-address* **vlan** *vlan-id* [ **interface** *interface-type* *interface-number* | **-c** *count* | **-s** *packetsize* | **-t** *timeout* **-p** *priority-value* ] \*
   
   
   
   The VLAN network connectivity is checked.
   
   
   
   The following shows an example:
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] ping mac enable 
   [*HUAWEI] commit 
   [~HUAWEI] ping mac 00e0-fc12-3456 vlan 10 -c 2 -s 112 
   Reply from 00e0-fc12-3456: bytes = 112 time < 1ms 
   Reply from 00e0-fc12-3456: bytes = 112 time < 1ms 
   Packets: Sent = 2, Received = 2, loss = 0 (0.00% loss) 
   Minimum = 1ms, Maximum = 1ms, Average = 1ms 
   ```
5. (Optional) In a VLL scenario: Run [**ping mac**](cmdqueryname=ping+mac) *mac-address* **l2vc** *l2vc-id* { **raw** | **tagged** } [ **interface** *interface-type* *interface-number* | { **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **dot1q-vlan** *vlan-id* } **-c** *count* | **-s** *packetsize* | **-t** *timeout* | **-p** *priority-value* ] \*
   
   
   
   The VLL network connectivity is checked.
   
   
   
   The following is an example:
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] ping mac enable
   [*HUAWEI] commit
   [~HUAWEI] ping mac 00e0-fc12-3456 l2vc 1 raw -c 2 -s 112
   Reply from 00e0-fc12-3456: bytes = 112 time < 1ms
   Reply from 00e0-fc12-3456: bytes = 112 time < 1ms
   Packets: Sent = 2, Received = 2, loss = 0 (0.00% loss)
   Minimum = 1ms, Maximum = 1ms, Average = 1ms
   ```
6. (Optional) In a VPLS scenario: Run [**ping mac**](cmdqueryname=ping+mac) *mac-address* **vsi** *vsi-name* [ **interface** *interface-type* *interface-number* | { **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **dot1q-vlan** *vlan-id* } **-c** *count* | **-s** *packetsize* | **-t** *timeout* | **-p** *priority-value* ] \*
   
   
   
   The VPLS network connectivity is checked.
   
   
   
   The following is an example:
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] ping mac enable
   [*HUAWEI] commit
   [~HUAWEI] ping mac 00e0-fc12-3456 vsi vsi1 -c 2 -s 112
   Reply from 00e0-fc12-3456: bytes = 112 time < 1ms
   Reply from 00e0-fc12-3456: bytes = 112 time < 1ms
   Packets: Sent = 2, Received = 2, loss = 0 (0.00% loss)
   Minimum = 1ms, Maximum = 1ms, Average = 1ms
   ```