traffic-analysis enable
=======================

traffic-analysis enable

Function
--------



The **traffic-analysis enable** command creates an action for enabling intelligent traffic analysis in a traffic behavior.

The **undo traffic-analysis enable** command deletes the action of enabling intelligent traffic analysis in a traffic behavior.



By default, no action of enabling intelligent traffic analysis is configured in a traffic behavior.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-analysis enable**

**undo traffic-analysis enable**


Parameters
----------

None

Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* The UDP intelligent traffic analysis module of a device matches UDP traffic passing through the inbound interface based on ACL rules. Only common IPv4 UDP packets or inner IPv4 UDP packets encapsulated in IPv4 VXLAN packets can be matched. Matched traffic is sent to The TAP for analysis based on the block granularity.
* The TCP intelligent traffic analysis module of a device matches TCP traffic passing through the inbound interface based on ACL rules and creates an intelligent traffic analysis flow table for in-depth analysis of matched traffic to obtain high-precision information such as the packet loss rate, delay, and traffic volume.

**Prerequisites**

An ACL has been created by running the **acl** command in the system view before intelligent traffic analysis is enabled for TCP flows. Currently, only the following advanced ACL rules are supported. The ACL rules that are not supported cannot be delivered, preventing the TAP from receiving corresponding service flows.

* Rule 1: TCP + destination IPv4 or IPv6 address;
* Rule 2: TCP + destination IPv4 or IPv6 address + destination TCP port number;
* Rule 3: TCP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address;
* Rule 4: TCP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address + destination TCP port number;
* Rule 5: UDP + destination IPv4 address + source IPv4 address + destination UDP port number Note: In intelligent traffic analysis, the deny or permit action specified in an ACL rule does not take effect. As long as service flows match the preceding advanced ACL rules, they are sent to the TAP for processing.

**Precautions**

* Intelligent traffic analysis for UDP flows cannot be performed for RoCEv2 packets whose destination UDP port number is 4791.
* If you run this command multiple times, all configurations take effect.
* The traffic policy containing the traffic behavior can be applied only to the inbound and outbound directions globally (including the slot). Only UDP is supported in the outbound direction.

Example
-------

# Configure a traffic behavior named b1 to enable intelligent traffic analysis.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] traffic-analysis enable

```