Configuring an Advanced ACL6
============================

Configuring an Advanced ACL6

#### Context

Advanced ACL6s give more flexibility and functionality than basic ACL6s, allowing you to filter packets more accurately. For example, with advanced ACL6s, you can define packet filtering rules based on information such as source and destination IPv6 addresses, IP protocol types, TCP source and destination port numbers, UDP source and destination port numbers, fragment information, and time ranges.

**When ACL6 rules are configured:**

* If the specified rule ID already exists and the new rule conflicts with the original, the original is replaced.
* Matching stops for a packet once the packet matches a rule in an ACL6.
* Many services that are not configured with ACL6 rules also occupy ACL6 resources. You can run the [**display system tcam service brief**](cmdqueryname=display+system+tcam+service+brief) command to check ACL6 resources occupied by services.

**When ACL6 rules are deleted:** The [**undo rule**](cmdqueryname=undo+rule) command can delete an ACL rule even if this rule is referenced. Before deleting a rule, run the [**display current-configuration | include acl**](cmdqueryname=display+current-configuration+%7C+include+acl) command to check whether the rule is being referenced.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an advanced ACL6. You can create a numbered or named advanced ACL6.
   
   
   * Create a numbered advanced ACL6 and enter its view.
     ```
     [acl ipv6](cmdqueryname=acl+ipv6+number) [ number ] advance-acl6-number 
     ```
     
     The number of an advanced ACL6 ranges from 3000 to 3999.
   * Create a named advanced ACL6 and enter its view.
     
     ```
     [acl ipv6 name](cmdqueryname=acl+ipv6+name+advance) advance-acl6-name [ advance ]
     ```
3. (Optional) Configure an ACL6 step.
   
   
   ```
   [step](cmdqueryname=step) step-value
   ```
   
   
   
   The default ACL6 step is 5. Change the step value as required.
4. (Optional) Configure a description for the basic ACL6.
   
   
   ```
   [description](cmdqueryname=description) text
   ```
   
   The ACL6 description helps you understand and remember the functions or purpose of the ACL6.
5. Configure a rule for the advanced ACL6. Run the following commands based on the protocol type:
   
   
   * When *protocol* is specified as UDP, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+udp+destination+any+destination-port+range) [ rule-id ] [ name rule-name ] { permit | deny } { udp | 17 } [ destination { destination-ipv6-address { prefix-length | destination-wildcard } | dest-ipv6-addr-prefix | any } | destination-port { range { port | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } { port | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } | { gt | lt | eq } { port | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } } | fragment | source { source-ipv6-address { prefix-length | source-wildcard } | src-ipv6-addr-prefix | any } | source-port { range { port | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } { port | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } | { gt | lt | eq } { port | biff | bootpc | bootps | dns | discard | dnsix | echo | mobilip-ag | mobilip-mn | nameserver | netbios-dgm | netbios-ns | netbios-ssn | ntp | rip | snmp | snmptrap | sunrpc | syslog | tacacs-ds | talk | tftp | time | who | xdmcp } } | time-range time-name | [ dscp dscp ] | vpn-instance vpn-instance-name | logging ] *
     ```
   * When *protocol* is specified as TCP, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+tcp+destination+any+destination-port+range) [ rule-id ] [ name rule-name ] { permit | deny } { tcp | 6 } [ destination { destination-ipv6-address { prefix-length | destination-wildcard } | dest-ipv6-addr-prefix | any } | destination-port { range { port | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } { port | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } | { gt | lt | eq } { port | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } } | fragment | source { source-ipv6-address { prefix-length | source-wildcard } | src-ipv6-addr-prefix | any } | source-port { range { port | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } { port | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } | { gt | lt | eq } { port | chargen | bgp | cmd | daytime | discard | domain | echo | exec | finger | ftp | ftp-data | gopher | hostname | irc | klogin | kshell | login | lpd | nntp | pop2 | pop3 | smtp | sunrpc | tacacs | talk | telnet | time | uucp | whois | www } } | time-range time-name | [ dscp dscp ] | vpn-instance vpn-instance-name | logging | tcp-flag { tcp-flag [ mask mask-value ] | established | { ack [ fin | psh | rst | syn | urg ] * } | { fin [ ack | psh | rst | syn | urg ] * } | { psh [ fin | ack | rst | syn | urg ] * } | { rst [ fin | psh | ack | syn | urg ] * } | { syn [ fin | psh | rst | ack | urg ] * } | { urg [ fin | psh | rst | syn | ack ] * } } ] *
     ```
   * When *protocol* is specified as ICMPv6, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+icmpv6+destination+any+fragment+icmp6-type) [ rule-id ] [ name rule-name ] { permit | deny } { icmpv6 | 58 } [ destination { destination-ipv6-address { prefix-length | destination-wildcard } | dest-ipv6-addr-prefix | any } | fragment | icmp6-type { icmp6-type-name | icmp6-type [ icmp6-code ] } | source { source-ipv6-address { prefix-length | source-wildcard } | src-ipv6-addr-prefix | any } | time-range time-name | [ dscp dscp ] | vpn-instance vpn-instance-name | logging ] *
     ```
   * When *protocol* is specified as any other protocol except the preceding well-known protocols, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+hoport+gre+ipv6+ipv6-ah+ipv6-esp+ospf) [ rule-id ] [ name rule-name ] { permit | deny } { hoport | protocol | gre | ipv6 | ipv6-ah | ipv6-esp | ospf | 7-16 | 18-57 | 59-255 | ipv6-frag | ipv6-routing | ipv6-destination } [ destination { destination-ipv6-address { prefix-length | destination-wildcard } | dest-ipv6-addr-prefix | any } | fragment | source { source-ipv6-address { prefix-length | source-wildcard } | src-ipv6-addr-prefix | any } | time-range time-name | [ dscp dscp ] | vpn-instance vpn-instance-name | logging ] *
     ```
   
   
   
   In this example, only one permit or deny rule is configured. In actual configuration, you can configure multiple ACL6 rules and decide the matching order of the rules according to service requirements.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To configure a time-based advanced ACL6, you must create a time range. For details, see [Creating a Time Range in Which an ACL6 Takes Effect](vrp_acl6_cfg_0009.html).
   
   When you configure a rule for an advanced ACL6:
   * If a destination IPv6 address, destination port number, source IPv6 address, and source port number are specified by **destination**, **destination-port**, **source**, and **source-port** respectively, the system filters only packets with the specified destination IPv6 address, destination port number, source IPv6 address, and source port number.
   * If all destination and source IPv6 addresses are specified by **any**, the system does not check packets' destination or source IPv6 addresses, and considers that all packets have matched the rule and directly takes an action (**deny** or **permit**) on the packets.
   * If **time-range** is specified, the specified time range name must exist. If the specified time range name does not exist, the ACL6 rule configuration fails.
