upload auto
===========

upload auto

Function
--------



The **upload auto** command enables a device to automatically upload performance statistics files to a server.

The **undo upload auto** command disables a device from automatically uploading performance statistics files to a server.



By default, a device is disabled from automatically uploading performance statistics files to a server.


Format
------

**upload auto** *request-name*

**undo upload auto**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *request-name* | Specifies the name of a request for uploading performance statistics files to a server. | The value is a string of 1 to 31 characters. The string can contain letters, digits, and underscores (\_). The name must start with letters or digits. |



Views
-----

Statistics task view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable the device to automatically upload performance statistics files to the PM server at a specific interval, run the upload auto command. This configuration allows the device to automatically upload performance statistics files to the server.

**Prerequisites**

A request for uploading performance statistics files to the PM server has been created using the **upload-config** command.


Example
-------

# Create a request named req1 for uploading performance statistics files to the PM server named a.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics-task huawei
[*HUAWEI-pm-statistics-huawei] upload auto req1

```