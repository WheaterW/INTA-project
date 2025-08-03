(Optional) Configuring Layer 2 Multicast Fast Recovery
======================================================

(Optional) Configuring Layer 2 Multicast Fast Recovery

#### Prerequisites

Before configuring Layer 2 multicast fast recovery, you have completed the following task:

* Set up a scenario with M-LAG master and backup devices.

#### Context

In a scenario where an M-LAG is used for Layer 2 multicast access, if an M-LAG member interface fails, the link corresponding to the M-LAG member interface goes down, and Layer 2 multicast entries on the interface are deleted. When the link goes up again, the interface needs to learn the entries again. As a result, the link switching takes a long time, and a large number of packets are lost. To prevent this problem, configure the Layer 2 multicast fast recovery function. After this function is configured, the device ignores the interface down event and retains Layer 2 multicast entries on the interface in the preceding situation. In addition, the device updates the entry aging time based on the packet maintenance entries synchronized from the backup device. After the interface goes up again, it does not need to learn Layer 2 multicast entries again, which speeds up the link switching and shortens the service interruption time.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable MLD snooping globally.
   
   
   ```
   [mld snooping enable](cmdqueryname=mld+snooping+enable)
   ```
3. Enter the view of an Eth-Trunk interface.
   
   
   ```
   [interface](cmdqueryname=interface) eth-trunk trunk-id
   ```
4. Switch the interface working mode from Layer 3 to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
5. Enable Layer 2 multicast fast recovery.
   
   
   ```
   [mld snooping port-fast-control](cmdqueryname=mld+snooping+port-fast-control)
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The [**mld snooping port-fast-control**](cmdqueryname=mld+snooping+port-fast-control) and [**mld snooping static-group**](cmdqueryname=mld+snooping+static-group) commands are mutually exclusive.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```