Configuring the Data Collection Mode
====================================

Configuring the Data Collection Mode

#### Prerequisites

Before the data collection mode is configured, an advanced ACL has been created using the [**acl**](cmdqueryname=acl) command in the system view. Only the following advanced ACL rules are supported. The ACL rules that are not supported cannot be delivered.

* Rule 1: TCP + destination IPv4 or IPv6 address
* Rule 2: TCP + destination IPv4 or IPv6 address + destination TCP port number
* Rule 3: TCP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address
* Rule 4: TCP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address + source TCP port number (no port range can be configured because exact match is used) + destination TCP port number
* Rule 5: TCP + any
* Rule 6: UDP + destination IPv4 or IPv6 address
* Rule 7: UDP + destination IPv4 or IPv6 address + destination UDP port number
* Rule 8: UDP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address
* Rule 9: UDP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address + source UDP port number (no port range can be configured because exact match is used) + destination UDP port number
* Rule 10: UDP + any

![](public_sys-resources/note_3.0-en-us.png) 

* The preceding advanced ACL rules 6 to 10 can be used to match only inner UDP packets encapsulated in VXLAN packets, but not ordinary UDP packets.
* For VXLAN packets, the preceding advanced ACL rules match the inner packets.
* In the IOAM function, the **deny** or **permit** action specified in an ACL rule does not take effect. Service flows are sampled for processing as along as they match the preceding advanced ACL rules.
* 5-tuple matching is supported. A destination port range can be configured, but a source port range cannot.
* The IOAM function takes effect only for ordinary TCP packets and VXLAN packets with inner TCP or UDP packets.
* An 8-byte probermarker field is added following the Layer 4 header (UDP/TCP) to identify an IOAM packet.


#### Procedure

1. Configure the encapsulation function on the encapsulation node.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the IOAM view.
      
      
      ```
      [ioam](cmdqueryname=ioam)
      ```
   3. Enter the IOAM profile view.
      
      
      ```
      [profile default](cmdqueryname=profile+default)
      ```
      
      
      
      By default, the device creates an IOAM profile named **default** after the IOAM view is created. This is the only profile supported by the device currently.
   4. Enter the IOAM policy view.
      
      
      ```
      [policy](cmdqueryname=policy) policy-id
      ```
      
      
      
      By default, no IOAM policy is created on the device. Currently, only one IOAM policy can be created on the device.
   5. (Optional) Configure description for the IOAM policy.
      
      
      ```
      [description](cmdqueryname=description) text
      ```
      
      
      
      By default, no description is configured for an IOAM policy.
   6. Configure the data collection mode.
      
      
      ```
      [action-type encapsulate](cmdqueryname=action-type+encapsulate)  [ service-type { trace | edge-to-edge | direct-export } ]
      ```
      
      
      
      By default, the data collection mode is trace mode.
   7. Configure IOAM packet matching rules.
      
      
      ```
      [acl](cmdqueryname=acl) [ ipv6 ] { acl-num | acl-name }
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      The device supports the configuration of both an advanced IPv4 ACL rule and an IPv6 ACL rule.
   8. Return to the IOAM profile view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   9. Return to the IOAM view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   10. Return to the system view.
       
       
       ```
       [quit](cmdqueryname=quit)
       ```
   11. Commit the configuration.
       
       
       ```
       [commit](cmdqueryname=commit)
       ```
2. Configure the transmission function on the transit node.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the IOAM view.
      
      
      ```
      [ioam](cmdqueryname=ioam)
      ```
   3. Enable the transmission function.
      
      
      ```
      [action-type](cmdqueryname=action-type) transit
      ```
      
      By default, this function is not configured.
   4. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   5. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
3. Configure the decapsulation function on the decapsulation node.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the IOAM view.
      
      
      ```
      [ioam](cmdqueryname=ioam)
      ```
   3. Enable the decapsulation function.
      
      
      ```
      [action-type](cmdqueryname=action-type) decapsulate
      ```
   4. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   5. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```