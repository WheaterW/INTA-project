stp binding process link-share (Layer 2 interface view)
=======================================================

stp binding process link-share (Layer 2 interface view)

Function
--------



The **stp binding process link-share** command configures an interface to participate in status calculation in multiple MSTP processes.

The **undo stp binding process** command removes an interface from status calculation of a certain MSTP process.



By default, an MSTP interface participates in status calculation only in MSTP process 0.


Format
------

**stp binding process** *process-id1* **link-share**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id1* | Specifies the ID of an MSTP process. | The value is an integer ranging from 1 to 256. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a Layer 2 network running MSTP, the link used by multiple access rings is a public link. An interface on the public link participates in the spanning tree calculation for multiple MSTP processes and access rings. Each MSTP process calculates an interface status. As a result, the interface may have multiple status, and which status is used cannot be determined. To prevent this problem, run the **stp binding process link-share** command to add the interface to multiple MSTP processes. The interface always uses its status in MSTP process 0, although it participates in status calculation in multiple MSTP processes.



**Configuration Impact**

After the **stp binding process link-share** command is run on an interface, the interface will perform the following operations:

* Participates in status calculation of a specified MSTP process without affecting packet forwarding of this MSTP process.
* Participates in status calculation of MSTP process 0, affecting packet forwarding of this MSTP process.If the **stp binding process link-share** command is run more than once, all configurations take effect.

**Precautions**

* The interface configured with the **stp binding process link-share** command must be an interface on the public link between devices configured with the MSTP multi-process, but not an interface that connects a device to an access ring.
* If a process has a public link, the **stp enable** command must be run in the view of this process to enable MSTP globally.
* For an interface that is added to a process in link-share mode, you must run the **stp enable** command in the interface view to enable MSTP.
* For an interface that is added to a process in link-share mode, the interface participates in status calculation of MSTP process 0. You must run the **stp enable** command to enable MSTP for process 0.


Example
-------

# Configure an interface to participate in status calculation in MSTP processes 1 and 2.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] quit
[*HUAWEI] stp process 2
[*HUAWEI-mst-process-2] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] stp enable
[*HUAWEI-100GE1/0/1] stp binding process 1 link-share
[*HUAWEI-100GE1/0/1] stp binding process 2 link-share

```