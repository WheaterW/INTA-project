Adjusting Forwarding Parameters
===============================

Parameters associated with PIM forwarding include the interval for sending Join/Prune messages, holdtime carried by a Join/Prune message, policy for filtering Join/Prune messages, and lan-delay and override-interval carried by a Hello message.

#### Context

Join messages indicate that a multicast Router requires upstream devices to forward IPv6 multicast data, and Prune messages indicate that a multicast Router requires upstream devices to stop forwarding IPv6 multicast data.

* After the first member joins a multicast group, the Router sends a Join message to request its upstream Router to forward required IPv6 multicast data.
  
  On an IPv6 PIM-SM network, the Router periodically sends Join messages to prevent RPT branches from being pruned off due to timeout.
* After the last member of a group leaves, the Router sends a Prune message to request its upstream Router to perform the prune action. If other downstream Routers still need to receive multicast data for the group, they must send Join messages to the upstream Router within the set **override-interval** to override the prune action.
  
  A Hello message carries the **lan-delay** and **override-interval** attributes.
  
  + **lan-delay** specifies the delay in transmitting Prune messages on a shared network segment.
  + **override-interval** specifies the interval for overriding the prune action.
  
  The relationship between **lan-delay**, **override-interval**, and PPT is: **lan-delay** + **override-interval** = PPT. The Prune-Pending Timer (PPT) indicates the period from the time when the Router receives a Prune message from a downstream interface to the time when the Router performs the prune action. If the Router receives a Join message from the downstream interface within the PPT, the Router does not perform the prune action.

You can set forwarding parameters either globally or on an interface.

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

To enhance the security of IPv6 PIM forwarding, configure a source address- and group address-based policy for filtering Join/Prune messages on an interface.


#### Procedure

* Set forwarding parameters globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
     
     
     
     The IPv6 PIM view is displayed.
  3. Run [**timer join-prune**](cmdqueryname=timer+join-prune) *interval*
     
     
     
     The interval for the interfaces of the Router to send Join/Prune messages is set.
  4. Run [**holdtime join-prune**](cmdqueryname=holdtime+join-prune) *interval*
     
     
     
     The value of the holdtime field carried by a sent Join/Prune message is set.
     
     After receiving a Join/Prune message from a downstream interface, an upstream Router determines the period for keeping the join or prune state of the downstream interface based on the value of the holdtime field in the Join/Prune message.
     
     In most cases, the value of the holdtime is 3.5 times the interval for sending Join/Prune messages.
  5. Run [**hello-option lan-delay**](cmdqueryname=hello-option+lan-delay) *interval*
     
     
     
     The value of the lan-delay field carried by a sent Hello message is set.
     
     When the values of **lan-delay** fields carried by Hello messages sent by the interfaces on a shared network segment are different, the largest one of these values is used.
  6. Run [**hello-option override-interval**](cmdqueryname=hello-option+override-interval) *interval*
     
     
     
     The value of the override-interval field carried by a sent Hello message is set.
     
     When the values of override-interval fields carried by Hello messages sent by the interfaces on a shared network segment are different, the maximum one of these values is used.
  7. Run [**neighbor-check**](cmdqueryname=neighbor-check) { **receive** | **send** }
     
     
     
     The neighbor check function is configured.
     
     You can specify both **receive** and **send** to enable the IPv6 PIM neighbor check function for both the received and sent Join/Prune messages and Assert messages.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set forwarding parameters for a specific interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic or an advanced ACL6 as needed.
     
     
     + Configure a basic ACL6.
       
       1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ]
          
          A basic ACL6 is created, and the basic ACL6 view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
          
          Rules are configured for the basic ACL6.
     + Configure an advanced ACL6.
       1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *advance-acl6-name* [ **advance** | [ **advance** ] **number** *advance-acl6-number* ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ]
          
          An advanced ACL6 is created, and the advanced ACL6 view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ipv6** [ **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
          
          Rules are configured for the advanced ACL6.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The IPv6 PIM interface view is displayed.
  5. Run [**pim ipv6 timer join-prune**](cmdqueryname=pim+ipv6+timer+join-prune) *interval*
     
     
     
     The interval at which the interface sends Join/Prune messages is set.
  6. Run [**pim ipv6 holdtime join-prune**](cmdqueryname=pim+ipv6+holdtime+join-prune) *interval*
     
     
     
     The value of the holdtime field carried by a Join/Prune message sent by the interface is set.
  7. Run [**pim ipv6 hello-option lan-delay**](cmdqueryname=pim+ipv6+hello-option+lan-delay) *interval*
     
     
     
     The value of the lan-delay field carried by a Hello message sent by the interface is set.
  8. Run [**pim ipv6 hello-option override-interval**](cmdqueryname=pim+ipv6+hello-option+override-interval) *interval*
     
     
     
     The value of the override-interval field carried by a Hello message sent by the interface is set.
  9. Run [**pim ipv6 join-policy**](cmdqueryname=pim+ipv6+join-policy) { { *advanced-acl6-number* | **acl6-name** *acl6-name* } | **asm** { *basic-acl6-number* | **acl6-name** *acl6-name* } | **ssm** { *advanced-acl6-number* | **acl6-name** *acl6-name* } }
     
     
     
     A policy for filtering Join messages contained in Join/Prune messages is configured.
     
     If **asm** is specified, run the [**rule**](cmdqueryname=rule) command in the basic ACL view and set the **source** parameter to the multicast group address range of join information.
     
     If **ssm** is specified, run the [**rule**](cmdqueryname=rule) command in the advanced ACL view, set the **source** parameter to the multicast source address range of join information, and set the **destination** parameter to the multicast group address range of join information.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a Join message's join information matches an ACL rule and the action is **permit**, the device permits this message.
     + If a Join message's join information matches an ACL rule and the action is **deny**, the device denies this message.
     + If a Join message's join information does not match any ACL rule, the device denies this message.
     + If a specified ACL does not exist or does not contain rules, the device denies all Join messages that contain join information.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.