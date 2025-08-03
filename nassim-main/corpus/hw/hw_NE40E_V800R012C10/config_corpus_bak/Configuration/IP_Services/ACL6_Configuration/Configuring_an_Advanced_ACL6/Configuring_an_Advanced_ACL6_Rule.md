Configuring an Advanced ACL6 Rule
=================================

Advanced ACL6 rules are defined based on the source IPv6 address, destination IPv6 address, protocol type carried over IPv6, source port, and destination port to filter packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl ipv6**](cmdqueryname=acl+ipv6+name+advance+number+match-order+config+auto) { **name** *advance-acl6-name* [ **advance** ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   The advanced ACL6 view is displayed.
3. Run any of the following commands to create an advanced ACL6 rule:
   
   
   * When *protocol* is specified as UDP, run:
     
     [**rule**](cmdqueryname=rule+name+permit+deny+udp+destination+any+destination-pool) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **udp** | *17* } [ { **destination** { *destination-ipv6-address* *prefix-length* | *dest-ipv6-addr-prefix* | **any** } | **destination-pool** *destination-pool-name* } | **destination-port** { **range** { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } | { **gt** | **lt** | **eq** | **neq** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } } | **fragment** | { **source** { *source-ipv6-address* *prefix-length* | *src-ipv6-addr-prefix* | **any** } | **source-pool** *source-pool-name* } | **source-port** { **range** { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } | { **gt** | **lt** | **eq** | **neq** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } } | **time-range** *time-name* | [ **dscp** *dscp* | [ **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } | **tos** { *tos* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } ] \* ] | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
   * When *protocol* is specified as TCP, run:
     
     [**rule**](cmdqueryname=rule+name+permit+deny+tcp+destination+any+destination-pool) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **tcp** | *6* } [ { **destination** { *destination-ipv6-address* *prefix-length* | *dest-ipv6-addr-prefix* | **any** } | **destination-pool** *destination-pool-name* } | **destination-port** { **range** { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } | { **gt** | **lt** | **eq** | **neq** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } } | **fragment** | { **source** { *source-ipv6-address* *prefix-length* | *src-ipv6-addr-prefix* | **any** } | **source-pool** *source-pool-name* } | **source-port** { **range** { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } | { **gt** | **lt** | **eq** | **neq** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } } | **time-range** *time-name* | [ **dscp** *dscp-value* | [ **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } | **tos** { *value* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } ] \* ] | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **tcp-flag** { *tcp-flag* [ **mask** *mask-value* ] | **established** | { **ack** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **fin** [ **ack** | **psh** | **rst** | **syn** | **urg** ] \* } | { **psh** [ **fin** | **ack** | **rst** | **syn** | **urg** ] \* } | { **rst** [ **fin** | **psh** | **ack** | **syn** | **urg** ] \* } | { **syn** [ **fin** | **psh** | **rst** | **ack** | **urg** ] \* } | { **urg** [ **fin** | **psh** | **rst** | **syn** | **ack** ] \* } } ] \*
   * When *protocol* is specified as ICMPv6, run:
     
     [**rule**](cmdqueryname=rule+name+permit+deny+icmpv6+destination+any+destination-pool) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **icmpv6** | *58* } [ { **destination** { *destination-ipv6-address* *prefix-length* | *dest-ipv6-addr-prefix* | **any** } | **destination-pool** *destination-pool-name* } | **fragment** | **icmp6-type** { *icmp6-type-name* | *icmp6-type* [ **to** *icmp6-type-end* ] [ *icmp6-code* ] } | { **source** { *source-ipv6-address* *prefix-length* | *src-ipv6-addr-prefix* | **any** } | **source-pool** *source-pool-name* } | **time-range** *time-name* | [ **dscp** *dscp* | [ **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } | **tos** { *tos* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } ] \* ] | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
   * When *protocol* is specified as a protocol other than TCP, UDP, and ICMPv6, run:
     
     [**rule**](cmdqueryname=rule+name+permit+deny+hoport+option-code+1+5+gre+ipv6+ipv6-frag) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **hoport** [ **option-code** *option-value* ] | **1** | **5** | *protocol* | **gre** | **ipv6** | **ipv6-frag** | **ipv6-ah** | **ipv6-esp** | **ospf** | *7-16* | *18-42* | { *43* | **ipv6-routing** } [ **routing-type** *routing-number* ] | *44-57* | *59* | { *60* | **ipv6-destination** } [ **option-code** *option-value* ] | *61-255* } [ { **destination** { *destination-ipv6-address* *prefix-length* | *dest-ipv6-addr-prefix* | **any** } | **destination-pool** *destination-pool-name* } | **fragment** | { **source** { *source-ipv6-address* *prefix-length* | *src-ipv6-addr-prefix* | **any** } | **source-pool** *source-pool-name* } | **time-range** *time-name* | [ **dscp** *dscp* | [ **precedence** { *precedence* | **critical** | **flash** | **flash-override** | **immediate** | **internet** | **network** | **priority** | **routine** } | **tos** { *tos* | **max-reliability** | **max-throughput** | **min-delay** | **min-monetary-cost** | **normal** } ] \* ] | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
   
   
   
   Adding new rules to an ACL6 will not affect the existing rules.
   
   When an existing rule is edited and the edited contents conflict with the original contents, the edited contents take effect.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When you configure an advanced ACL6 rule:
   
   * If a destination IPv6 address is specified by configuring **destination**, a destination port number is specified by configuring **destination-port**, a source IPv6 address is specified by configuring **source**, and a source port number is specified by configuring **source-port**, the system filters only packets with the specified destination IPv6 address, destination port number, source IPv6 address, and source port number.
   * If all destination IPv6 addresses, destination port numbers, source IPv6 addresses, and source port numbers are specified by configuring **any**, the system does not check packets' destination IPv6 addresses, destination port numbers, source IPv6 addresses, and source port numbers, and considers that all packets have matched the rule and directly takes an action (**deny** or **permit**) on the packets.
   * If a validity period is specified by configuring **time-range**, the time range name specified by *time-name* must already exist. Otherwise, the configuration does not take effect.
   * If you delete the IPv6 addresses specified in an ACL6 rule by running the **undo rule** command, filtering will not be performed based on IPv6 addresses, potentially causing service interruptions. The service interruption risk warning function, enabled by default, indicates that such configuration may adversely affect services. If the function is disabled, run the **undo configuration prevent-misoperation disable** command to enable it.
4. (Optional) Run [**rule**](cmdqueryname=rule) *rule-id* [**description**](cmdqueryname=description) *destext*
   
   
   
   A description is configured for the rule.
   
   
   
   The description of an ACL6 rule can contain the functions of the ACL6 rule. Configuring a description for an ACL6 rule is recommended to prevent misuse of the rule in the following situations:
   * A large number of ACL6s are configured, and their functions are difficult to identify.
   * An ACL6 is used at a long interval, and its function may be left forgotten.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.