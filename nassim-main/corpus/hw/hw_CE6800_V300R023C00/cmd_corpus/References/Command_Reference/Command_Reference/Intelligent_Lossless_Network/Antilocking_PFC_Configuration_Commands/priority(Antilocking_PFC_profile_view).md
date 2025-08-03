priority(Antilocking PFC profile view)
======================================

priority(Antilocking PFC profile view)

Function
--------



The **priority** command enables antilocking PFC for a specified priority queue.

The **undo priority** command disables antilocking PFC for a specified priority queue.



By default, antilocking PFC is not enabled for any priority queue.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6885-SAN.



Format
------

**priority** *priority* &<1-4>

**undo priority** [ *priority* ] &<0-4>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies the priority. | The value is an integer ranging from 0 to 7. |



Views
-----

Antilocking PFC profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to enable antilocking PFC for a specified priority queue and then run the **abs-pfc enable** command to enable antilocking PFC on an interface.


Example
-------

# Enable antilocking PFC for priority queues 3 and 5.
```
<HUAWEI> system-view
[~HUAWEI] abs-pfc profile myabspfc
[*HUAWEI-abs-pfc-myabspfc] priority 3 5

```