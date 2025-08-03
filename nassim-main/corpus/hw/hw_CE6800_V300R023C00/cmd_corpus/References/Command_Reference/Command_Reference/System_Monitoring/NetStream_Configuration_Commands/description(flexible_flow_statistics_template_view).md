description(flexible flow statistics template view)
===================================================

description(flexible flow statistics template view)

Function
--------



The **description** command configures a description for a flexible flow.

The **undo description** command deletes a description for a flexible flow.



By default, no flexible flow description is configured.


Format
------

**description** *description-information*

**undo description** [ *description-information* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description-information* | Specifies the description for a flexible flow. | The value is a string of 1 to 80 characters, spaces supported. |



Views
-----

IPv4 flexible flow statistics template view,IPv6 flexible flow statistics template view,VXLAN flexible flow statistics template view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Multiple flexible flows can be configured, each of which can be assigned matching and collected fields. To help rapidly understand a flexible flow, run the **description** command to configure a description for each flow. For example, a description defines some fields or meanings of fields in packets for a flexible flow.

**Configuration Impact**

If a description has been configured for a flexible flow, running the **description** command override the previous description.


Example
-------

# Configure the flexible flow description as ipRecord.
```
<HUAWEI> system-view
[~HUAWEI] netstream record test ip
[*HUAWEI-netstream-record-ipv4-test] description ipRecord

```