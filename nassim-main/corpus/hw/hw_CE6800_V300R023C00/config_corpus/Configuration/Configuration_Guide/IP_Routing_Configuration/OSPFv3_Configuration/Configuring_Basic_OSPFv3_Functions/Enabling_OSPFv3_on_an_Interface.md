Enabling OSPFv3 on an Interface
===============================

Enabling OSPFv3 on an Interface

#### Context

After enabling OSPFv3 in the system view, you need to enable OSPFv3 on interfaces as required.

Since OSPFv3 supports multi-instance, you need to specify the ID of the instance to which an OSPFv3 process belongs when enabling OSPFv3 on an interface. If no instance ID is specified, OSPFv3 is enabled in instance 0 bound to the interface by default. The instances bound to the interfaces between which a neighbor relationship is to be established must be the same. Perform the following steps on each device that needs to run OSPFv3.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable OSPFv3 on the interface.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) process-id area area-id [ instance instance-id ]
   ```
   
   
   
   The specified area ID can be a decimal integer or in the IPv4 address format. Regardless of the specified format, the area ID is displayed as an IPv4 address.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```