display this ipv6 interface
===========================

display this ipv6 interface

Function
--------



The **display this ipv6 interface** command displays IPv6 information about the current interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display this ipv6 interface**


Parameters
----------

None

Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view IPv6 information on an interface, run the **display this ipv6 interface** command.

**Precautions**

Information displayed using the **display this ipv6 interface** command in the current interface view is the same as the information displayed using the display ipv6 interface command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IPv6 information on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] display this ipv6 interface
100GE1/0/1 current state : UP
IPv6 protocol current state : UP
IPv6 is enabled, link-local address is FE80::3ABA:1200:78A:6E02
  Global unicast address(es):
    2001:db8:1::1, subnet is 2001:db8:1::/64
  Joined group address(es):
    FF02::1:FF00:1
    FF02::1:FF8A:6E02
    FF02::2
    FF02::1
  MTU is 1500 bytes
  ND DAD is enabled, number of DAD attempts: 1
  ND reachable time is 1200000 milliseconds
  ND retransmit interval is 1000 milliseconds
  Hosts use stateless autoconfig for addresses

```

**Table 1** Description of the **display this ipv6 interface** command output
| Item | Description |
| --- | --- |
| current state | Physical status of the interface.   * UP. * DOWN. * Administratively DOWN. |
| IPv6 is enabled | The IPv6 capability is configured on the interface. |
| IPv6 protocol current state | Protocol status of the interface.   * UP. * DOWN. * Administratively DOWN. |
| link-local address | Link local address configured for that interface. |
| Global unicast address(es) | Global unicast address of the interface. |
| Joined group address(es) | All multicast addresses that have joined the interface. |
| MTU | MTU of the interface. |
| ND reachable time | Time period for a neighbor to keep reachable. |
| ND retransmit interval | Retransmission interval. |
| number of DAD attempts | Number of conflicting address detection times. |
| Hosts use stateless autoconfig for addresses | Host address obtained using stateless autoconfiguration. |