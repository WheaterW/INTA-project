Configuring an Advanced ACL
===========================

Configuring an Advanced ACL

#### Context

Advanced ACLs give more flexibility and functionality than basic ACLs, allowing you to filter packets more accurately. For example, with advanced ACLs, you can define packet filtering rules based on information such as source and destination IPv4 addresses, IP protocol types, TCP source and destination port numbers, UDP source and destination port numbers, fragment information, and time ranges.

To match multiple source and destination IPv4 addresses using an advanced ACL, configure an ACL IPv4 address pool. This helps reduce configuration workloads. After an ACL IPv4 address pool is configured, you only need to configure an ACL rule with a specified ACL IPv4 address pool name (*pool-name*) to match multiple IPv4 addresses.

To match multiple source and destination port numbers using an advanced ACL, configure an ACL port pool. This helps reduce configuration workloads. After an ACL port pool is configured, you only need to configure an ACL rule with a specified ACL port pool name (*pool-name*) to match multiple port numbers.

**When ACL rules are configured:**

* If the specified rule ID already exists and the new rule conflicts with the original, the original is replaced.
* Matching stops for a packet once the packet matches a rule in an ACL.
* Many services that are not configured with ACL rules also occupy ACL resources. You can run the [**display system tcam service brief**](cmdqueryname=display+system+tcam+service+brief) command to check ACL resources occupied by services.

**When ACL rules are deleted:** The [**undo rule**](cmdqueryname=undo+rule) command can delete an ACL rule even if this rule is referenced. Before deleting a rule, run the [**display current-configuration | include acl**](cmdqueryname=display+current-configuration+%7C+include+acl) command to check whether the rule is being referenced.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an advanced ACL. You can create a numbered or named advanced ACL.
   
   
   * Create a numbered advanced ACL and enter its view.
     ```
     [acl](cmdqueryname=acl+number) [ number ] advance-acl-number 
     ```
     
     The number of an advanced ACL ranges from 3000 to 3999.
   * Create a named advanced ACL and enter its view.
     
     ```
     [acl name](cmdqueryname=acl+name+advance+number) advance-acl-name [ advance | [ number ] advance-acl-number ] 
     ```
3. (Optional) Configure an ACL step.
   
   
   ```
   [step](cmdqueryname=step) step-value
   ```
   
   
   
   The default ACL step is 5. Change the step value as required.
4. (Optional) Configure a description for the basic ACL.
   
   
   ```
   [description](cmdqueryname=description) text
   ```
   
   The ACL description helps you understand and remember the functions or purpose of the ACL.
5. (Optional) Configure an ACL IPv4 address pool.
   1. Create an ACL IPv4 address pool and enter its view.
      
      
      ```
      [acl ip-pool](cmdqueryname=acl+ip-pool) pool-name
      ```
   2. Add an IPv4 address to the ACL IPv4 address pool.
      
      
      ```
      [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
      ```
6. (Optional) Configure an ACL port pool.
   1. Create an ACL port pool and enter its view.
      
      
      ```
      [acl port-pool](cmdqueryname=acl+port-pool) pool-name
      ```
   2. Run one or more of the following commands to add a port number to the ACL port pool.
      
      
      ```
      { eq | lt | gt } begin-port-number
      ```
      ```
      [range](cmdqueryname=range) begin-port-number end-port-number
      ```
7. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Run either of the following commands to enter the advanced ACL view.
   
   
   ```
   [acl](cmdqueryname=acl+number) [ number ] advance-acl-number
   ```
   ```
   [acl name](cmdqueryname=acl+name) advance-acl-name
   ```
