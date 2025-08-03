Adjusting Neighbor Parameters
=============================

Devices establish neighbor relationships by exchanging Hello messages. PIM neighbor parameters include the interval for sending Hello messages, timeout period of a neighbor relationship, whether to deny a Hello message carrying the Generation ID option, and policy for filtering neighbors.

#### Context

You can set the interval for sending Hello messages and timeout period of a neighbor relationship either globally or on an interface.

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

#### Procedure

* Adjust neighbor parameters globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**timer hello**](cmdqueryname=timer+hello) *interval*
     
     
     
     The interval for sending Hello messages is set.
  4. Run [**hello-option holdtime**](cmdqueryname=hello-option+holdtime) *holdtimeValue*
     
     
     
     The neighbor holdtime carried in the PIM Hello messages to be sent is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The interval for a Router to send Hello messages must be shorter than the timeout period of neighbor relationships.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Adjust neighbor parameters for a specific interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL or a named ACL as needed.
     
     
     + Configure a basic numbered ACL.
       
       1. Run the [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ] command to create a basic numbered ACL and enter the corresponding ACL view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } command to configure a rule for the basic numbered ACL.
     + Configure a named ACL.
       
       1. Run the [**acl**](cmdqueryname=acl) **name** *acl-name* **basic** [ **match-order** { **auto** | **config** } ] command to create a named ACL and enter the corresponding ACL view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } command to configure a rule for the named ACL.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The PIM interface view is displayed.
  5. Run [**pim timer hello**](cmdqueryname=pim+timer+hello) *interval*
     
     
     
     The interval for the interface to send Hello messages is set.
  6. Run [**pim hello-option holdtime**](cmdqueryname=pim+hello-option+holdtime) *helloHoldTime*
     
     
     
     The neighbor holdtime carried in the PIM Hello messages to be sent is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The interval for an interface to send Hello messages must be shorter than the timeout period of neighbor relationships.
  7. Run [**pim require-genid**](cmdqueryname=pim+require-genid)
     
     
     
     The interface is configured to accept only Hello messages with Generation ID fields.
     
     After an interface on the Router is enabled with PIM-SM, the Router generates a random number as the Generation ID of the Hello message. If the status of the Router changes, a new Generation ID is generated. If the Router finds that the Hello messages received from PIM neighbors carry different Generation IDs, the Router considers that the PIM neighbor status changes.
  8. Run [**pim neighbor-policy**](cmdqueryname=pim+neighbor-policy) { *basic-acl-number* | **acl-name** *acl-name* }
     
     
     
     A neighbor filtering policy is configured.
     
     The neighbor filtering policy defines the range of valid neighbor addresses. The Router discards Hello messages received from the Routers that are not in this address range.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a peer matches an ACL and the action is **permit**, the local Router sets up a neighbor relationship with this peer.
     + If a peer matches an ACL and the action is **deny**, the local Router does not set up a neighbor relationship with this peer.
     + If a peer does not match any ACL rule, the local Router does not set up a neighbor relationship with this peer.
     + If a specified ACL does not exist or does not contain rules, the local Router does not set up neighbor relationships with any peers.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.