Configuring a Traffic Policy
============================

In application-aware traffic steering scenarios, a device searches the FIB table for a mapping policy based on the destination address of a packet, and then determines the packet forwarding path based on the mapping policy ID and APN ID. To implement application-aware traffic steering, configure a traffic policy first.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a traffic classification rule.
   1. Run either of the following commands to create an ACL or ACL6 and enter its view:
      
      
      * For a basic ACL (ACL number ranging from 2000 to 2999), run the [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command.
      * For an advanced ACL (ACL number ranging from 3000 to 3999), run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command.
      * For a basic ACL6 (ACL number ranging from 2000 to 2999), run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* [ **basic** ] | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ] command.
      * For an advanced ACL6 (ACL number ranging from 3000 to 3999), run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *advance-acl6-name* [ **advance** ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ] command.
   2. Run either of the following commands to create an ACL or ACL6 rule:
      
      
      * For a basic ACL (ACL number ranging from 2000 to 2999), run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **logging** ] \* command.
      * For an advanced ACL (ACL number ranging from 3000 to 3999), the command to be run differs for different protocols.
        
        [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **tcp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | { **destination-port** *operator* *port-number* | **destination-port-pool** *destination-port-pool-name* } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | { **source-port** *operator* *port-number* | **source-port-pool** *source-port-pool-name* } | { **tcp-flag** | **syn-flag** } { *tcp-flag* [ **mask** *mask-value* ] | **established** |{ **ack** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **fin** [ **ack** | **psh** | **rst** | **syn** | **urg** ] \* } | { **psh** [ **fin** | **ack** |**rst** |**syn** | **urg** ] \* } | { **rst** [ **fin** | **psh** | **ack** | **syn** | **urg** ] \* } | { **syn** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **urg** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } } |**time-range** *time-name* | **ttl** *ttl-operation* *ttl-value* | **packet-length** *length-operation* *length-value* ] \*
        
        The preceding configuration uses TCP as the example protocol. The configurations of other protocols are similar. For details, see the **rule (Advanced ACL view) (UDP)**, **rule (Advanced ACL view) (gre-igmp-ip-ipinip-ospf)**, and **rule (advanced ACL view) (ICMP)** commands in the *Command Reference* of the device.
      * For a basic ACL6 (ACL number ranging from 2000 to 2999), run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address/prefix-length* | **any** } | **time-range** *time-name* | [{ **vpn-instance** | **vpn6-instance** } *vpn-instance-name* | **vpn-instance-any** ]]\* command.
      * For an advanced ACL6 (ACL number ranging from 3000 to 3999), the command to be run varies according to protocols.
        
        [**rule**](cmdqueryname=rule+name+permit+deny+tcp+destination+any+destination-pool) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **tcp** | *6* } [ { **destination** { *destination-ipv6-address* *prefix-length* | *dest-ipv6-addr-prefix* | **any** } | **destination-pool** *destination-pool-name* } | **destination-port** { **range** { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } | { **gt** | **lt** | **eq** | **neq** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } } | **fragment** | { **source** { *source-ipv6-address* *prefix-length* | *src-ipv6-addr-prefix* | **any** } | **source-pool** *source-pool-name* } | **source-port** { **range** { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } | { **gt** | **lt** | **eq** | **neq** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } } | **time-range** *time-name* | [ **dscp** *dscp-value* | [ **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } | **tos** { *value* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } ] \* ] | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **tcp-flag** { *tcp-flag* [ **mask** *mask-value* ] | **established** | { **ack** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **fin** [ **ack** | **psh** | **rst** | **syn** | **urg** ] \* } | { **psh** [ **fin** | **ack** | **rst** | **syn** | **urg** ] \* } | { **rst** [ **fin** | **psh** | **ack** | **syn** | **urg** ] \* } | { **syn** [ **fin** | **psh** | **rst** | **ack** | **urg** ] \* } | { **urg** [ **fin** | **psh** | **rst** | **syn** | **ack** ] \* } } ] \*
        
        The preceding configuration uses TCP as the example protocol. The configurations of other protocols are similar. For details, see [Configuring an Advanced ACL6 Rule](dc_vrp_acl6_cfg_0057.html).![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * Generally, ACL rule matching is based on source IP addresses. To specify multiple ACL rules, repeat [2.b](#EN-US_TASK_0000001244093088__substep_02).
      * In an ACL, rules that traffic is matched against are used based on the depth first rule (when **auto** is configured) or in the configuration order (when **config** is configured). By default, rules are matched based on the configuration order (with **config** configured).
        
        When an ACL rule is associated with an instance, the address wildcard of the ACL rule must be a subnet mask in which all binary 1s are consecutive and all binary 0s are consecutive. For example, 255.255.255.0 is allowed, but 255.0.255.0 is not.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
3. Configure a traffic classifier.
   1. Run the [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ] command to configure a traffic classifier and enter its view.
   2. Run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **acl** *acl-number* command to configure an ACL-based matching rule for MF traffic classification.
      
      
      
      To configure multiple ACL-based matching rules, repeat this step.
      
      For IPv6 packets, specify the keyword **ipv6**.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
4. Configure a traffic behavior.
   1. Run the [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name* command to configure a traffic behavior and enter its view.
   2. Run the [**remark apn-id-ipv6 instance**](cmdqueryname=remark+apn-id-ipv6+instance) *apn-instance-name* command to configure the device to add an APN ID to an IPv6 packet.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
5. Configure a traffic policy.
   1. Run the [**traffic policy**](cmdqueryname=traffic+policy) *policy-name* command to configure a traffic policy and enter its view.
   2. Run the [**classifier**](cmdqueryname=classifier+behavior) *classifier-name* **behavior** *behavior-name* command to configure a traffic classifier and behavior for the traffic policy.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
6. Apply the traffic policy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After an APN ID is generated based on a local ACL policy, the APN ID can be added to packets only if routes are recursed to SRv6 BE or SRv6 TE Policies.
   
   
   
   Apply the traffic policy to an interface.
   
   
   
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
   2. Run the [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound** [ **link-layer** | **all-layer** | **mpls-layer** ] command to apply the traffic policy to the interface.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   
   
   
   Apply the traffic policy to a VPN instance.
   
   
   
   1. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
   2. Run the **[**traffic-policy**](cmdqueryname=traffic-policy)** **policy-name** **[**network**](cmdqueryname=network)** **[**inbound**](cmdqueryname=inbound)** command to apply the traffic policy in the VPN instance view.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.