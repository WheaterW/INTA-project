dhcpv6 relay prefix-delegation route autosave
=============================================

dhcpv6 relay prefix-delegation route autosave

Function
--------



The **dhcpv6 relay prefix-delegation route autosave** command saves routing information forwarded by a relay agent into a specified file.

The undo dhcpv6 relay prefix-delegation route autosave command cancels the configuration.



By default, routing information forwarded by a relay agent into a specified file is not saved.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 relay prefix-delegation route autosave** *file-name*

**undo dhcpv6 relay prefix-delegation route autosave**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the path and file name of the file where routing information of DHCPv6 PD terminals is to be saved, for example, flash:/\*.pdr. | The value is a string of 1 to 51 case-insensitive characters, spaces not supported.The string contains letters, digits, hyphens (-), underscores (\_), and dots (.). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This command is used on DHCPv6 relay agents. This command saves routing information forwarded by a relay agent into a specified .pdr file.After this command is run, the system immediately saves routing information, and then saves routing information again every two hours. The interval at which the system saves routing information cannot be set.


Example
-------

# Save routing information forwarded by a relay agent into a specified file.
```
<HUAWEI> system-view
[~HUAWEI] dhcpv6 relay prefix-delegation route autosave flash:/dhcpv6-pd.pdr

```