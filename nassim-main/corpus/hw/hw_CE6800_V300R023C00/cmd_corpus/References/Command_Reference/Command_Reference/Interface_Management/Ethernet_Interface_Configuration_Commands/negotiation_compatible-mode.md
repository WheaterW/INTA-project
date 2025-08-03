negotiation compatible-mode
===========================

negotiation compatible-mode

Function
--------



The **negotiation compatible-mode** command switches the working mode of an interface to compatible mode.

The undo negotiation compatible-mode command switches the working mode of an interface to incompatible mode.



By default, an interface works in incompatible mode.


Format
------

**negotiation compatible-mode** [ **precursor** *precursor-value* **postcursor** *postcursor-value* ]

**undo negotiation compatible-mode** [ **precursor** *precursor-value* **postcursor** *postcursor-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **precursor** *precursor-value* | Set a pre-emphasis value before data transition. | The value is an integer that ranges from -15 to 15. |
| **postcursor** *postcursor-value* | Set a pre-emphasis value after data transition. | The value is an integer that ranges from -15 to 15. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Auto-negotiation may fail on an interface in incompatible mode. If the interface goes Down due to an auto-negotiation failure, run the **negotiation compatible-mode** command to switch the interface to compatible mode and check whether the interface is Up.Before running this command, you are advised to contact technical support engineers to determine whether to use this command and set the parameters. Incorrect use of this command may cause an interface in the Up state to go Down.The CE6820H, CE6820S, CE6820H-K, CE6863H, CE6863H-K, CE6881H, and CE6881H-K do not support this command.



**Precautions**



This command can be run only on interfaces that have copper cables installed or have copper cables pre-configured and support auto-negotiation.




Example
-------

# Configure 100GE1/0/1 to work in compatible mode.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] negotiation compatible-mode
Warning: The operation may cause port down. Continue? [Y/N]:Y

```

# Configure 100GE1/0/1 to work in incompatible mode.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo negotiation compatible-mode
Warning: The operation may cause port down. Continue? [Y/N]:Y

```