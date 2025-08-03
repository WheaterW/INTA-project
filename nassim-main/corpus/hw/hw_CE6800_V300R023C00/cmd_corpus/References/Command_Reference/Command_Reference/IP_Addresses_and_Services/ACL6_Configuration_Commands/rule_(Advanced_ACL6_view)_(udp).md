rule (Advanced ACL6 view) (udp)
===============================

rule (Advanced ACL6 view) (udp)

Function
--------



The **rule** command creates or modifies an ACL6 rule in the advanced ACL6 view.

The **undo rule** command deletes an ACL6 rule in the advanced ACL6 view.



By default, no advanced ACL6 rule is created.


Format
------

**rule** [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **udp** | *17* } [ **destination** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *dest-ipv6-addr-prefix* | **any** } | **destination-port** { **range** { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } | { **gt** | **lt** | **eq** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } } | **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *src-ipv6-addr-prefix* | **any** } | **source-port** { **range** { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } | { **gt** | **lt** | **eq** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } } | **time-range** *time-name* | **dscp** *dscp* | **vpn-instance** *vpn-instance-name* | **logging** ] \*

**undo rule** [ **name** *rule-name* ] { **permit** | **deny** } { **udp** | *17* } [ **destination** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *dest-ipv6-addr-prefix* | **any** } | **destination-port** { **range** { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } | { **gt** | **lt** | **eq** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } } | **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *src-ipv6-addr-prefix* | **any** } | **source-port** { **range** { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } | { **gt** | **lt** | **eq** } { *port* | **biff** | **bootpc** | **bootps** | **dns** | **discard** | **dnsix** | **echo** | **mobilip-ag** | **mobilip-mn** | **nameserver** | **netbios-dgm** | **netbios-ns** | **netbios-ssn** | **ntp** | **rip** | **snmp** | **snmptrap** | **sunrpc** | **syslog** | **tacacs-ds** | **talk** | **tftp** | **time** | **who** | **xdmcp** } } | **time-range** *time-name* | **dscp** *dscp* | **vpn-instance** *vpn-instance-name* | **logging** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-id* | Specifies the ID of an ACL6 rule. | The value is an integer ranging from 0 to 4294967294. |
| **name** *rule-name* | Specifies the name of an ACL rule. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or start with an underscore (\_). |
| **permit** | Permits packets that match conditions. | - |
| **deny** | Denies the packets that match the rule. | - |
| **udp** | User Datagram Protocol(17). | - |
| *17* | Specifies a protocol number. | - |
| **destination** | Matches packets based on the destination IPv6 address.  If no destination IPv6 address is specified, an ACL takes effect for packets with any destination IPv6 address. | - |
| *destination-ipv6-address* | Specifies the destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specify the length of IPv6 address mask. | The value is an integer ranging from 1 to 128. |
| *dest-ipv6-addr-prefix* | Specifies the destination IPv6 address with a prefix. | The value is a string case-sensitive characters. It cannot contain spaces. |
| **any** | Indicates any destination IPv6 address. | - |
| **destination-port** | Matches packets based on destination port numbers. This parameter is available only when protocol is set to tcp (6) or udp (17). If destination-port is not configured, TCP and UDP packets to any destination ports are matched. | - |
| **range** | Matches packets with the specified port number in a specified range. | - |
| *port* | Specifies a UDP port number. | The value is an integer ranging from 0 to 65535. |
| **biff** | Asynchronous mail, which can be used to notify the user of the arrival of a mail. | - |
| **bootpc** | Bootstrap Protocol (BOOTP) client, which is used by DHCP clients. | - |
| **bootps** | Bootstrap Protocol (BOOTP) server, which is used by the DHCP service. | - |
| **dns** | Domain Name Service (53). | - |
| **discard** | Empty service(9). | - |
| **dnsix** | DNSIX security attribute marker (90). | - |
| **echo** | Echo service (7). | - |
| **mobilip-ag** | Mobile IP agent (434). | - |
| **mobilip-mn** | Mobile IP management (435). | - |
| **nameserver** | Host name service (42). | - |
| **netbios-dgm** | NETBIOS datagram service (138). | - |
| **netbios-ns** | NETBIOS name service (137). | - |
| **netbios-ssn** | NETBIOS session service (139). | - |
| **ntp** | Network time protocol, which can be exploited by worms (123). | - |
| **rip** | RIP Routing Protocol (520). | - |
| **snmp** | Simple Network Management Protocol (SNMP) (161). | - |
| **snmptrap** | SNMP Trap (162). | - |
| **sunrpc** | Remote Procedure Call (RPC) protocol of SUN. It is used to execute remote commands and is used by the network file system (NFS). (111). | - |
| **syslog** | Port used to execute non-interactive commands on a remote system (rshell, rcp) (514). | - |
| **tacacs-ds** | TACACS database service (65). | - |
| **talk** | Remote dialog service and customer (517). | - |
| **tftp** | Small File Transfer Protocol (69). | - |
| **time** | Time Protocol (37). | - |
| **who** | Who, list of login users (513). | - |
| **xdmcp** | X Display Manager Control Protocol,X Display Manager Control Protocol (177). | - |
| **gt** | Matches packets with a port number greater than the specified port number. | - |
| **lt** | Packets with source or destination port numbers less than the specified port number are matched. | - |
| **eq** | Packets with source or destination port numbers equal to the specified port number are matched. | - |
| **fragment** | Checks fragmented packets. | - |
| **source** | Matches packets based on source IPv6 addresses.  If source is not configured, packets from any source IPv6 address are matched. | - |
| *source-ipv6-address* | Specifies the source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *src-ipv6-addr-prefix* | Specifies the length of an IPv6 address mask. | The value is an integer ranging from 1 to 128. |
| **source-port** | Matches packets based on the source port.  If source port is not specified, packets originating from any port are matched. | - |
| **time-range** *time-name* | Specifies the time range during which the rule takes effect. If this parameter is not specified, the rule takes effect immediately after being configured.  The time range is configured using the time-range command. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **dscp** *dscp* | Matches IPv6 packets based on the leftmost six bits of the TC field. | The value is an integer ranging from 0 to 63. |
| **vpn-instance** *vpn-instance-name* | Matches packets based on an IPv6 VPN instance name. If the traffic is from L3VPN, this option must be configured in the ACL. If this option is not configured, it indicates the traffic belongs to the public network rather than L3VPN. | The name is a string of 1 to 31 characters and case sensitive. |
| **logging** | Indicates whether to log the matched packets. | - |
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



