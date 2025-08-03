reset arp anti-attack statistics check user-bind
================================================

reset arp anti-attack statistics check user-bind

Function
--------



The **reset arp anti-attack statistics check user-bind** command clears the statistics on discarded ARP packets matching no binding entry.




Format
------

For CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**reset arp anti-attack statistics check user-bind** [ **vlan** [ *vlan-id* ] | **interface** [ *interface-name* | *interface-type* *interface-number* ] | **bridge-domain** [ *bd-id* ] ]

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**reset arp anti-attack statistics check user-bind** [ **vlan** [ *vlan-id* ] | **interface** [ *interface-name* | *interface-type* *interface-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Clears DAI statistics in a specified VLAN.  If vlan-id is not specified, the command clears DAI statistics in all VLANs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Clears DAI statistics on a specified interface.  If no interface name is specified, DAI statistics on all interfaces are cleared.   * interface-type specifies the interface type. * interface-number specifies the interface number. | - |
| **bridge-domain** *bd-id* | Clears DAI statistics in a specified BD.  If bd-id is not specified, DAI statistics in all BDs are cleared.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K. | The value is an integer ranging from 1 to 16777215. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After DAI is enabled, if ARP packets are discarded because they do not match the binding table, you can run the reset arp anti-attack statistics packet command to clear statistics about discarded ARP packets.


Example
-------

# Clear statistics about discarded ARP packets on 100GE 1/0/1.
```
<HUAWEI> reset arp anti-attack statistics check user-bind interface 100GE 1/0/1

```

# Clear statistics about all discarded ARP packets.
```
<HUAWEI> reset arp anti-attack statistics check user-bind

```