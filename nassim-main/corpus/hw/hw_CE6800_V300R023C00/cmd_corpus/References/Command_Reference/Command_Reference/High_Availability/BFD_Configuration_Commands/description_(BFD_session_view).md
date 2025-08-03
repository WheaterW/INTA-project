description (BFD session view)
==============================

description (BFD session view)

Function
--------



The **description** command configures a description for a BFD session.

The **undo description** command deletes the description configured for a BFD session.



By default, no description is configured for a BFD session.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies a description for a BFD session. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |



Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To identify a BFD session, run the **description** command to configure a description for the BFD session. It is recommended that you configure a distinctive description for the BFD session.

**Prerequisites**

A BFD session has been created.

**Configuration Impact**

After the description of a BFD session is deleted, it will be inconvenient to identify a BFD session.

**Precautions**

* If the **description** command is run to reconfigure a description for a BFD session that already has a description, the original description is overridden and the system does not display any messages.
* The **description** command can be configured when the BFD session is being set up or after the BFD session goes Up and the BFD session view is displayed.

Example
-------

# Configure a description for the BFD session named session.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd session bind peer-ip 10.10.20.2
[*HUAWEI-bfd-session-session] quit
[*HUAWEI] bfd session
[*HUAWEI-bfd-session-session] description DeviceA_to_DeviceC

```