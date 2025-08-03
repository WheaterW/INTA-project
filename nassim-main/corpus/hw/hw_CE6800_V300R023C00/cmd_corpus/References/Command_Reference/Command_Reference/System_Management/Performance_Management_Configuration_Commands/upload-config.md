upload-config
=============

upload-config

Function
--------



The **upload-config** command creates a request for uploading performance statistics files to a specified PM server.

The **undo upload-config** command deletes a request for uploading performance statistics files to a specified PM server.



By default, no request for uploading performance statistics files to a specified PM server is created.


Format
------

**upload-config** *request-name* **server** *server-name*

**undo upload-config** *request-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *request-name* | Specifies the name of a request for uploading performance statistics files. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The string contains letters, digits, and underscores (\_), and must start with letters or digits. |
| **server** *server-name* | Specifies the IP address of the PM server. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The string contains letters, digits, and underscores (\_), and must start with letters or digits. |



Views
-----

Performance management view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to upload performance statistics files to a PM server, run the upload-config command to create a request for uploading.

**Follow-up Procedure**

Enable the device to upload performance statistics files to the PM server.


Example
-------

# Create a request named req1 for uploading performance statistics files to the PM server named a.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics enable
[*HUAWEI-pm] upload-config req1 server a

```