When you configure advanced ACL6 rules for ICMPv6, fragment and icmp6-type cannot be both configured.If auto is configured when you run the **acl ipv6** command to create an ACL6, you cannot specify a rule ID when creating a rule. The system automatically uses the ACL6 step as the start rule ID, and the subsequent rules are numbered by a step in ascending order.If the auto mode based on the depth-first principle is specified as the matching order for an advanced ACL6 rule group, you cannot specify a rule ID when creating a rule.If rule-id is not specified when you run the **rule** command to create an ACL6, the system automatically assigns an ID to the ACL6 rule. You can run the **display acl ipv6** command to check the rule ID automatically assigned to an ACL6.If name rule-name is not specified when you run the **rule** command to create an ACL6, the system automatically generates a name for the ACL6 in the format of "rule"+"\_"+rule ID. Rule ID is the ID of an ACL6 rule that can be specified using the rule-id parameter or automatically assigned by the system. You can check the automatically generated name of an ACL6 rule through the NMS.You must specify the rule ID when deleting a rule. To check rule IDs, run the **display acl ipv6** command.Before deleting an ACL6 rule, run the **display acl ipv6** command to check whether the ACL6 rule has been applied to other services. Delete the rule only when it is not applied to other services.If the ID of an advanced ACL6 rule to be deleted is not specified, you must specify all parameters in the rule before deleting it.When you configure advanced ACL6 rules for TCP or UDP, fragment and destination-port or source-port cannot be both configured.If auto is configured when you run the **acl ipv6** command to create an ACL6, you cannot specify a rule ID when creating a rule. The system automatically uses the ACL6 step as the start rule ID, and the subsequent rules are numbered by a step in ascending order.If the auto mode based on the depth-first principle is specified as the matching order for an advanced ACL6 rule group, you cannot specify a rule ID when creating a rule.If rule-id is not specified when you run the **rule** command to create an ACL6, the system automatically assigns an ID to the ACL6 rule. You can run the **display acl ipv6** command to check the rule ID automatically assigned to an ACL6.If name rule-name is not specified when you run the **rule** command to create an ACL6, the system automatically generates a name for the ACL6 in the format of "rule"+"\_"+rule ID. Rule ID is the ID of an ACL6 rule that can be specified using the rule-id parameter or automatically assigned by the system. You can check the automatically generated name of an ACL6 rule through the NMS.You must specify the rule ID when deleting a rule. To check rule IDs, run the **display acl ipv6** command.Before deleting an ACL6 rule, run the **display acl ipv6** command to check whether the ACL6 rule has been applied to other services. Delete the rule only when it is not applied to other services.If the ID of an advanced ACL6 rule to be deleted is not specified, you must specify all parameters in the rule before deleting it.




Example
-------

# Configure an advanced ACL6 whose matching order is config.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 3000
[*HUAWEI-acl6-advance-3000] rule deny udp source 2001:db8::1 64

```