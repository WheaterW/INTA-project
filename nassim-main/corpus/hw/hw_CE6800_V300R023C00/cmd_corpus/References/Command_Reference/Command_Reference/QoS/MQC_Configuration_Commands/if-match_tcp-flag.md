if-match tcp-flag
=================

if-match tcp-flag

Function
--------



The **if-match tcp-flag** command configures a matching rule based on the TCP Flag in the TCP packet header in a traffic classifier.

The **undo if-match tcp-flag** command deletes a matching rule based on the TCP Flag in the TCP packet header in a traffic classifier.



By default, a matching rule based on the TCP Flag in the TCP packet header is not configured in a traffic classifier.


Format
------

**if-match tcp-flag** { *tcp-flag-value* | { **ack** | **fin** | **psh** | **rst** | **syn** | **urg** } \* }

**undo if-match tcp-flag**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tcp-flag-value* | Specifies the value of the TCP flag in the TCP packet header. | The value is an integer ranging from 0 to 63. |
| **ack** | Indicates that the TCP Flag type in the TCP packet header is ACK. | - |
| **fin** | Indicates that the TCP flag type in the TCP packet header is FIN. | - |
| **psh** | Indicates that the TCP Flag type in the TCP packet header is PSH. | - |
| **rst** | Indicates that the TCP flag type in the TCP packet header is RST. | - |
| **syn** | Indicates that the TCP Flag type in the TCP packet header is SYN. | - |
| **urg** | Indicates that the TCP Flag type in the TCP packet header is URG. | - |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match tcp-flag** command to classify packets based on the TCP Flag in the TCP packet header so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

If you run the **if-match tcp-flag** command in the same traffic classifier view multiple times, only the latest configuration takes effect.


Example
-------

# Configure a matching rule based on the TCP Flag of psh in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match tcp-flag psh

```