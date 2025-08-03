Configuring OPS to Control Packet Sending and Receiving on RIP Interfaces
=========================================================================

Configuring OPS to Control Packet Sending and Receiving on RIP Interfaces

#### Prerequisites

Before configuring OPS to control packet sending and receiving on RIP interfaces, complete the following task:

* [Configure static BFD for RIP](vrp_rip_cfg_0048.html).


#### Context

[Figure 1](#EN-US_TASK_0000001382327600__fig1274872311373) shows an unaffiliated static BFD for RIP scenario where primary and backup paths exist. If the link from DeviceA to DeviceB on the primary path fails, BFD on DeviceA rapidly detects the link fault, and the RIP route on DeviceA rapidly converges to the backup path. Because DeviceB does not support BFD or is not configured with BFD, DeviceB cannot rapidly detect the link fault. As a result, the RIP route on DeviceB cannot converge rapidly. In this case, DeviceB continues to send RIP messages to DeviceA. After DeviceA re-learns the RIP route from DeviceB, traffic is switched from the backup path to the primary path. However, the link from DeviceA to DeviceB is still faulty. As a result, traffic cannot be forwarded.

**Figure 1** Networking diagram of unaffiliated static BFD for RIP  
![](figure/en-us_image_0000001382168944.png)

#### Precautions

* The OPS mechanism allows a single script assistant to cache a maximum of 256 alarms. Therefore, this function does not apply to the scenario where BFD goes down due to a large number of link faults.
* After this function is enabled, you are advised not to perform an active/standby switchover, restart the device, or modify static BFD for RIP configurations when a link is faulty. Otherwise, the command for disabling an interface from receiving and sending RIP packets may fail to be deleted, causing a residual configuration.
* Broadcast network scenarios are not supported.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OPS view.
   
   
   ```
   [ops](cmdqueryname=ops)
   ```
3. Create a script assistant.
   
   
   ```
   [script-assistant python](cmdqueryname=script-assistant+python) ripbfd_down_mtp.py
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After this function is enabled, if BFD Down alarm information is received, the script assistant obtains information about the interface corresponding to the faulty link from the alarm information and determines whether to disable the interface from sending and receiving RIP packets based on whether the **rip bfd static** command is configured on the interface.
   
   * If the **rip bfd static**, **undo rip output**, and **undo rip input** commands are run on the interface, the interface is disabled from sending and receiving RIP packets.
   * If the **rip bfd static** command is not run on the interface, the interface is not affected.
4. Create a script assistant.
   
   
   ```
   [script-assistant python](cmdqueryname=script-assistant+python) ripbfd_up_mtp.py
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After this function is enabled, if BFD Down alarm clearing information is received, the script assistant obtains information about the interface corresponding to the faulty link from the alarm information and determines whether to allow the interface to send and receive RIP packets based on whether the **rip bfd static** command is configured on the interface.
   
   * If the **rip bfd static**, **rip output**, and **rip input** commands are run on the interface, the interface is allowed to send and receive RIP packets.
   * If the **rip bfd static** command is not run on the interface, the interface is not affected.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ops assistant**](cmdqueryname=display+ops+assistant) **current** command to check the current status of script assistants.