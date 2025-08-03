if-match inbound-interface
==========================

if-match inbound-interface

Function
--------



The **if-match inbound-interface** command configures a matching rule based on an inbound interface in a traffic classifier.

The **undo if-match inbound-interface** command deletes a matching rule based on an inbound interface in a traffic classifier.



By default, a matching rule based on an inbound interface is not configured in a traffic classifier.


Format
------

**if-match inbound-interface** { { *interface-type* *interface-number1* | *interface-name1* } [ **to** { *interface-type* *interface-number2* | *interface-name2* } ] } &<1-8>

**undo if-match inbound-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number1* | The interface-number1 specifies the number of the first interface. | - |
| *interface-name1* | interface-name1 specifies the name of the first interface. | - |
| **to** | If to interface-type interface-number2 is not specified, only the interface specified by interface-number1 is used. | - |
| *interface-number2* | The interface-number2 specifies the number of the last interface. interface-number2 and interface-number1 identify a range of interfaces. If interface-number1 and interface-number2 are specified, multiple inbound interfaces can be matched. | - |
| *interface-name2* | interface-name2 specifies the name of the last interface. interface-name2 and interface-name1 specify an interface range, indicating that multiple inbound interfaces are matched. | - |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match inbound-interface** command to classify traffic based on an inbound interface so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

* A traffic policy containing the traffic classifier cannot be applied to either the outbound direction or inbound direction of an interface.
* A traffic classifier cannot match the inbound and outbound interfaces simultaneously.
* If you run the **if-match inbound-interface** command in the same traffic classifier view multiple times, only the latest configuration takes effect.
* This command can only specify physical interfaces of the same type in the same slot at a time. If the device supports interface split and the command specifies split interfaces, these interfaces must be split from the same physical interface.
* The matched interface cannot be an Eth-Trunk member interface.


Example
-------

# Configure a matching rule based on the inbound interface of 100GE1/0/1 in the traffic classifier class1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier class1
[*HUAWEI-classifier-class1] if-match inbound-interface 100GE 1/0/1

```