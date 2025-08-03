display auto-defend configuration
=================================

display auto-defend configuration

Function
--------



The **display auto-defend configuration** command displays the attack source tracing configuration.




Format
------

**display auto-defend configuration** [ **cpu-defend** **policy** *policy-name* | **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cpu-defend** | Configure CPU defend. | - |
| **policy** *policy-name* | Displays the attack source tracing configuration of a specified attack defense policy.  If the cpu-defend policy policy-name parameter is specified, the configuration of the specified attack defense policy is displayed.  If the cpu-defend policy policy-name parameter is not specified, the configurations of all attack defense policies are displayed. | The value is a string of 1 to 31 case-sensitive characters. |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After attack source tracing is configured in an attack defense policy, you can run the display auto-defend configuration command to view the attack source tracing configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display auto-defend configuration.
```
<HUAWEI> display auto-defend configuration slot 1
 ----------------------------------------------------------------------------
 Name  : test
 Related slot : <1>
 auto-defend                      : enable
 auto-defend threshold            : 60 (pps)
 auto-defend attack-packet sample : 5 (pps)
 auto-defend alarm                : enable
 auto-defend alarm threshold      : 128 (pps)
 auto-defend action               : deny timer: 300 (second)
 auto-defend trace-type           : source-mac source-ip
 auto-defend protocol             : arp icmp dhcp dns igmp tcp telnet tcpv6 nd dhcpv6 mld icmpv6
 auto-defend whitelist 1          : acl number 2002
 ----------------------------------------------------------------------------

```
```
<HUAWEI> display auto-defend configuration slot 1
 ----------------------------------------------------------------------------
 Name  : test
 Related slot : <1>
 auto-defend                      : enable
 auto-defend threshold            : 60 (pps)
 auto-defend attack-packet sample : 5 (pps)
 auto-defend alarm                : enable
 auto-defend alarm threshold      : 128 (pps)
 auto-defend action               : deny timer: 300 (second)
 auto-defend trace-type           : source-mac source-ip
 auto-defend protocol             : arp icmp dhcp dns igmp tcp telnet
 auto-defend whitelist 1          : acl number 2002
 ----------------------------------------------------------------------------

```

**Table 1** Description of the **display auto-defend configuration** command output
| Item | Description |
| --- | --- |
| auto-defend | Whether attack source tracing is enabled. |
| auto-defend attack-packet sample | Packet sampling ratio for attack source tracing. |
| auto-defend threshold | Checking threshold for attack source tracing. |
| auto-defend alarm | Whether the alarm function for attack source tracing is enabled. |
| auto-defend trace-type | Attack source tracing mode:  source-mac: indicates attack source tracing based on source MAC addresses.  source-ip: indicates attack source tracing based on source IP addresses.  source-portvlan: indicates attack source tracing based on source ports+VLANs. |
| auto-defend protocol | Type of traced packets. |
| auto-defend action | Action taken on the attack source. The value can be:  deny timer: 300 (second): indicates that the device discards all attack packets in 300s.  error-down: indicates that the inbound interfaces of attack packets are shut down. |
| auto-defend whitelist | Whitelist for attack source tracing. |
| auto-defend alarm threshold | Threshold for reporting the attack source tracing event. |
| Name | Name of an attack defense policy. |
| Related slot | Slot that an attack defense policy is applied to. |