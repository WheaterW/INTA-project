observe-port packet-length
==========================

observe-port packet-length

Function
--------



The **observe-port packet-length** command configures the packet truncation function.

The **undo observe-port packet-length** command disables the packet truncation function.



By default, the packet truncation function is not configured.


Format
------

**observe-port packet-length** *packet-length*

**undo observe-port packet-length**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-length* | Specify the truncation length of mirror packets. | For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 64 to 256 and must be a multiple of 32. The unit is byte.  For the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer in the range from 64 to 255. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Supports the global configuration of the packet truncation option to truncate the original packet. After the truncation mode is configured, the configuration takes effect on all observing ports. By default, the original packets are not truncated.



For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM, the default length of truncated packets for intelligent traffic analysis is 256 bytes. After this command is executed, the length of truncated packets for intelligent traffic analysis is the same as that specified by the length parameter in the command.



**Precautions**

The actual length of the mirrored packet to be truncated is the configured length of the mirrored packet to be truncated plus the 4-byte CRC. For example, if the mirrored packet truncation length is set to 64 bytes, the mirrored packet length is 68 bytes (64 + 4 bytes).If the number of bytes truncated by the mirrored packet is too small, the protocol fields of mirrored packets may be incomplete. As a result, packets are discarded during forwarding. You are advised to set this parameter to a value greater than or equal to 160.


Example
-------

# Configure packet truncation and set the truncation length to 128 bytes.
```
<HUAWEI> system-view
[~HUAWEI] observe-port packet-length 128

```