isis enable
===========

isis enable

Function
--------



The **isis enable** command enables IS-IS on an interface and specifies the IS-IS process ID to be associated with the interface.

The **undo isis enable** command disables IS-IS from an interface and dissociates the IS-IS process from the interface.



By default, IS-IS is not enabled on an interface.


Format
------

**isis enable**

**isis enable** *process-id*

**undo isis enable**

**undo isis enable** *process-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value ranges from 1 to 4294967295. The default value is 1. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an IS-IS process is configured in the system view, run the **isis enable** command to enable IS-IS on interfaces and associate these interfaces with the IS-IS process.

**Prerequisites**

An IS-IS process has been created using the **isis** command in the system view.

**Precautions**



The next hop of an SR route cannot be recursed to a tunnel interface. Therefore, when an SRGB-enabled IS-IS process is enabled on an FA tunnel interface, SR-labeled traffic may be discarded.If the **multi-instance enable** command is run in the IS-IS view to configure an IS-IS process as a multi-instance process, to disable IS-IS on an interface, you must run the **undo isis enable process-id** command, in which, process-id specifies the multi-instance process to be deleted.If an EVPL instance or a local CCC is bound to an interface, the interface becomes a Layer 2 interface and IS-IS packets cannot be transparently transmitted through the interface. If IS-IS is enabled on the interface, the establishment of the IS-IS neighbor relationship that forwards packets through the link is affected.




Example
-------

# Create IS-IS process 1 and activate this process on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] network-entity 10.0001.1010.1020.1030.00
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1

```