6. (Optional) Configure a description for the ACL6 rule.
   
   
   ```
   [rule](cmdqueryname=rule+description) rule-id description destext
   ```
   
   The ACL6 rule description helps you understand and remember the functions or purpose of the ACL6 rule.
   
   You must create a rule before you can configure a description for it.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Example

* Configure a filtering rule for ICMPv6 packets based on the source IPv6 address (host address) and destination IPv6 address segment.
  
  To permit ICMPv6 packets from a host and destined for a network segment, configure a rule in an ACL6. For example, to permit ICMPv6 packets from the host at 2001:db8:1::2/128 and destined for the network segment 2001:db8:1::1/64, configure the following rule in ACL6 3001.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl ipv6 3001
  [*HUAWEI-acl6-advance-3001] rule permit icmpv6 source 2001:db8:1::2 128 destination 2001:db8:1::1 64
  [*HUAWEI-acl6-advance-3001] quit
  [*HUAWEI] commit
  ```
* Configure a filtering rule for TCP packets based on the TCP destination port number, source IPv6 address (host address), and destination IPv6 address segment.
  
  To prohibit Telnet connections between a specified host and the hosts on a network segment, configure a rule in an advanced ACL6. For example, to prohibit Telnet connections between the host at 2001:db8:1::3/128 and hosts on the network segment 2001:db8:2::1/64, configure the following rule in the advanced ACL6 **deny-telnet**.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl ipv6 name deny-telnet
  [*HUAWEI-acl6-advance-deny-telnet] rule deny tcp destination-port eq telnet source 2001:db8:1::3 128 destination 2001:db8:2::1 64
  [*HUAWEI-acl6-advance-deny-telnet] quit
  [*HUAWEI] commit
  ```
  
  To prohibit the specified hosts from accessing web pages (HTTP is used to access web pages, and the TCP port number is 80), configure rules in an advanced ACL6. For example, to prohibit hosts at 2001:db8:1::3/128 and 2001:db8:1::4/128 from accessing web pages, configure the following rules in the advanced ACL6 **no-web**.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl ipv6 name no-web
  [*HUAWEI-acl6-advance-no-web] rule deny tcp destination-port eq 80 source 2001:db8:1::3 128
  [*HUAWEI-acl6-advance-no-web] rule deny tcp destination-port eq 80 source 2001:db8:1::4 128
  [*HUAWEI-acl6-advance-no-web] quit
  [*HUAWEI] commit
  ```

#### Verifying the Configuration

Run the [**display acl ipv6**](cmdqueryname=display+acl+ipv6+name+all) { *advance-acl6-number* | **name** *advance-acl6-name* | **all** } command to check the configuration of the advanced ACL6.


#### Follow-up Procedure

Apply the advanced ACL6 to a service module so that the advanced ACL6 rules can be delivered and take effect.