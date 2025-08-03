Configuring NTP Access Authority
================================

Configuring NTP Access Authority

#### Context

When an NTP access request reaches the local end, access authority is matched against the following access permissions in sequence: peer, server, synchronization, query, and limited, and peer has the maximum access permission.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a basic ACL.
   
   
   * Create a basic IPv4 ACL.
     ```
     [acl](cmdqueryname=acl) [ number] basic-acl-number
     ```
   * Create a basic ACL6.
     ```
     [acl ipv6](cmdqueryname=acl+ipv6) [ number] basic-acl6-number
     ```
3. Configure an ACL rule.
   
   
   * Configure a basic ACL rule.
     ```
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment-type fragment | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
     ```
   * Configure a basic ACL6 rule.
     ```
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment | source { source-ipv6-address { prefix-length | source-wildcard } | source-ipv6-address/prefix-length | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
     ```Check the ACL rule configuration.
   * If a source IP address is set to permit in the ACL rule, packets originating from this address are permitted.
   * If a source IP address is set to deny in the ACL rule, packets originating from this address are denied.
   * If a source IP address does not match the ACL rule, packets originating from this address are denied.
   * If no rule exists in the ACL or the referenced ACL does not exist, packets from all source IP addresses are denied.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
6. Configure NTP access authority on the local device.
   
   
   ```
   [ntp access](cmdqueryname=ntp+access) { peer | query | server | synchronization | limited } { { acl-number | acl-name aclname } [ ipv6 { acl6-number | acl6-name acl6name } ] | ipv6 { acl6-number | acl6-name acl6name } [ { acl-number | acl-name aclname } ] }
   ```
   
   Determine the device to be configured based on the site requirements. For details, see [Table 1](#EN-US_TASK_0000001563995629__tab_dc_vrp_ntp_cfg_001301).
   
   **Table 1** Description of the NTP access authority
   | NTP Operating Mode | Type of Restriction | Configuration Object |
   | --- | --- | --- |
   | NTP client/server mode or NTP manycast mode | Clock synchronization from the server to the client | Client |
   | Clock synchronization request to be processed by the server | Server |
   | NTP peer mode | Clock synchronization between the symmetric active peer and symmetric passive peer | Symmetric active end |
   | Clock synchronization request to be processed by the symmetric passive peer | Symmetric passive end |
   | NTP multicast mode | Clock synchronization between the client and server | NTP multicast client |
   | NTP broadcast mode | Clock synchronization between the client and server | NTP broadcast client |
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```