display configuration rollback result
=====================================

display configuration rollback result

Function
--------



The **display configuration rollback result** command displays the configurations that fail to be rolled back and the messages displayed when configuration commands are run.




Format
------

**display configuration rollback result**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

During the configuration rollback operation, some configurations may fail to be retrieved, and some configurations trigger the generation of prompt messages. You can run the display configuration rollback result command to view relevant information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the latest configuration rollback failure and information about the commit failure during the configuration rollback.
```
<HUAWEI> display configuration rollback result
!warning information
+ ftp server enable
Warning: FTP is not a secure protocol, it is recommended to use SFTP.
!commit error information
Error: Some labels in the label range were used. Delete unwanted services to release the labels or check for other available label ranges.
!warning information
+ ftp server enable
Warning: FTP is not a secure protocol, it is recommended to use SFTP.
!commit error information
Error: Some labels in the label range were used. Delete unwanted services to release the labels or check for other available label ranges.
!There are still several differences as follow:
- FTP server enable
  #
- FTP server-source all-interface
  #
+ ftp server enable
  #
+ undo FTP server-source all-interface
  #
+ segment-routing
  #
+  cost-style wide
+  segment-routing global-block 50000 80000
  #

```

# Display the result of the most recent successful configuration rollback operation during which no prompt message is generated.
```
<HUAWEI> display configuration rollback result

```

# Display failure messages and prompt messages during the latest configuration rollback operation.
```
<HUAWEI> display configuration rollback result
!warning information
  interface 10GE1/0/5
+  ipv6 enable
Warning: The configuration is successful. Enable global BFD to validate the configuration.
!There are still several differences as follow:
  #
  interface 10GE1/0/2
- ip address 3.3.3.3 255.255.255.0
+  ip address 4.4.4.4 255.255.255.0
  #

```

**Table 1** Description of the **display configuration rollback result** command output
| Item | Description |
| --- | --- |
| !warning information | Prompt messages during the configuration rollback operation. |
| + | A new configuration.  For each modified configuration, both "-" indicating the deleted configuration and "+" indicating the created configuration are displayed. |
| !There are still several differences as follow: | Information about configurations that fail to be rolled back. |
| - | A deleted configuration.  For each modified configuration, both "-" indicating the deleted configuration and "+" indicating the created configuration are displayed. |