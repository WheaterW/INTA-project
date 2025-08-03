(Optional) Configuring Telnet Access Control
============================================

An ACL can be configured to allow only specified clients to access a Telnet server.

#### Context

When a device functions as a Telnet server, you can configure an ACL to allow only the clients that meet the rules specified in the ACL to access the Telnet server.

Perform the following steps on the device that functions as a Telnet server:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   The ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* or [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** **fragment** | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
   
   
   
   A rule is configured for the ACL.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**telnet server acl**](cmdqueryname=telnet+server+acl){ *acl4name* | *acl4num* } or [**telnet ipv6 server acl**](cmdqueryname=telnet+ipv6+server+acl){ *acl6name* | *acl6num* }
   
   
   
   A Telnet ACL is configured.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.