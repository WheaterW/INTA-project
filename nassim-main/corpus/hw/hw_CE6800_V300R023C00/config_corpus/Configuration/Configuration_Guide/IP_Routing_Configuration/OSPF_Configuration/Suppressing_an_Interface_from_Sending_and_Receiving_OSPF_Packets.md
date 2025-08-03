Suppressing an Interface from Sending and Receiving OSPF Packets
================================================================

Suppressing an Interface from Sending and Receiving OSPF Packets

#### Prerequisites

Before suppressing an interface from sending and receiving OSPF packets, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

If a device interface is suppressed from sending and receiving OSPF packets, link information about this interface will not be used for route calculation. This ensures that routes to the other interfaces on the device are preferentially selected.

For example, there are three routes between DeviceA and DeviceB, as shown in [Figure 1](#EN-US_TASK_0000001176663009__fig_dc_vrp_ospf_cfg_203701). To ensure that the route to interface 2 is selected as the optimal route, you need to suppress interface 1 and interface 3 from sending and receiving OSPF packets.

**Figure 1** Network diagram of suppressing the interfaces from sending and receiving OSPF packets  
![](figure/en-us_image_0000001176663075.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Suppress a specified interface from sending and receiving OSPF packets.
   
   
   ```
   [silent-interface](cmdqueryname=silent-interface) { all | interface-type interface-number }
   ```
   
   Different processes can suppress the same interface from sending and receiving OSPF packets, but the [**silent-interface**](cmdqueryname=silent-interface) command is valid only for the OSPF interfaces enabled in the current process.
   
   After an OSPF interface is configured to be in silent state, the interface can still advertise its direct routes. Hello packets on the interface, however, cannot be sent. Therefore, a neighbor relationship cannot be established on the interface. This can enhance the networking adaptability of OSPF and reduce system resource consumption.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check information about OSPF interfaces.