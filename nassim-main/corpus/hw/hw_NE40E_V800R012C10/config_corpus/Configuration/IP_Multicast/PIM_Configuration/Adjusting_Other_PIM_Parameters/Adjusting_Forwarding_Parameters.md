Adjusting Forwarding Parameters
===============================

Parameters associated with PIM forwarding include the interval for sending Join/Prune messages, holdtime carried by a Join/Prune message, policy for filtering Join/Prune messages, and lan-delay and override-interval carried by a Hello message.

#### Context

Join messages indicate that a multicast Router requires upstream devices to forward multicast data, and Prune messages indicate that a multicast Router requires upstream devices to stop forwarding multicast data.

* After the first member joins a multicast group, the Router sends a Join message through the upstream interface to require the upstream Router to forward multicast packets to this network segment.
  
  On a PIM-SM network, the Router periodically sends Join messages to prevent rendezvous point tree (RPT) branches from being pruned off due to timeout.
* After the last member of a group leaves, the Router sends a Prune message through the upstream interface to request the upstream router to perform the prune action. If other downstream Routers exist on this network segment, they must send the Join message to override the prune action.
  
  A Hello message carries the **lan-delay** and **override-interval** attributes.
  
  + **lan-delay** specifies the delay in transmitting Prune messages on a shared network segment.
  + **override-interval** specifies the period allowed for overriding the prune action. If the Routers still need to receive the multicast data, they must send Join messages upstream within the override-interval.
  
  The relationship between **lan-delay**, **override-interval**, and PPT is: **lan-delay** + **override-interval** = PPT. The Prune-Pending Timer (PPT) indicates the period from the time when the Router receives a Prune message from a downstream interface to the time when the Router performs the prune action. If the downstream interface receives a Join message within the PPT, the prune action is canceled.

You can set forwarding parameters either globally or on an interface.

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If no interface-specific configuration is performed for an interface, the interface uses the global configuration.

#### Procedure

* Set forwarding parameters globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**timer join-prune**](cmdqueryname=timer+join-prune) *interval*
     
     
     
     An interval is set for all interfaces on the device to send Join/Prune messages.
  4. Run [**holdtime join-prune**](cmdqueryname=holdtime+join-prune) *interval*
     
     
     
     The holdtime is set for Join/Prune messages to be sent by all interfaces on the Router.
     
     An upstream Router determines the period for a downstream interface to hold the join or prune state based on the holdtime carried in the Join/Prune message received from the downstream interface.
  5. Run [**hello-option lan-delay**](cmdqueryname=hello-option+lan-delay) *interval*
     
     
     
     The lan-delay is set for Hello messages to be sent by all interfaces on the Router.
     
     If Router interfaces on a shared network segment have different lan-delay values, the maximum lan-delay value is used by negotiation.
  6. Run [**hello-option override-interval**](cmdqueryname=hello-option+override-interval) *interval*
     
     
     
     The override-interval is set for Hello messages to be sent by all interfaces on the Router.
     
     If Router interfaces on a shared network segment have different override-intervals, the maximum override-interval is used by negotiation.
  7. Run [**neighbor-check**](cmdqueryname=neighbor-check) { **receive** | **send** }
     
     
     
     The neighbor check function is configured.
     
     You can specify **receive** and **send** to enable the PIM neighbor check function for both received and sent Join/Prune and Assert messages.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set forwarding parameters for a specific interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic or an advanced ACL as needed.
     
     
     + Configure a basic ACL.
       
       1. Run the [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ] command to create a basic ACL and enter the corresponding ACL view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } command to configure a rule for the basic ACL.
     + Configure an advanced ACL.
       
       1. Run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command to create an advanced ACL and enter the corresponding ACL view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \* command to configure a rule for the advanced ACL.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The PIM interface view is displayed.
  5. Run [**pim timer join-prune**](cmdqueryname=pim+timer+join-prune) *interval*
     
     
     
     An interval is set for the interface to send Join/Prune messages.
  6. Run [**pim holdtime join-prune**](cmdqueryname=pim+holdtime+join-prune) *interval*
     
     
     
     The holdtime is set for Join/Prune messages to be sent by the interface.
  7. Run [**pim hello-option lan-delay**](cmdqueryname=pim+hello-option+lan-delay) *interval*
     
     
     
     The lan-delay is set for Hello messages to be sent by the interface.
  8. Run [**pim hello-option override-interval**](cmdqueryname=pim+hello-option+override-interval) *interval*
     
     
     
     The override-interval is set for Hello messages to be sent by the interface.
  9. Run [**pim join-policy**](cmdqueryname=pim+join-policy) { { *advanced-acl-number* | **acl-name** *acl-name* } | **asm** { *basic-acl-number* | **acl-name** *acl-name* } | **ssm** { *advanced-acl-number* | **acl-name** *acl-name* } }
     
     
     
     A policy is created for filtering join information in Join/Prune messages.
     
     The Router filters join information in Join/Prune messages based on source addresses or both source and group addresses.
     
     If **asm** is specified, run the [**rule**](cmdqueryname=rule) command in the basic ACL view and set the **source** parameter to the multicast group address range of join information.
     
     If **ssm** is specified, run the [**rule**](cmdqueryname=rule) command in the advanced ACL view, set the **source** parameter to the multicast source address range of join information, and set the **destination** parameter to the multicast group address range of join information.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a Join message's join information matches an ACL rule and the action is **permit**, the device permits this message.
     + If a Join message's join information matches an ACL rule and the action is **deny**, the device denies this message.
     + If a Join message's join information does not match any ACL rule, the device denies this message.
     + If a specified ACL does not exist or does not contain rules, the device denies all Join messages that contain join information.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.