9. Configure a rule for the advanced ACL. Run the following commands based on the protocol type:
   
   
   * When *protocol* is specified as UDP, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+udp+dscp+af11+af12+af13+af21+af22+af23) [ rule-id ] [ name rule-name ] { permit | deny } { udp | 17 } [ [ dscp { dscp | af11 | af12 | af13 | af21 | af22 | af23 | af31 | af32 | af33 | af41 | af42 | af43 | cs1 | cs2 | cs3 | cs4 | cs5 | cs6 | cs7 | default | ef } | [ tos { tos | max-reliability | max-throughput | min-delay | min-monetary-cost | normal } | precedence { precedence | critical | flash | flash-override | immediate | internet | network | priority | routine } ] * ] | { destination { destination-ip-address { destination-wildcard | 0 | des-netmask } | any } | destination-pool destination-pool-name } | { destination-port { range { port-number | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } { port-number | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } | { gt | lt | eq } { port-number | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } } | destination-port-pool destination-port-pool-name } | fragment-type fragment | { source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | source-pool source-pool-name } | { source-port { range { port-number | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } { port-number | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } | { gt | lt | eq } { port-number | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } } | source-port-pool source-port-pool-name } | time-range time-name | ttl { { gt | lt | eq | neq } begin-ttlvalue | range begin-ttlvalue end-ttlvalue } | vpn-instance vpn-instance-name | logging ] *
     ```
   * When *protocol* is specified as TCP, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+tcp+dscp+af11+af12+af13+af21+af22+af23) [ rule-id ] [ name rule-name ] { permit | deny } { tcp | 6 } [ [ dscp { dscp | af11 | af12 | af13 | af21 | af22 | af23 | af31 | af32 | af33 | af41 | af42 | af43 | cs1 | cs2 | cs3 | cs4 | cs5 | cs6 | cs7 | default | ef } | [ precedence { precedence | critical | flash | flash-override | immediate | internet | network | priority | routine } | tos { tos | max-reliability | max-throughput | min-delay | min-monetary-cost | normal } ] * ] | { destination { destination-ip-address { destination-wildcard | 0 | des-netmask } | any } | destination-pool destination-pool-name } | { destination-port { range { port-number | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } { port-number | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } | { gt | lt | eq } { port-number | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } } | destination-port-pool destination-port-pool-name } | fragment-type fragment | { source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | source-pool source-pool-name } | { source-port { range { port-number | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } { port-number | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } | { gt | lt | eq } { port-number | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } } | source-port-pool source-port-pool-name } | tcp-flag { tcp-flag [ mask mask-value ] | established | { ack [ fin | psh | rst | syn | urg ] * } | { fin [ ack | psh | rst | syn | urg ] * } | { psh [ fin | ack | rst | syn | urg ] * } | { rst [ fin | psh | ack | syn | urg ] * } | { syn [ fin | psh | rst | ack | urg ] * } | { urg [ fin | psh | rst | syn | ack ] * } } | ttl { { gt | lt | eq | neq } begin-ttlvalue | range begin-ttlvalue end-ttlvalue } | vpn-instance vpn-instance-name | time-range time-name | logging ] *
     ```
   * When *protocol* is specified as ICMP, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+icmp+dscp+af11+af12+af13+af21+af22+af23) [ rule-id ] [ name rule-name ] { permit | deny } { icmp | 1 } [ [ dscp { dscp | af11 | af12 | af13 | af21 | af22 | af23 | af31 | af32 | af33 | af41 | af42 | af43 | cs1 | cs2 | cs3 | cs4 | cs5 | cs6 | cs7 | default | ef } | [ tos { tos | max-reliability | max-throughput | min-delay | min-monetary-cost | normal } | precedence { precedence | critical | flash | flash-override | immediate | internet | network | priority | routine } ] * ] | { destination { destination-ip-address { destination-wildcard | 0 | des-netmask } | any } | destination-pool destination-pool-name } | [ fragment-type fragment ] | icmp-type { icmp-name | icmp-type [ icmp-code ] } | { source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | source-pool source-pool-name } | time-range time-name | ttl { { gt | lt | eq | neq } begin-ttlvalue | range begin-ttlvalue end-ttlvalue } | vpn-instance vpn-instance-name | logging ] *
     ```
   * When *protocol* is specified as IGMP, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+igmp+dscp+af11+af12+af13+af21+af22+af23) [ rule-id ] [ name rule-name ] { permit | deny } { igmp | 2 } [ [ dscp { dscp | af11 | af12 | af13 | af21 | af22 | af23 | af31 | af32 | af33 | af41 | af42 | af43 | cs1 | cs2 | cs3 | cs4 | cs5 | cs6 | cs7 | default | ef } | [ tos { value | max-reliability | max-throughput | min-delay | min-monetary-cost | normal } | precedence { precedence | critical | flash | flash-override | immediate | internet | network | priority | routine } ] * ] | { destination { destination-ip-address { destination-wildcard | 0 | des-netmask } | any } | destination-pool destination-pool-name } | fragment-type fragment | { source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | source-pool source-pool-name } | time-range time-name | ttl { { gt | lt | eq | neq } begin-ttlvalue | range begin-ttlvalue end-ttlvalue } | vpn-instance vpn-instance-name | logging ] *
     ```
   * When *protocol* is specified as a protocol other than TCP, UDP, ICMP, and IGMP, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+zero+gre+ip+ipinip+ospf+dscp+af11+af12) [ rule-id ] [ name rule-name ] { permit | deny } { zero | protocol | gre | ip | ipinip | ospf | 7-16 | 18-255 } [ [ dscp { dscp | af11 | af12 | af13 | af21 | af22 | af23 | af31 | af32 | af33 | af41 | af42 | af43 | cs1 | cs2 | cs3 | cs4 | cs5 | cs6 | cs7 | default | ef } | [ tos { value | max-reliability | max-throughput | min-delay | min-monetary-cost | normal } | precedence { precedence | critical | flash | flash-override | immediate | internet | network | priority | routine } ] * ] | { destination { destination-ip-address { destination-wildcard | 0 | des-netmask } | any } | destination-pool destination-pool-name } | fragment-type fragment | { source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | source-pool source-pool-name } | time-range time-name | ttl { { gt | lt | eq | neq } begin-ttlvalue | range begin-ttlvalue end-ttlvalue } | vpn-instance vpn-instance-name | logging ] *
     ```
   
   
   
   In this example, only one permit or deny rule is configured. In actual configuration, you can configure multiple ACL rules and decide the matching order of the rules according to service requirements.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To configure a time-based advanced ACL, you must create a time range. For details, see [Creating a Time Range in Which an ACL Takes Effect](vrp_acl_cfg_0009.html).
   
   When a rule is configured for an advanced ACL:
   * If a destination IPv4 address, destination port number, source IPv4 address, and source port number are specified by **destination**, **destination-port**, **source**, and **source-port** respectively, the system filters only packets with the specified destination IPv4 address, destination port number, source IPv4 address, and source port number.
   * If all destination and source IPv4 addresses are specified by **any**, the system does not check packets' destination or source IPv4 addresses, and considers that all packets have matched the rule and directly takes an action (**deny** or **permit**) on the packets.
   * If **time-range** is specified, the specified time range name must exist. Otherwise, the ACL rule configuration fails.
10. (Optional) Configure a description for the ACL rule.
    
    
    ```
    [rule](cmdqueryname=rule+description) rule-id description destext
    ```
    
    The ACL rule description helps you understand and remember the functions or purpose of the ACL rule.
    
    You must create a rule before you can configure a description for it.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Example

* Configure a filtering rule for ICMP packets based on the source IPv4 address (host address) and destination IPv4 address segment.
  
  To permit ICMP packets from a host and destined for a network segment, configure a rule in an ACL. For example, to permit ICMP packets from the host at 192.168.1.3 and destined for the network segment 192.168.2.0/24, configure the following rule in ACL 3001.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl 3001
  [*HUAWEI-acl4-advance-3001] rule permit icmp source 192.168.1.3 0 destination 192.168.2.0 0.0.0.255
  [*HUAWEI-acl4-advance-3001] quit
  [*HUAWEI] commit
  ```
