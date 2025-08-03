reset sdn openflow session
==========================

reset sdn openflow session

Function
--------



The **reset sdn openflow session** command resets the OpenFlow connection.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset sdn openflow session** [ **controller** [ **vpn-instance** *vpn-instance-name* ] { *ipv4-address* | *ipv6-address* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **controller** | Controller. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance that the controller belongs to. | The value must be the name of an existing VPN instance. |
| *ipv4-address* | Specifies the controller's IP address. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the controller's IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Running the **reset sdn openflow session** command will tear down and reestablish the OpenFlow connection. This command can be used when you need to verify the OpenFlow connection establishment process. Exercise caution when you use this command to reset an OpenFlow connection.


Example
-------

# Reset the OpenFlow connection.
```
<HUAWEI> reset sdn openflow session

```