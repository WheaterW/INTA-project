Suppressing an Interface from Sending and Receiving OSPFv3 Packets
==================================================================

Suppressing an Interface from Sending and Receiving OSPFv3 Packets

#### Prerequisites

Before suppressing an interface from sending and receiving OSPFv3 packets, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

To prevent a device interface from sending its OSPFv3 routing information to other devices on the network and disable the device interface from receiving routing updates from other devices, you can suppress the interface from sending and receiving OSPFv3 packets. After the interface is suppressed, OSPFv3 packets carrying this interface's routing information can still be advertised (through other interfaces on the device) but this interface's Hello packets will be blocked. As a result, no neighbor relationships can be established between this interface and other devices. This configuration can enhance the networking adaptability of OSPFv3 and reduce system resource consumption.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Suppress a specified interface from sending and receiving OSPFv3 packets.
   
   
   ```
   [silent-interface](cmdqueryname=silent-interface+%28OSPFv3+view%29) { all | interface-type interface-number }
   ```
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   In different processes, you can suppress the same interface from sending and receiving OSPFv3 packets. However, the [**silent-interface**](cmdqueryname=silent-interface) configuration takes effect only on the interfaces in the specified process, not on the interfaces of other processes.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **no-peer** | **area** *area-id* ] [ *interface-type* *interface-number* ] command to check OSPFv3 interface information.