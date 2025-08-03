Creating an OSPFv3 Process
==========================

Creating an OSPFv3 Process

#### Prerequisites

Before creating an OSPFv3 process, you have completed the following task:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.

#### Context

OSPFv3 supports multi-process. This means that multiple OSPFv3 processes running on a single device are identified by their process IDs. You can set an OSPFv3 process ID when creating an OSPFv3 process. The process ID is only locally valid and does not affect packet exchange with other devices.

A router ID is a 32-bit unsigned integer that uniquely identifies a device in an AS, and follows the IPv4 address format. The OSPFv3 router ID must be manually set, and OSPFv3 cannot run properly without a router ID.

When you configure a router ID for a device, ensure that the router ID in an AS is unique. When multiple processes need to run on the same device, you are advised to specify a unique router ID for each process.

To ensure OSPFv3 stability, plan router IDs properly during network design and manually set the router ID of each device during network deployment.

Perform the following steps on each device that needs to run OSPFv3.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an OSPFv3 process and enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) process-id
   ```
3. (Optional) Configure a description for the OSPFv3 process.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   
   To easily identify a specific process, you can add a description for the OSPFv3 process.
4. Configure a router ID.
   
   
   ```
   [router-id](cmdqueryname=router-id) router-id
   ```
   
   This router ID must be unique in an AS. The common practice is to select the IP address of an interface on the device as the router ID.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The router ID for each OSPFv3 process must be unique across the whole network. Otherwise, an OSPFv3 neighbor relationship cannot be established, and routing information is incorrect. You are advised to set a network-wide unique router ID for each OSPFv3 process on an OSPFv3 device.
   
   If a router ID conflict occurs, perform either of the following operations:
   
   * Manually configure a new router ID.
     ```
     [router-id](cmdqueryname=router-id) router-id
     ```
   * Enable the router ID automatic recovery function to ensure that the device can automatically allocate a new router ID.
     ```
     [undo ospfv3 router-id auto-recover disable](cmdqueryname=undo+ospfv3+router-id+auto-recover+disable)
     ```![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the automatic recovery function is enabled and a router ID conflict occurs between indirectly connected devices in one OSPFv3 area, the conflicting router ID is replaced with a newly calculated one, even if the conflicting router ID was manually configured.
   
   If a router ID conflict persists, a device can replace a router ID for a maximum of three attempts.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```