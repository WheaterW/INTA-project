Configuring TFTP Access Control
===============================

An ACL can be configured to allow the TFTP client to access specified TFTP servers.

#### Context

An ACL is a set of sequential rules. These rules are described based on source addresses, destination addresses, and port numbers of packets. ACL rules are used to filter packets. After ACL rules are applied to a device, the device permits or denies packets based on the ACL rules.

Multiple rules can be defined for one ACL. ACL rules are classified as interface, basic, or advanced ACL rules based on their functions.

Perform the following steps on the Router that functions as a TFTP client:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl) *acl-number* or *acl-number*
   
   
   
   The basic ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ [ **fragment** | **fragment-type** *fragment-type-name* ] | **logging** | **source** { *source-ip-address source-wildcard* | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
   
   
   
   An ACL rule is configured.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Configure ACL to control the TFTP client's access to TFTP servers.
   
   
   * For IPv4
     
     Run [**tftp-server acl**](cmdqueryname=tftp-server+acl) { *acl-number* | *acl-name* } to apply the ACL to the TFTP client to control its access to TFTP servers.
   * For IPv6
     
     Run [**tftp-server ipv6 acl**](cmdqueryname=tftp-server+ipv6+acl) { *acl-number* | *acl-name* } to apply the ACL to the TFTP client to control its access to TFTP servers.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.