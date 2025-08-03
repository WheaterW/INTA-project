nqa jitter tag-version
======================

nqa jitter tag-version

Function
--------



The **nqa jitter tag-version** command sets the packet version for a jitter test instance.

The **undo nqa jitter tag-version** command restores the default configuration.



By default, the packet version in a jitter test instance is 1.


Format
------

**nqa jitter tag-version** *version-number*

**undo nqa jitter tag-version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *version-number* | Specifies the version of packets. | The value can be 1 or 2. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Packet statistics in version 2 is more accurate than those in version 1. Version 2 is recommended.

**Precautions**

If the nqa-jitter tag-version command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the packet version for a jitter test instance to 2.
```
<HUAWEI> system-view
[~HUAWEI] nqa jitter tag-version 2

```