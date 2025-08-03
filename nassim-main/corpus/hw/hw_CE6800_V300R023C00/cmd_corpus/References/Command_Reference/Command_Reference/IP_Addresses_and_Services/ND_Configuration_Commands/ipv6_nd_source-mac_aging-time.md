ipv6 nd source-mac aging-time
=============================

ipv6 nd source-mac aging-time

Function
--------



The **ipv6 nd source-mac aging-time** command sets an aging time for ND attack entries with fixed source MAC addresses.

The **undo ipv6 nd source-mac aging-time** command restores the default aging time for ND attack entries with fixed source MAC addresses.



The default aging time of ND attack entries with fixed source MAC addresses is 300 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd source-mac aging-time** *aging-value*

**undo ipv6 nd source-mac aging-time** [ *aging-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *aging-value* | Specifies an aging time for ND attack entries. | The value is an integer ranging from 60 to 6000, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The ND protocol has powerful functions. However, if there is no security mechanism, the ND protocol can be easily used by attackers. The system collects statistics about ND messages sent to the CPU based on the source MAC addresses of the messages. If the number of ND messages with the same source MAC address received within 5 seconds exceeds a specified threshold, the system considers that an attack occurs and adds the MAC address to an attack entry. Before the attack entry ages out, the system performs the following operations based on a configured detection mode:

* If the detection mode is set to filter, the system generates log information and filters out the ND messages sent from the source MAC address.
* If the detection mode is set to monitor, the system only generates log information and does not filter out the ND messages sent from the source MAC address.To configure an aging time for ND attack entries with fixed source MAC addresses, run the ipv6 nd source-mac aging-time command.After the configured aging time expires, the entries are aged out.

Example
-------

# Set an aging time for ND attack entries with fixed source MAC addresses to 500s.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd source-mac aging-time 500

```