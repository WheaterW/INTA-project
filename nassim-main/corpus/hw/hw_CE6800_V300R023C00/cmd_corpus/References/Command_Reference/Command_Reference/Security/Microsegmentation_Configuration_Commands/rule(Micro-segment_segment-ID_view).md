rule(Micro-segment segment-ID view)
===================================

rule(Micro-segment segment-ID view)

Function
--------



The **rule** command configures a policy rule in the microsegmentation classifier view.

The **undo rule** command deletes a policy rule in the microsegmentation classifier view.



By default, no policy rule is configured in the microsegmentation classifier view.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**rule** [ *priority* ] { **permit** | **deny** } { **source-segment** *id-value* | **destination-segment** *id-value* } \* [ [ **protocol** *protocol-number-1* ] | [ **protocol** { **tcp** | **udp** | *protocol-number-2* } [ **source-port** { **eq** *port-num* | **gt** *gt-port-num* | **lt** *lt-port-num* | **range** *begin-port-num* *end-port-num* } ] [ **destination-port** { **eq** *port-num* | **gt** *gt-port-num* | **lt** *lt-port-num* | **range** *begin-port-num* *end-port-num* } ] ] ]

**undo rule** [ *priority* ] { **permit** | **deny** } { **source-segment** *id-value* | **destination-segment** *id-value* } \* [ [ **protocol** *protocol-number-1* ] | [ **protocol** { **tcp** | **udp** | *protocol-number-2* } [ **source-port** { **eq** *port-num* | **gt** *gt-port-num* | **lt** *lt-port-num* | **range** *begin-port-num* *end-port-num* } ] [ **destination-port** { **eq** *port-num* | **gt** *gt-port-num* | **lt** *lt-port-num* | **range** *begin-port-num* *end-port-num* } ] ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Rule priority. | The value is an integer ranging from 0 to 4095. |
| **permit** | Allows packets to pass. | - |
| **deny** | Discards the packets. | - |
| **source-segment** *id-value* | Microsegmentation source group. | The value is an integer ranging from 1 to 65535. |
| **destination-segment** *id-value* | Microsegmentation destination group. | The value is an integer ranging from 1 to 65535. |
| **protocol** *protocol-number-2* | TCP or UDP protocol number. | The value is 6 or 17. |
| **protocol** *protocol-number-1* | Protocol number. | The value is an integer ranging from 0 to 5, 7 to 16, or 18 to 255. |
| **tcp** | TCP protocol. | - |
| **udp** | UDP protocol. | - |
| **source-port** | Source port. | - |
| **eq** *port-num* | The value is the same as the specified port number. | The value is an integer ranging from 0 to 65535. |
| **gt** *gt-port-num* | The value is greater than the specified port number. | The value is an integer ranging from 0 to 65534. |
| **lt** *lt-port-num* | The value is smaller than the specified port number. | The value is an integer ranging from 1 to 65535. |
| **range** *begin-port-num* *end-port-num* | Range of port numbers. | The value is an integer ranging from 0 to 65535. |
| **destination-port** | Destination port. | - |



Views
-----

Micro-segment segment-ID view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a data center network, servers are grouped into EPGs based on certain rules. If you do not want to use the default microsegmentation policy for packets matching EPGs but specify GBPs for the packets, configure and apply GBPs as follows:

1. Create a segment classifier and configure rules for matching EPG packets in the segment classifier view.
2. Create a segment behavior and configure a traffic control behavior for the EPG in the segment behavior view.
3. Create a segment policy and bind the segment classifier and segment behavior to the segment policy in the segment policy view.
4. Apply the segment policy.

**Precautions**

1. When range begin-port-num end-port-num is specified in the **rule** command, begin-port-num must be smaller than or equal to end-port-num.
2. If no rule priority is configured (that is, the priority parameter is not configured), the default value of priority is 0. If a policy rule has been configured, the value of priority is the next value of the configured maximum value.

Example
-------

# Configure a matching rule based on the source EPG 32768 and destination EPG 49151 in the segment classifier class1.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] segment classifier class1
[*HUAWEI-segmentclassifier-class1] rule permit source-segment 32768 destination-segment 49151

```