* Configure a filtering rule for TCP packets based on the TCP destination port number, source IPv4 address (host address), and destination IPv4 address segment.
  
  To prohibit Telnet connections between a specified host and the hosts on a network segment, configure a rule in an advanced ACL. For example, to prohibit Telnet connections between the host at 192.168.1.3 and hosts on the network segment 192.168.2.0/24, configure the following rule in the advanced ACL **deny-telnet**.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl name deny-telnet
  [*HUAWEI-acl4-advance-deny-telnet] rule deny tcp destination-port eq telnet source 192.168.1.3 0 destination 192.168.2.0 0.0.0.255
  [*HUAWEI-acl4-advance-deny-telnet] quit
  [*HUAWEI] commit
  ```
  
  To prohibit the specified hosts from accessing web pages (HTTP is used to access web pages, and the TCP port number is 80), configure rules in an advanced ACL. For example, to prohibit hosts 192.168.1.3 and 192.168.1.4 from accessing web pages, configure the following rules in ACL **no-web** and configure the description "Web access restrictions" for the ACL.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl name no-web
  [*HUAWEI-acl4-advance-no-web] description Web access restrictions
  [*HUAWEI-acl4-advance-no-web] rule deny tcp destination-port eq 80 source 192.168.1.3 0
  [*HUAWEI-acl4-advance-no-web] rule deny tcp destination-port eq 80 source 192.168.1.4 0
  [*HUAWEI-acl4-advance-no-web] quit
  [*HUAWEI] commit
  ```
