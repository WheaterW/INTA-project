ipv6 nd source-mac exclude-mac
==============================

ipv6 nd source-mac exclude-mac

Function
--------



The **ipv6 nd source-mac exclude-mac** command configures a protected MAC address.

The **undo ipv6 nd source-mac exclude-mac** command deletes a configured protected MAC address.



By default, no protected MAC address is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd source-mac exclude-mac** *mac-address*

**undo ipv6 nd source-mac exclude-mac** *mac-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a MAC address. | The value is in the H-H-H format. H is a 4-digit hexadecimal number. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The ND protocol has powerful functions. However, if there is no security mechanism, the ND protocol can be easily used by attackers. The system collects statistics about ND messages sent to the CPU based on the source MAC addresses of the messages. If the number of ND messages with the same source MAC address received within 5 seconds exceeds a specified threshold, the system considers that an attack occurs and adds the MAC address to an attack entry. Before the attack entry ages out, If a MAC address is added to an ND attack entry, the MAC address is aged out after the aging time expires. Some important servers may send a large number of ND messages. To prevent these messages from being filtered out, run the ipv6 nd source-mac exclude-mac command to configure the MAC addresses of these ND messages as protected ones.Set the maximum number of protected MAC addresses to 10.

**Precautions**

After a protected MAC address is configured, the device does not filter out ND attack messages sent from this MAC address.


Example
-------

# Set a protected MAC address to 2-2-2.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd source-mac exclude-mac 2-2-2

```