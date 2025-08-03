if-match outbound-interface
===========================

if-match outbound-interface

Function
--------



The **if-match outbound-interface** command configures a matching rule based on an outbound interface in a traffic classifier.

The **undo if-match outbound-interface** command deletes a matching rule based on an outbound interface in a traffic classifier.



By default, a matching rule based on an outbound interface is not configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match outbound-interface** { { *interface-type* *interface-number1* | *interface-name1* } [ **to** { *interface-type* *interface-number2* | *interface-name2* } ] } &<1-8>

**undo if-match outbound-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number1* | The interface-number1 specifies the number of the first interface. | - |
| *interface-name1* | interface-name1 specifies the name of the first interface. | - |
| **to** | If to interface-type interface-number2 is not specified, only the interface specified by interface-number1 is matched. A maximum of eight interfaces can be specified. | - |
| *interface-number2* | The interface-number2 specifies the number of the last interface. interface-number2 and interface-number1 identify a range of interfaces. If interface-number1 and interface-number2 are specified, multiple outbound interfaces can be matched. | - |
| *interface-name2* | interface-name2 specifies the name of the last interface. interface-name2 and interface-name1 specify an interface range, indicating that multiple outbound interfaces are matched. | - |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match outbound-interface** command to classify packets based on an outbound interface so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

* A traffic policy containing this matching rule cannot be applied to the outbound direction .
* If the device supports interface split and the command specifies split interfaces, these interfaces must be split from the same physical interface.
* The matched interface cannot be an Eth-Trunk member interface.
* A traffic classifier cannot match the inbound and outbound interfaces simultaneously.
* If you run the **if-match outbound-interface** command in the same traffic classifier view multiple times, only the latest configuration takes effect.
* A traffic policy containing this matching rule takes effect only for known unicast packets forwarded.


Example
-------

# Configure a matching rule based on the outbound interface of 100GE1/0/1 in the traffic classifier class1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier class1
[*HUAWEI-classifier-class1] if-match outbound-interface 100GE 1/0/1

```