reset ipv6 nd security timestamp
================================

reset ipv6 nd security timestamp

Function
--------



The **reset ipv6 nd security timestamp** command clears the timestamp in SEND messages on a specified interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ipv6 nd security timestamp** { *interface-name* | *interface-type* *interface-num* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Clears the timestamp in SEND messages on a specified the name of an interface. | - |
| *interface-type* *interface-num* | Clears the timestamp in SEND messages on a specified the type and number of an interface. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **reset ipv6 nd security timestamp** command clears the timestamp cached by the system when sending SEND messages. If further SEND messages are received, the system will discard the messages because no matching timestamp can be found in the cache. Exercise caution when running this command.


Example
-------

# Clear the timestamp in SEND messages on 100GE 1/0/1.
```
<HUAWEI> reset ipv6 nd security timestamp 100GE 1/0/1

```