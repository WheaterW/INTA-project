c-bsr hash-length
=================

c-bsr hash-length

Function
--------



The **c-bsr hash-length** command sets a global hash mask length for candidate-bootstrap routers (C-BSRs).

The **undo c-bsr hash-length** command restores the default value.



By default, the global hash mask length of C-BSRs is 30.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-bsr hash-length** *hash-length*

**undo c-bsr hash-length**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hash-length* | Specifies a global hash mask length for C-BSRs. | The value is an integer ranging from 0 to 128. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an IPv6 PIM-SM network where a rendezvous point (RP) is dynamically elected using the BSR mechanism, each candidate-rendezvous point (C-RP) sends to the BSR an Advertisement message carrying the C-RP address, range of multicast groups that the C-RP serves, and C-RP priority. Then, the BSR collects all those information and the BSR hash mask length as an RP-set, encapsulates the RP-set into a bootstrap message, and advertises the message to all routers on the network. All routers use the RP-set and follow the same RP election rules to elect an RP for a specific group.The RP election rules are as follows:

* The C-RP with the highest priority wins (a larger priority value indicates a lower priority).
* If all C-RPs have the same priority, the hash function is operated. The C-RP with the largest calculated value is elected as the RP.
* If all C-RPs have the same priority and calculated hash value, the C-RP with the largest address wins the election.To configure a global hash mask length for C-BSRs, run the **c-bsr hash-length** command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast ipv6 routing-enable** command in the public network instance view.

**Configuration Impact**

If the **c-bsr hash-length** command is run more than once, the latest configuration overrides the previous one.

**Precautions**

A hash mask length configured for the global domain has the highest priority.A global hash mask length configured using the **c-bsr hash-length** command is effective for all C-BSRs on the router. To change the hash mask length of a C-BSR on an interface, run the **c-bsr** command.The **c-bsr** command is valid only for the specified interface. The **c-bsr** command configuration takes precedence over the **c-bsr hash-length** command configuration.


Example
-------

# In the public network instance, set the global hash mask length to 16 for C-BSRs.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] c-bsr hash-length 16

```