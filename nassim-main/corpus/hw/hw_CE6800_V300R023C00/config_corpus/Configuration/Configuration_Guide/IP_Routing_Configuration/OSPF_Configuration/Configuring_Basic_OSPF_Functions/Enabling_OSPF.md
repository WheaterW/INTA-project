Enabling OSPF
=============

Enabling OSPF

#### Prerequisites

Before enabling OSPF, you have completed the following task:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.

#### Context

A router ID must exist before a device runs OSPF. The router ID is a 32-bit unsigned integer that uniquely identifies the device in an AS. To ensure OSPF stability, plan router IDs properly during network planning and manually set the router ID of each device during network deployment.

OSPF partitions an AS into different areas to prevent the LSDB size from unexpectedly growing. An area is regarded as a logical group, and each group is identified by an area ID. The border of an area is a device rather than a link. A network segment (or a link) belongs to only one area, and the area to which each OSPF interface belongs must be specified.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an OSPF process and enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) process-id [ router-id route-id | vpn-instance vpname ] *
   ```
   
   *process-id* specifies the ID of an OSPF process, and the default value is 1.
   
   The device supports OSPF multi-process. Processes can be classified by service type. Devices exchange packets regardless of process IDs. Therefore, packets can also be exchanged between devices with different process IDs.
   
   **router-id** *router-id* specifies the router ID of a device.
   
   By default, a device automatically selects the IP address of an interface as the router ID. When configuring a router ID, ensure that the router ID is unique in an AS. You can configure the IP address of a device interface as the device's router ID.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   Each router ID in an OSPF process must be unique. Otherwise, an OSPF neighbor relationship cannot be established, and routing information is incorrect. Manually setting a unique router ID for each device is recommended.
   
   If a router ID conflict occurs, perform either of the following operations:
   
   * Manually configure a new router ID.
     ```
     [ospf](cmdqueryname=ospf) router-id router-id
     ```
   * Enable the router ID automatic recovery function to ensure that the device can automatically allocate a new router ID.
     ```
     [undo ospf router-id auto-recover disable](cmdqueryname=undo+ospf+router-id+auto-recover+disable)
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     If the automatic recovery function is enabled and a router ID conflict occurs between indirectly connected devices in one OSPF area, the conflicting router ID is replaced with a newly calculated one, regardless of whether the conflicting router ID was manually configured or automatically generated.
     
     If a router ID conflict persists, a device can replace a router ID for a maximum of three attempts.
3. (Optional) Configure a description for the OSPF process.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   
   To easily identify a specific process, you can add a description for the process.
4. Create an OSPF area, and enter the OSPF area view.
   
   
   ```
   [area](cmdqueryname=area) area-id
   ```
   
   OSPF areas are classified as either a backbone area (with area ID 0) or non-backbone area. The backbone area forwards inter-area routing information, and routing information exchanged between non-backbone areas must be forwarded through the backbone area.
5. (Optional) Configure a description for the OSPF area.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   
   To easily identify a specific area, you can add a description for the area.
6. To configure OSPF, configure the network segments included in an area or enable OSPF on an interface.
   
   
   * Configure the network segments included in an area.
     
     ```
     [network](cmdqueryname=network) address wildcard-mask [ description text ]
     ```
     
     **description** *text* specifies the description for a network segment.
     
     OSPF runs on an interface only when both of the following conditions are met:
     
     1. The mask length of the interface's IP address is greater than or equal to that specified in the [**network**](cmdqueryname=network) command.![](../public_sys-resources/note_3.0-en-us.png) 
        
        If the *wildcard-mask* in the [**network**](cmdqueryname=network) command is all zeros and the IP address of the interface is the same as the IP address specified in the [**network**](cmdqueryname=network) *address* command, OSPF is also enabled on the interface.
     2. The interface's primary IP address belongs to the network segment specified in the [**network**](cmdqueryname=network) command.
     
     By default, OSPF uses a host route with a 32-bit mask to advertise the IP address of a loopback interface, regardless of the mask length configured for the IP address. Therefore, to allow a loopback interface to advertise network-segment routes, its network type must be set to NBMA or broadcast in the interface view. For details on how to set the network type, see [Setting the Network Type to Broadcast](vrp_ospf_cfg_0022.html).
   * Enable OSPF on an interface.
     1. Exit the area view.
        ```
        [quit](cmdqueryname=quit)
        ```
     2. Enter the interface view.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        ```
     3. Switch the interface working mode from Layer 2 to Layer 3. Determine whether to perform this step based on the current interface working mode.
        ```
        [undo portswitch](cmdqueryname=undo+portswitch)
        ```
        
        Determine whether to perform this step based on the current interface working mode.
     4. Enable OSPF on the interface.
        ```
        [ospf enable](cmdqueryname=ospf+enable) [ process-id ] area area-id
        ```
        
        The area ID specified using *area-id* can be either a decimal integer or in the format of an IPv4 address. Regardless of the format, the area ID is displayed as an IPv4 address.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

If a router ID is changed, run the following command for the new router ID to take effect:

```
[reset ospf](cmdqueryname=reset+ospf) [ process-id ] process
```