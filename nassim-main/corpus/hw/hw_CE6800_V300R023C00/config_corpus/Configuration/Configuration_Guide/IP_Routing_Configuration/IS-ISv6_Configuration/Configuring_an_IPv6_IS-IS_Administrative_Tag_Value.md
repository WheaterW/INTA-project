Configuring an IPv6 IS-IS Administrative Tag Value
==================================================

Configuring an IPv6 IS-IS Administrative Tag Value

#### Prerequisites

Before configuring an IPv6 IS-IS administrative tag value, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

Administrative tags are used to control the advertisement of IPv6 prefixes in an IPv6 IS-IS routing domain, simplifying routing management.

**Figure 1** IS-IS networking  
![](figure/en-us_image_0000001176742121.png)

In [Figure 1](#EN-US_TASK_0000001130622610__fig_dc_feature_isis_001101), DeviceA needs to communicate with DeviceB, DeviceC, and DeviceD in other Level-1 areas. To ensure information security, the other routing devices in these Level-1 areas must not receive the packets sent by DeviceA. You can configure the same administrative tag for the IS-IS interfaces on DeviceB, DeviceC, and DeviceD. Then, apply the configured administrative tag on the Level-1-2 device in area 4 when it leaks routes from the Level-2 area to the Level-1 area. In this way, DeviceA communicates with only DeviceB, DeviceC, and DeviceD during communication with other Level-1 areas. [Figure 2](#EN-US_TASK_0000001130622610__fig_dc_feature_isis_001102) shows the topology formed on DeviceA.

**Figure 2** Network diagram after an IS-IS administrative tag is configured  
![](figure/en-us_image_0000001130782452.png)

#### Procedure

* Configure an administrative tag value for all interfaces in an IPv6 IS-IS process.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure an administrative tag value for all interfaces in the IPv6 IS-IS process.
     
     
     ```
     [ipv6 circuit default-tag](cmdqueryname=ipv6+circuit+default-tag) tag [ level-1 | level-2 ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The LSPs advertised by the interface carry the configured administrative tag only if the IS-IS cost style is wide, wide-compatible, or compatible. To set a cost style, run the **cost-style** command.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an administrative tag value for a specified IPv6 IS-IS interface.
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
  4. Configure an administrative tag value for the interface.
     
     
     ```
     [isis ipv6 tag-value](cmdqueryname=isis+ipv6+tag-value) tag [ level-1 | level-2 ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The LSPs advertised by the interface carry the configured administrative tag only if the IS-IS cost style is wide, wide-compatible, or compatible. To set a cost style, run the **cost-style** command.
     
     The administrative tag value configured using the [**ipv6 isis tag-value**](cmdqueryname=ipv6+isis+tag-value) command takes precedence over that configured using the [**ipv6 circuit default-tag**](cmdqueryname=ipv6+circuit+default-tag) command.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display isis**](cmdqueryname=display+isis) *process-id* **route** **ipv6** [ *ipv6-address* [ *prefix-length* ] | { **level-1** | **level-2** } | **verbose** ] \* command to check administrative tags of IPv6 IS-IS routes.