* Configure a packet filtering rule for TCP packets based on the source IPv4 address segment and TCP flags.
  
  To implement unidirectional access control on a network segment, configure rules in an ACL. For example, to implement unidirectional access control on the network segment 192.168.2.0/24, configure the following rules in ACL 3002. In the rules, the hosts on 192.168.2.0/24 can only respond to TCP handshake packets, but cannot send the packets. Set the descriptions of the ACL rules to "Allow the ACK TCP packets through," "Allow the RST TCP packets through," and "Do not Allow the other TCP packet through."
  
  Configure two permit rules to permit the packets with the ACK or RST field being 1 from 192.168.2.0/24, and then configure a deny rule to reject other TCP packets from this network segment.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl 3002
  [*HUAWEI-acl4-advance-3002] rule permit tcp source 192.168.2.0 0.0.0.255 tcp-flag ack
  [*HUAWEI-acl4-advance-3002] quit
  [*HUAWEI] commit
  [~HUAWEI] acl 3002
  [*HUAWEI-acl4-advance-3002] display this   //If you do not specify an ID for a created rule, you can perform this step to obtain the rule ID allocated by the system and configure a description for the corresponding rule.
  #                                                                               
  acl number 3002                                                                 
   rule 5 permit tcp source 192.168.2.0 0.0.0.255 tcp-flag ack           //The rule ID allocated by the system is 5.
  #                                                                               
  return 
  [*HUAWEI-acl4-advance-3002] rule 5 description Allow the ACK TCP packets through
  [*HUAWEI-acl4-advance-3002] rule permit tcp source 192.168.2.0 0.0.0.255 tcp-flag rst
  [*HUAWEI-acl4-advance-3002] quit
  [*HUAWEI] commit
  [~HUAWEI] acl 3002
  [*HUAWEI-acl4-advance-3002] display this
  #                                                                               
  acl number 3002                                                                 
   rule 5 permit tcp source 192.168.2.0 0.0.0.255 tcp-flag ack                 
   rule 5 description Allow the ACK TCP packets through                 
   rule 10 permit tcp source 192.168.2.0 0.0.0.255 tcp-flag rst       //The rule ID allocated by the system is 10.
  #                                                                               
  return   
  [*HUAWEI-acl4-advance-3002] rule 10 description Allow the RST TCP packets through
  [*HUAWEI-acl4-advance-3002] rule deny tcp source 192.168.2.0 0.0.0.255
  [*HUAWEI-acl4-advance-3002] quit
  [*HUAWEI] commit
  [~HUAWEI] acl 3002
  [*HUAWEI-acl4-advance-3002] display this
  #                                                                               
  acl number 3002                                                                 
   rule 5 permit tcp source 192.168.2.0 0.0.0.255 tcp-flag ack                 
   rule 5 description Allow the ACK TCP packets through                 
   rule 10 permit tcp source 192.168.2.0 0.0.0.255 tcp-flag rst                
   rule 10 description Allow the RST TCP packets through                
   rule 15 deny tcp source 192.168.2.0 0.0.0.255       //The rule ID allocated by the system is 15.
  #                                                                               
  return   
  [*HUAWEI-acl4-advance-3002] rule 15 description Do not Allow the other TCP packet through
  [*HUAWEI-acl4-advance-3002] quit
  [*HUAWEI] commit
  ```
  
  You can specify the **established** parameter to permit the packets with the ACK or RST field being 1 from 192.168.2.0/24, and configure a deny rule to reject other TCP packets from this network segment.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl 3002
  [*HUAWEI-acl4-advance-3002] rule permit tcp source 192.168.2.0 0.0.0.255 tcp-flag established
  [*HUAWEI-acl4-advance-3002] rule 5 description Allow the Established TCP packets through
  [*HUAWEI-acl4-advance-3002] rule deny tcp source 192.168.2.0 0.0.0.255
  [*HUAWEI-acl4-advance-3002] rule 10 description Do not Allow the other TCP packet through
  [*HUAWEI-acl4-advance-3002] quit
  [*HUAWEI] commit
  [~HUAWEI] acl 3002
  [*HUAWEI-acl4-advance-3002] display this
  #                                                                                                                                   
  acl number 3002                                                                                                                     
   rule 5 permit tcp source 192.168.2.0 0.0.0.255 tcp-flag established                                                                
   rule 5 description Allow the Established TCP packets through                                                                       
   rule 10 deny tcp source 192.168.2.0 0.0.0.255                                                                                      
   rule 10 description Do not Allow the other TCP packet through                                                                      
  #                                                                                                                                   
  return
  ```

#### Verifying the Configuration

Run the [**display acl**](cmdqueryname=display+acl+name+all) { *advance-acl-number* | **name** *advance-acl-name* | **all** } command to check the configuration of the advanced ACL.


#### Follow-up Procedure

Apply the advanced ACL to a service module so that the advanced ACL rules can be delivered and take effect.