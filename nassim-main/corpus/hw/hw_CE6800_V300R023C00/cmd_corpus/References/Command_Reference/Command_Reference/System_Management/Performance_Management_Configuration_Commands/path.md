path
====

path

Function
--------



The **path** command configures the destination path where performance statistics files are uploaded on a PM server.

The **undo path** command deletes the configured destination path.



By default, performance statistics files are uploaded to the default path on a PM server.


Format
------

**path** *destination-path*

**undo path**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *destination-path* | Specifies the destination path where performance statistics files are uploaded on a PM server. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

PM server view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To upload performance statistics files to a specific path on the PM server, run the path command to configure the destination path.


Example
-------

# Configure the destination path where performance statistics files are uploaded on the PM server.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] pm-server a
[*HUAWEI-pm-server-a] path /db

```