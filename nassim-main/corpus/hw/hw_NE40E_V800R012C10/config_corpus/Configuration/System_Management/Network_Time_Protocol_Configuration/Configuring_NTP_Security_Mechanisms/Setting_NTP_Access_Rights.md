Setting NTP Access Rights
=========================

When receiving an access request packet, the NTP server matches the request packet with the access right in descending order (from peer, server, synchronization, query to limited). The first matched right takes effect.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an ACL to filter network administrators.
   
   
   * To create a basic IPv4 ACL and enter the basic ACL view, run the [**acl**](cmdqueryname=acl) *basic-acl-number* command.
   * To create a basic IPv6 ACL and enter the basic ACL6 view, run the [**acl ipv6**](cmdqueryname=acl+ipv6) *basic-acl-number* command.
3. Add a rule to the ACL.
   
   
   * To create a rule for the basic ACL, run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* command.
   * To create a rule for the basic ACL6, run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* command.![](../../../../public_sys-resources/note_3.0-en-us.png) Before configuring access control rights in an ACL, check the ACL rule configuration.
   * If the ACL rule of a source IP address is set to permit, packets from the source IP address are permitted.
   * If the ACL rule of a source IP address is set to deny, packets from the source IP address are denied.
   * If a source IP address is not in an ACL rule, packets from the source IP address are denied.
   * If no rule exists in the ACL or the referenced ACL does not exist, packets from all source IP addresses are denied.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**ntp-service access**](cmdqueryname=ntp-service+access) { **peer** | **query** | **server** | **synchronization** | **limited** } { { *acl-number* | **acl-name** *acl-name* } | **ipv6** { *acl6-number* | **acl6-name** *acl6-name* } } \*
   
   
   
   Access rights for the NTP service on the local Router are configured.
   
   Before specifying an ACL number, make sure you have already created and configured this ACL.
   
   You can configure the [**ntp-service access**](cmdqueryname=ntp-service+access) command depending on the actual situation. [Table 1](#EN-US_TASK_0000001801088658__tab_dc_vrp_ntp_cfg_001301) shows the detailed NTP access rights.
   
   **Table 1** Description of the NTP access rights
   | NTP Operation Mode | Limited NTP Query | Supported Devices |
   | --- | --- | --- |
   | Unicast NTP server/client mode | Synchronizing the client with the server | Client |
   | Unicast NTP server/client mode | Clock synchronization request from the client | Server |
   | NTP peer mode | Clock synchronization with each other | Symmetric active end |
   | NTP peer mode | Clock synchronization request from the active end | Symmetric passive end |
   | NTP multicast mode | Synchronizing the client with the server | NTP multicast client |
   | NTP broadcast mode | Synchronizing the client with the server | NTP broadcast client |
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.