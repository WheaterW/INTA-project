min-echo-rx-interval
====================

min-echo-rx-interval

Function
--------



The **min-echo-rx-interval** command configures a minimum interval at which one-arm BFD echo session packets are received.

The **undo min-echo-rx-interval** command restores the default minimum interval at which one-arm BFD echo session packets are received.



By default, the minimum interval is 1000 ms.


Format
------

**min-echo-rx-interval** *interval*

**undo min-echo-rx-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the minimum interval at which one-arm BFD echo session packets are received. | The value is an integer that ranges from 3 to 1000, in milliseconds. |



Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After creating a one-arm BFD echo session, you can configure a minimum interval at which one-arm BFD echo session packets are received.

**Prerequisites**



A one-arm BFD echo session has been configured using the **bfd one-arm-echo** command.




Example
-------

# Set the minimum interval at which one-arm BFD echo session packets are received to 100 ms.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ip address 10.10.20.1 24
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd session bind peer-ip 10.10.20.2 interface 100GE 1/0/1 one-arm-echo
[*HUAWEI-bfd-session-session] quit
[*HUAWEI] bfd session
[*HUAWEI-bfd-session-session] min-echo-rx-interval 100

```