Adjusting Neighbor Parameters
=============================

Devices establish neighbor relationships by exchanging Hello messages. PIM neighbor parameters include the interval for sending Hello messages, neighbor holdtime, whether to deny Hello messages without the Generation ID option, and neighbor filtering policy.

#### Context

You can set the interval for sending Hello messages and neighbor holdtime as follows:

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

The following functions can be configured on interfaces to improve the security of IPv6 PIM neighbors:

* Deny Hello messages without the Generation ID option. If the Router finds that a Hello message received from a PIM neighbor contains a different generation ID, the Router considers that the status of the PIM neighbor changes.
* Configure a neighbor filtering policy to limit the range of valid neighbor addresses. The Router discards a Hello message received from a neighbor with the address beyond the set range.

#### Procedure

* Adjust neighbor parameters globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
     
     
     
     The IPv6 PIM view is displayed.
  3. Run [**timer hello**](cmdqueryname=timer+hello) *helloInterval*
     
     
     
     The interval for sending Hello messages is set.
  4. Run [**hello-option holdtime**](cmdqueryname=hello-option+holdtime) *holdtimeValue*
     
     
     
     The neighbor holdtime carried in the PIM Hello messages to be sent is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The interval at which the Router sends Hello messages must be shorter than the neighbor timeout period.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Adjust neighbor parameters for a specific interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL6 or a named ACL6 as needed.
     
     
     + Configure a basic numbered ACL6.
       
       1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ]
          
          A basic numbered ACL6 is created, and the basic numbered ACL6 view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
          
          Rules are configured for the basic numbered ACL6.
     + Configure a naming ACL6.
       1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) **name** *acl6-name* **basic** [ **match-order** { **auto** | **config** } ]
          
          A named ACL6 is created, and the named ACL6 view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
          
          Rules are configured for the named ACL6.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The IPv6 PIM interface view is displayed.
  5. Run [**pim ipv6 timer hello**](cmdqueryname=pim+ipv6+timer+hello) *interval*
     
     
     
     The interval at which the interface sends Hello messages is set.
  6. Run [**pim ipv6 hello-option holdtime**](cmdqueryname=pim+ipv6+hello-option+holdtime) *helloHoldTime*
     
     
     
     The neighbor holdtime carried in the PIM Hello messages to be sent is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The interval at which the Router sends Hello messages must be shorter than the neighbor holdtime.
  7. Run [**pim ipv6 require-genid**](cmdqueryname=pim+ipv6+require-genid)
     
     
     
     The interface is configured to accept the Hello messages with the Generation ID option and deny the Hello messages without the Generation ID option.
  8. Run [**pim ipv6 neighbor-policy**](cmdqueryname=pim+ipv6+neighbor-policy) { *basic-acl6-number* | **acl6-name** *acl6-name* }
     
     
     
     A neighbor filtering policy is configured.
     
     When being configured on an interface, the neighbor filtering function needs to be configured on the Routers that set up PIM neighbor relationships with this interface accordingly.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a peer matches an ACL and the action is **permit**, the local Router sets up a neighbor relationship with this peer.
     + If a peer matches an ACL and the action is **deny**, the local Router does not set up a neighbor relationship with this peer.
     + If a peer does not match any ACL rule, the local Router does not set up a neighbor relationship with this peer.
     + If a specified ACL does not exist or does not contain rules, the local Router does not set up neighbor relationships with any peers.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.