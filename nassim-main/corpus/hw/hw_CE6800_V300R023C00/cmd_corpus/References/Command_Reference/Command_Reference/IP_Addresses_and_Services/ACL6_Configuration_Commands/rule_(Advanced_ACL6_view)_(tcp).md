rule (Advanced ACL6 view) (tcp)
===============================

rule (Advanced ACL6 view) (tcp)

Function
--------



The **rule** command creates or modifies an ACL6 rule in the advanced ACL6 view.

The **undo rule** command deletes an ACL6 rule in the advanced ACL6 view.



By default, no advanced ACL6 rule is created.


Format
------

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **tcp** | *6* } [ **destination** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *dest-ipv6-addr-prefix* | **any** } | **destination-port** { **range** { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } | { **gt** | **lt** | **eq** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } } | **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *src-ipv6-addr-prefix* | **any** } | **source-port** { **range** { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } | { **gt** | **lt** | **eq** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } } | **time-range** *time-name* | **dscp** *dscp-value* | **vpn-instance** *vpn-instance-name* | **logging** | **tcp-flag** { *tcp-flag* [ **mask** *mask-value* ] | **established** | { **ack** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **fin** [ **ack** | **psh** | **rst** | **syn** | **urg** ] \* } | { **psh** [ **fin** | **ack** | **rst** | **syn** | **urg** ] \* } | { **rst** [ **fin** | **psh** | **ack** | **syn** | **urg** ] \* } | { **syn** [ **fin** | **psh** | **rst** | **ack** | **urg** ] \* } | { **urg** [ **fin** | **psh** | **rst** | **syn** | **ack** ] \* } } ] \*

