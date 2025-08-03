if-match ip-precedence
======================

if-match ip-precedence

Function
--------



The **if-match ip-precedence** command configures a matching rule based on the IP precedence of packets in a traffic classifier.

The **undo if-match ip-precedence** command deletes a matching rule based on the IP precedence of packets in a traffic classifier.



By default, a matching rule based on the IP precedence of packets is not configured in a traffic classifier.


Format
------

**if-match ip-precedence** *ip-precedence* &<1-8>

**undo if-match ip-precedence**

**undo if-match ip-precedence** *ip-precedence* &<1-8>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-precedence* | Specifies the IP precedence. | The value is an integer that ranges from 0 to 7. A larger value indicates a higher priority of packets. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match ip-precedence** command to classify packets based on the IP precedence so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

* After the **if-match ip-precedence** command is run, IP precedences are listed in ascending order.
* If you enter multiple IP precedences in the **if-match ip-precedence** command, a packet matches a rule as long as it matches one of the IP precedences, regardless of whether the relationship between traffic classification rules is AND or OR.
* In a traffic classifier where the relationship between rules is AND, the if-match dscp and **if-match ip-precedence** commands cannot be used simultaneously.
* If you run the **if-match ip-precedence** command in the same traffic classifier view multiple times, only the latest configuration takes effect.

Example
-------

# Configure a matching rule based on the IP precedence of 1 in the traffic classifier class1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier class1
[*HUAWEI-classifier-class1] if-match ip-precedence 1

```