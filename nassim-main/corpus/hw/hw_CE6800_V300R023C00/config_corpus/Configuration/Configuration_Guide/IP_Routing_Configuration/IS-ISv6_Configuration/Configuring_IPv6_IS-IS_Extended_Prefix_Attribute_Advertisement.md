Configuring IPv6 IS-IS Extended Prefix Attribute Advertisement
==============================================================

Configuring IPv6 IS-IS Extended Prefix Attribute Advertisement

#### Context

IS-IS defines a type of extended prefix attribute (IPv4/IPv6 Extended Reachability Attribute) sub-TLVs. These sub-TLVs are used to describe the origin of advertised routes and can be advertised in IPv4, IPv6, and locator TLVs. Based on the advertised sub-TLVs, the device can determine whether the received routes are inter-domain routes or host routes.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL in low latency mode does not support IPv6.

The extended prefix attribute flag (IPv4/IPv6 Extended Reachability Attribute Flags) is a part of the extended prefix attribute sub-TLV. The specific composition is as follows:

**Figure 1** Format of the IPv4/IPv6 Extended Reachability Attribute Flags sub-TLV  
![](figure/en-us_image_0000001666795697.png)

[Table 1](#EN-US_TASK_0000001666704689__en-us_task_0000001618178050_tab_dc_vrp_isis_feature_000701) describes the fields of the extended prefix attribute flag.

**Table 1** Description of fields in the IPv4/IPv6 Extended Reachability Attribute Flags sub-TLV
| Field | Length | Description |
| --- | --- | --- |
| X | 1 bit | External prefix flag:   * This flag indicates whether the prefix is imported from another protocol or IS-IS process and re-advertised. * The value of this flag remains unchanged during inter-level leaking. * For an IPv6 prefix, the X flag is not set to 1 because the parent TLV has a flag with the same function. |
| R | 1 bit | Re-advertisement flag:   * This flag is set to 1 when routes leak from a Level-1 area to a Level-2 area or from a Level-2 area to a Level-1 area on an IS-IS Level-1-2 device. * When local direct routes leak, this flag is not set to 1. |
| N | 1 bit | Node flag:   * This flag can be set to 1 when an IPv4 host route (with a 32-bit subnet mask) or IPv6 host route (with a 128-bit subnet mask) is advertised. You can run a command to determine whether to set this flag. * The setting of this flag is kept when routes are leaked on an IS-IS Level-1-2 device. |

You can determine whether to configure a device to advertise the extended prefix attribute flag.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an IS-IS process and enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ] [ vpn-instance vpn-instance-name ]
   ```
3. Enable IPv6 for the IS-IS process.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable) [ topology { compatible [ enable-mt-spf ] | ipv6 | standard } ]
   ```
4. Enable the IPv6 IS-IS process to advertise the extended prefix attribute flag.
   
   
   ```
   [ipv6 advertise prefix-attributes flags](cmdqueryname=ipv6+advertise+prefix-attributes+flags)
   ```
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. (Optional) Set the N flag of the extended prefix attribute on a loopback interface in the IPv6 IS-IS process to 0.
   
   
   
   By default, if a loopback interface's route with a 128-bit subnet mask is a host route, the extended prefix N flag is set to 1. To set the extended prefix N flag to 0, perform this step.
   
   1. Enter the loopback interface view.
      ```
      [interface](cmdqueryname=interface) Loopback interface-number
      ```
   2. Switch the interface working mode from Layer 2 to Layer 3.
      ```
      [undo portswitch](cmdqueryname=undo+portswitch)
      ```
      
      Determine whether to perform this step based on the current interface working mode.
   3. Enable IS-IS on the interface.
      ```
      [isis ipv6 enable](cmdqueryname=isis+ipv6+enable) [ process-id ]
      ```
   4. Set the N flag of the extended prefix attribute on the loopback interface in the IPv6 IS-IS process to 0.
      ```
      [isis](cmdqueryname=isis) [ process-id process-id-value ] [ipv6 prefix-attributes node-disable](cmdqueryname=ipv6+prefix-attributes+node-disable)
      ```
   5. Return to the system view.
      ```
      [quit](cmdqueryname=quit)
      ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display isis lsdb verbose**](cmdqueryname=display+isis+lsdb+verbose) command to check information about the extended prefix attribute flag of IPv6 IS-IS.