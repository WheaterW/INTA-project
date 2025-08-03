pm-server
=========

pm-server

Function
--------



The **pm-server** command creates a process serving the PM server and displays the view of the PM server created in the process. If there is an existing PM server view, the pm-server command displays the PM server view without creating a process.

The **undo pm-server** command deletes the created process.



By default, no process serving the PM server is created.


Format
------

**pm-server** *server-name*

**undo pm-server** *server-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *server-name* | Specifies the name of the process serving the PM server. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The string contains letters, digits, and underscores (\_), and must start with letters or digits. |



Views
-----

Performance management view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To upload generated performance statistics files to the PM server, run the pm-server command to create a process serving the PM server.

**Follow-up Procedure**

Configure the IP address and port number of the PM server, and the user name and password for connecting to the PM server. Then the PM server can obtain performance statistics files from the device through FTP or SFTP. The FTP protocol has security risks. You are advised to use the SFTP protocol.

**Precautions**

If a device is enabled to upload performance statistics files to a PM server, the process serving the PM server cannot be deleted.


Example
-------

# Create a process named a to serve the PM server.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] pm-server a
[*HUAWEI-pm-server-a]

```