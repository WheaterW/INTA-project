Configuring an IS-IS Administrative Tag Value
=============================================

Configuring an IS-IS Administrative Tag Value

#### Context

Administrative tags are used to control the advertisement of IP prefixes in an IS-IS routing domain, simplifying routing management.

**Figure 1** Network diagram before an IS-IS administrative tag is configured  
![](figure/en-us_image_0000001130624402.png)

In [Figure 1](#EN-US_TASK_0000001130624348__fig_dc_feature_isis_001101), DeviceA needs to communicate with DeviceB, DeviceC, and DeviceD in other Level-1 areas. To ensure information security, the other routing devices in these Level-1 areas must not receive the packets sent by DeviceA. You can configure the same administrative tag for the IS-IS interfaces on DeviceB, DeviceC, and DeviceD. Then, apply the configured administrative tag on the Level-1-2 device in area 4 when it leaks routes from the Level-2 area to the Level-1 area. In this way, DeviceA communicates with only DeviceB, DeviceC, and DeviceD during communication with other Level-1 areas. [Figure 2](#EN-US_TASK_0000001130624348__fig_dc_feature_isis_001102) shows the topology formed on DeviceA.

**Figure 2** Network diagram after an IS-IS administrative tag is configured  
![](figure/en-us_image_0000001176743859.png)

#### Procedure

* Configure an administrative tag value for all interfaces in an IS-IS process.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure an administrative tag value for all interfaces in the IS-IS process.
     
     
     ```
     [circuit default-tag](cmdqueryname=circuit+default-tag) tag [ level-1 | level-2 ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The LSPs advertised by the interface carry the configured administrative tag only if the IS-IS cost style is wide, wide-compatible, or compatible. To set a cost style, run the **cost-style** command.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an administrative tag value for a specified IS-IS interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure an administrative tag value for the interface.
     
     
     ```
     [isis tag-value](cmdqueryname=isis+tag-value) tag [ level-1 | level-2 ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The LSPs advertised by the interface carry the configured administrative tag only if the IS-IS cost style is wide, wide-compatible, or compatible. To set a cost style, run the **cost-style** command.
     
     The administrative tag value configured using the [**isis tag-value**](cmdqueryname=isis+tag-value) command takes precedence over that configured using the [**circuit default-tag**](cmdqueryname=circuit+default-tag) command.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] command to check administrative tags of IS-IS routes.