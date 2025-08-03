Configuring Passive BFD Echo
============================

This section describes how to configure passive BFD echo to implement interworking between devices that support the echo function. Passive BFD echo applies only to single-hop BFD sessions.

#### Usage Scenario

BFD provides the asynchronous detection mode. An auxiliary function of the asynchronous mode is the echo function, which must work with the asynchronous mode. When the echo function is activated, the local system sends a BFD control packet and the remote system loops the packet back through the forwarding channel. If several consecutive echo packets are not received, the session is declared to be down.

If a device that supports the echo function is deployed on a network, you can enable passive BFD echo for interworking with other vendors' devices.


#### Pre-configuration Tasks

Before configuring passive BFD echo, complete the following tasks:

* Enable BFD globally.
* (Optional) Create an ACL.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   The basic ACL view is displayed.
3. (Optional) Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
   
   
   
   An ACL rule is created.
4. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   The BFD view is displayed.
6. Run [**echo-passive**](cmdqueryname=echo-passive) { **all** | **acl** *basic-acl-number* }
   
   
   
   Passive BFD echo is enabled.
   
   
   
   * To enable passive echo for all BFD sessions, specify the **all** parameter.
   * To enable passive echo for BFD sessions that match a configured ACL rule, specify the **acl** parameter. Passive echo is enabled for the BFD control packets that are permitted by the ACL, not for the BFD control packets that are denied by the ACL or do not match any ACL rules.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If an ACL rule is created or modified after a BFD session goes up through negotiations, this ACL rule can take effect only after the BFD session goes up from down or the parameters of the BFD session are modified.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.