**undo rule** [ **name** *rule-name* ] { **permit** | **deny** } { **tcp** | *6* } [ **destination** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *dest-ipv6-addr-prefix* | **any** } | **destination-port** { **range** { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } | { **gt** | **lt** | **eq** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } } | **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *src-ipv6-addr-prefix* | **any** } | **source-port** { **range** { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } | { **gt** | **lt** | **eq** } { *port* | **chargen** | **bgp** | **cmd** | **daytime** | **discard** | **domain** | **echo** | **exec** | **finger** | **ftp** | **ftp-data** | **gopher** | **hostname** | **irc** | **klogin** | **kshell** | **login** | **lpd** | **nntp** | **pop2** | **pop3** | **smtp** | **sunrpc** | **tacacs** | **talk** | **telnet** | **time** | **uucp** | **whois** | **www** } } | **time-range** *time-name* | **dscp** *dscp-value* | **vpn-instance** *vpn-instance-name* | **logging** | **tcp-flag** { *tcp-flag* [ **mask** *mask-value* ] | **established** | { **ack** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **fin** [ **ack** | **psh** | **rst** | **syn** | **urg** ] \* } | { **psh** [ **fin** | **ack** | **rst** | **syn** | **urg** ] \* } | { **rst** [ **fin** | **psh** | **ack** | **syn** | **urg** ] \* } | { **syn** [ **fin** | **psh** | **rst** | **ack** | **urg** ] \* } | { **urg** [ **fin** | **psh** | **rst** | **syn** | **ack** ] \* } } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL6 rule. | The value is an integer ranging from 0 to 4294967294. |
| **name** *rule-name* | Specifies the name of an ACL rule. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or start with an underscore (\_). |
| **permit** | Permits packets that match conditions. | - |
| **deny** | Denies the packets that match the rule. | - |
| **tcp** *6* | Transmission Control Protocol(6). | - |
| **destination** | Matches packets based on the destination IPv6 address.  If no destination IPv6 address is specified, an ACL takes effect for packets with any destination IPv6 address. | - |
| *destination-ipv6-address* | Specifies the destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specify the length of IPv6 address mask. | The value is an integer ranging from 1 to 128. |
| *dest-ipv6-addr-prefix* | Specifies the destination IPv6 address with a prefix. | The value is a string case-sensitive characters. It cannot contain spaces. |
| **any** | Indicates any destination IPv6 address. | - |
| **destination-port** | Matches packets based on destination port numbers. This parameter is available only when protocol is set to tcp (6) or udp (17). If destination-port is not configured, TCP and UDP packets to any destination ports are matched. | - |
| **range** | Matches packets with the specified port number in a specified range. | - |
| *port* | Specifies a TCP port number. | The value is an integer ranging from 0 to 65535. |
| **chargen** | Port for the Character Generator Protocol (19). | - |
| **bgp** | Border Gateway Protocol (179). | - |
| **cmd** | Remote commands, with no requirement for remote shell (rshell) and remote copy during login(514). | - |
| **daytime** | Port used to send the date and time to the requesting host (13). | - |
| **discard** | Empty service(9). | - |
| **domain** | Domain Name Service (53). | - |
| **echo** | Echo service (7). | - |
| **exec** | Port used to authenticate remote processes (512). | - |
| **finger** | Finger service for user contact information, used to query information, such as online users of remote host(79). | - |
| **ftp** | File Transfer Protocol data port (21). | - |
| **ftp-data** | FTP data connections port (20). | - |
| **gopher** | Information retrieval protocol (used for Internet document searching and retrieval) (70). | - |
| **hostname** | Host name service on the NIC (101). | - |
| **irc** | IRC (multi-thread chat protocol) (194). | - |
| **klogin** | Remote login using Kerberos version 5 (543). | - |
| **kshell** | Remote shell using Kerberos version 5 (544). | - |
| **login** | Remote login (513). | - |
| **lpd** | Port for the Line Printer Daemon protocol (515). | - |
| **nntp** | NNTP port, which carries USENET (119). | - |
| **pop2** | Port for the email protocol version 2 (109). | - |
| **pop3** | Port for the email protocol version 3 (110). | - |
| **smtp** | Simple Mail Transport Protocol (25). | - |
| **sunrpc** | Remote Procedure Call (RPC) protocol of SUN. It is used to execute remote commands and is used by the network file system (NFS). (111). | - |
| **tacacs** | Access control system used for TCP/IP authentication and access (TACACS) (49). | - |
| **talk** | Remote dialog service and customer (517). | - |
| **telnet** | Telnet (23). | - |
| **time** | Time Protocol (37). | - |
| **uucp** | Unix-to-Unix Copy Program (540). | - |
| **whois** | Directory service (43). | - |
| **www** | World Wide Web,HTTP for WWW services, used for web page browsing (80). | - |
| **gt** | Matches packets with a port number greater than the specified port number. | - |
| **lt** | Packets with source or destination port numbers less than the specified port number are matched. | - |
| **eq** | Packets with source or destination port numbers equal to the specified port number are matched. | - |
| **fragment** | Checks fragmented packets. | - |
| **source** | Matches packets based on source IPv6 addresses.  If source is not configured, packets from any source IPv6 address are matched. | - |
| *source-ipv6-address* | Specifies the source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *src-ipv6-addr-prefix* | Specifies the length of an IPv6 address mask. | The value is an integer ranging from 1 to 128. |
| **source-port** | Matches packets based on the source port.  If source port is not specified, packets originating from any port are matched. | - |
| **time-range** *time-name* | Specifies the time range during which the rule takes effect. If this parameter is not specified, the rule takes effect immediately after being configured.  The time range is configured using the time-range command. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **dscp** *dscp-value* | Specifies a DSCP. | The value is an integer ranging from 0 to 63. |
| **vpn-instance** *vpn-instance-name* | Matches packets based on an IPv6 VPN instance name. If the traffic is from L3VPN, this option must be configured in the ACL. If this option is not configured, it indicates the traffic belongs to the public network rather than L3VPN. | The name is a string of 1 to 31 characters and case sensitive. |
| **logging** | Indicates whether to log the matched packets. | - |
| **tcp-flag** *tcp-flag* | Specifies a TCP flag value.  This parameter is available only when protocol is set to tcp (6). The TCP header has six flag bits (including URG, ACK, PSH, PST, SYN, and FIN). The meanings of the flag bits are as follows:   * URG: indicates that the urgent pointer is valid. * ACK: indicates that the sequence number is confirmed to be valid. * PSH: indicates that the receiver should deliver this segment to the application layer as soon as possible. * PST: indicates that the connection is reestablished. * SYN: indicates that the sequence number is synchronized to initiate a connection. * FIN: indicates that the sender finishes sending data. | The value is an integer ranging from 0 to 63. ACL use integer (0 to 63) to indicate the 6 flags. For example, if the tcp-flag is set as 0, it indicates all the bits of the 6 flags are 0s. 63 indicates all the bits of the 6 flags are 1s. If SYN is 1 and ACK is 1, other flags are 0, set the tcp-flag to 18 (binary number is 010010). |
| **mask** *mask-value* | Specifies a TCP flag mask. | The value is an integer ranging from 0 to 63. After this parameter is set, the system uses bits to match the value of the Flags field in TCP packets. The matching is considered successful if the bits obtained by performing the bitwise AND operation on the values of the Flags field carried in a TCP packet and the mask-value parameter are consistent with those obtained by performing the same operation on the specified values of the tcp-flag and mask-value parameters. |
| **established** | Matches TCP packets in the Established state.  After established is configured in an ACL rule, a device matches the TCP packets whose ACK is 1 or RST is 1. Network attackers may send a large number of invalid TCP SYN packets to attack network devices. You can configure established in an advanced ACL rule to allow TCP packets to be transmitted unidirectionally. This means that after a device has set up TCP connections with other devices, the device only sends TCP packets to the other devices but does not receive TCP packets from the other devices. | - |
| **ack** | Matches TCP packets based on the ACK flag. | - |
| **fin** | Matches TCP packets based on the FIN flag. | - |
| **psh** | Matches the PSH flag bit in a TCP packet. | - |
| **rst** | Matches TCP packets based on the RST flag. | - |
| **syn** | Matches TCP packets based on the SYN flag. | - |
| **urg** | Matches TCP packets based on the URG flag. | - |
| **rule** | Specifies an ACL6 rule. | - |
| *destination-wildcard* | Specifies the wildcard of the destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *source-wildcard* | Specifies the wildcard mask of a source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

