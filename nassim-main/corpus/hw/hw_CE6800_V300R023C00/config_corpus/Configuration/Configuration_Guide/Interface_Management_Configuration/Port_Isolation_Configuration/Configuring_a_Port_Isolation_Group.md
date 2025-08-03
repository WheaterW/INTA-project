Configuring a Port Isolation Group
==================================

Configuring a Port Isolation Group

#### Context

To isolate broadcast packets in the same VLAN but allow users on different interfaces to communicate at Layer 3, you can set the port isolation mode to Layer 2 isolation and Layer 3 interworking. You can also prevent users on different interfaces in the same VLAN from communicating with each other by setting the port isolation mode to Layer 2 and Layer 3 isolation. [Figure 1](#EN-US_CONCEPT_0000001251918969__fig1587831014518) shows the method and application scenario of port isolation. PC1, PC2, and PC3 belong to VLAN 10. After interface 1 and interface 2 connected to PC1 and PC2 are added to a port isolation group, PC1 and PC2 cannot communicate with each other in VLAN 10. PC3 can still communicate with PC1 and PC2.

**Figure 1** Network diagram of port isolation![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1, Interface2, and Interface3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001207365334.png)

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Ethernet interface view.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 3 to Layer 2.
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable the port isolation group function.
   ```
   [port-isolate enable](cmdqueryname=port-isolate+enable) group group-id
   ```
   
   By default, the port isolation group function is disabled. This function applies only to interfaces on the same device and cannot isolate interfaces on different devices.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display port-isolate**](cmdqueryname=display+port-isolate) **group** { *group-id* | **all** } command to check the configurations of all port isolation groups or a specified one.