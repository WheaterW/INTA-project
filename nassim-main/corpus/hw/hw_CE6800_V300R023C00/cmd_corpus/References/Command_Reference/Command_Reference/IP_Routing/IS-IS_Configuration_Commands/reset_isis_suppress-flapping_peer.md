reset isis suppress-flapping peer
=================================

reset isis suppress-flapping peer

Function
--------



The **reset isis suppress-flapping peer** command configures an interface to exit IS-IS neighbor relationship flapping suppression.




Format
------

**reset isis** *process-id* **suppress-flapping** **peer** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ **notify-peer** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| **interface** *interface-name* | Specifies an interface name. | - |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| **notify-peer** | Instructs neighbors to exit from IS-IS neighbor relationship flapping suppression too. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Interfaces exit from flapping suppression in the following scenarios:

* The suppression timer expires.
* The corresponding IS-IS process is reset.
* An IS-IS neighbor is reset using the **reset isis peer** command.
* IS-IS neighbor relationship flapping suppression is disabled globally using the suppress-flapping peer disable (IS-IS) command in the IS-IS view.
* The **reset isis suppress-flapping peer** command is run.
* Suppression is aborted forcibly using the **reset isis suppress-flapping peer notify-peer** command on the remote device.

Example
-------

# Configure interfaces to exit IS-IS neighbor relationship flapping suppression.
```
<HUAWEI> reset isis 1 suppress-flapping peer

```