Advanced ACL6 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After an advanced ACL6 is created, run the **rule** command to add rules to the ACL6.



**Prerequisites**



An advanced ACL6 has been created using the **acl ipv6** command in the system view.A time range has been configured using the **time-range** command in the system view if you want to specify a validity period when creating an advanced ACL6 rule.



**Configuration Impact**

When specifying an ACL rule ID, note the following:

* If a rule with a specified rule ID already exists, and the new rule conflicts with the existing one, the conflicting part in the new rule overwrites that in the existing rule.
* If no rule with the specified rule ID exists, a rule with the specified rule ID is created.When an ACL rule ID is not specified and a rule is added, the system automatically allocates an ID to this rule. ACL rules are arranged in ascending order of rule IDs, with the difference between two adjacent rules as an ACL increment.The rule IDs automatically generated by the system start from the ACL increment. For example, if the ACL increment is 5, the rule ID starts from 5; if the ACL increment is 2, the rule ID starts from 2. This allows you to add rules before the first rule.

**Precautions**



When you configure advanced ACL6 rules for ICMPv6, fragment and icmp6-type cannot be both configured.When you configure advanced ACL6 rules for TCP or UDP, fragment and destination-port or source-port cannot be both configured.If auto is configured when you run the **acl ipv6** command to create an ACL6, you cannot specify a rule ID when creating a rule. The system automatically uses the ACL6 step as the start rule ID, and the subsequent rules are numbered by a step in ascending order.If the auto mode based on the depth-first principle is specified as the matching order for an advanced ACL6 rule group, you cannot specify a rule ID when creating a rule.If rule-id is not specified when you run the **rule** command to create an ACL6, the system automatically assigns an ID to the ACL6 rule. You can run the **display acl ipv6** command to check the rule ID automatically assigned to an ACL6.If name rule-name is not specified when you run the **rule** command to create an ACL6, the system automatically generates a name for the ACL6 in the format of "rule"+"\_"+rule ID. Rule ID is the ID of an ACL6 rule that can be specified using the rule-id parameter or automatically assigned by the system. You can check the automatically generated name of an ACL6 rule through the NMS.You must specify the rule ID when deleting a rule. To check rule IDs, run the **display acl ipv6** command.Before deleting an ACL6 rule, run the **display acl ipv6** command to check whether the ACL6 rule has been applied to other services. Delete the rule only when it is not applied to other services.If the ID of an advanced ACL6 rule to be deleted is not specified, you must specify all parameters in the rule before deleting it.




Example
-------

# Configure an advanced ACL6 whose matching order is config.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 3000
[*HUAWEI-acl6-advance-3000] rule permit tcp source 2001:db8::1 64

```