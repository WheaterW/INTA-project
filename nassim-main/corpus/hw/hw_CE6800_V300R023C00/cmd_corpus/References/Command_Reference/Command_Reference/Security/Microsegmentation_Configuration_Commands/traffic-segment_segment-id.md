traffic-segment segment-id
==========================

traffic-segment segment-id

Function
--------



The **traffic-segment segment-id** command creates an EPG and displays the EPG view, or displays the view of an existing EPG.

The **undo traffic-segment segment-id** command deletes an EPG.



By default, no EPG is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-segment segment-id** *id-value* [ **segment-name** *name* ] [ **intra-epg-behavior** { **permit** | **deny** | **none** } ]

**undo traffic-segment segment-id** *id-value* [ **segment-name** *name* ] [ **intra-epg-behavior** { **permit** | **deny** | **none** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *id-value* | Specifies a microsegmentation group of the IP address type. | The value is an integer that ranges from 1 to 65535. |
| **segment-name** *name* | Specifies a microsegmentation name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. It must start with a letter. |
| **intra-epg-behavior** | Configures the intra-group behavior of the EPG. | - |
| **permit** | Allows packets to pass. | - |
| **deny** | Discards the packets. | - |
| **none** | If no behavior is configured for an EPG, packet forwarding is not affected. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a data center network, servers can be added to EPGs based on certain rules, and GBPs can be deployed based on EPGs to implement traffic control between servers. You can run the **traffic-segment segment-id** command to create an EPG.


Example
-------

# Configure EPG 32768 and EPG TEST.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] traffic-segment segment-id 32768 segment-name TEST

```