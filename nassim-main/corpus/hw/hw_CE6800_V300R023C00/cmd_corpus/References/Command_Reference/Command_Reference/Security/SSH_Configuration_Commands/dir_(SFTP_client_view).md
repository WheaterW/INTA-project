dir (SFTP client view)
======================

dir (SFTP client view)

Function
--------



The **dir** command displays the list of directories and files in the specified directory of the remote machine.



By default, the details about the current directory are displayed.


Format
------

**dir** [ *remote-directory* [ *local-filename* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *remote-directory* | Specifies the remote directory name. | The value is a string of 1 to 255 case-sensitive characters without a blank space. |
| *local-filename* | Specifies the saved local file name. | The value is a string of 1 to 255 case-sensitive characters without a blank space. |



Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **dir** command to query files in a specified directory on the SFTP server. After the local-filename parameter is set, the file content can be saved to a local file.

**Precautions**



The Flash has internal partitions. The remaining space information shown in the dir flash: command output greatly differs from that shown in the dir flash:/logfile/ command output. Before you install the target system software, run the dir flash: command to verify whether the remaining space is sufficient.




Example
-------

# Query the directory names.
```
<HUAWEI> system-view
[~HUAWEI] sftp 1.1.1.1
Trying 1.1.1.1 ...
Press CTRL + K to abort
Connected to 1.1.1.1.
220 VRPV8 SFTP service ready.
User(1.1.1.1:(none)):sftp
331 Password required for sftp.
Enter password:
sftp-client> dir

```

# Query the directory named new\_folder on the SFTP server.
```
<HUAWEI> system-view
[~HUAWEI] sftp 1.1.1.1
Trying 1.1.1.1 ...
Press CTRL + K to abort
Connected to 1.1.1.1.
220 VRPV8 SFTP service ready.
User(1.1.1.1:(none)):sftp
331 Password required for sftp.
Enter password:
sftp-client> dir new_folder

```

# Query the new\_folder and save the query result in the file output.txt.
```
<HUAWEI> system-view
[~HUAWEI] sftp 1.1.1.1
Trying 1.1.1.1 ...
Press CTRL + K to abort
Connected to 1.1.1.1.
220 VRPV8 SFTP service ready.
User(1.1.1.1:(none)):sftp
331 Password required for sftp.
Enter password:
sftp-client> dir new_folder output.txt

```