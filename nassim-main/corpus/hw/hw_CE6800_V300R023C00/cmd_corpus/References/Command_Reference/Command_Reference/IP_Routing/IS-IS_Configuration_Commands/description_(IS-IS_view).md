description (IS-IS view)
========================

description (IS-IS view)

Function
--------



The **description** command configures a description for an IS-IS process.

The **undo description** command deletes the description of an IS-IS process.



By default, no description is configured for an IS-IS process.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Configures a description for an IS-IS process. | The value is a string of 1 to 80 case-sensitive characters, with digits, letters, and spaces supported. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The description configured for an IS-IS process using the **description** command is not advertised through an LSP, whereas the description configured for an IS-IS process using the **is-name** command is advertised through an LSP.


Example
-------

# Configure a description for IS-IS process 1 to It is a test.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] description It is a test

```