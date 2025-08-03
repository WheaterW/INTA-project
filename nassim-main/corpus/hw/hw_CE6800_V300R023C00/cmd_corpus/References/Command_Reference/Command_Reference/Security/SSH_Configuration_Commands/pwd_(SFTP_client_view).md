pwd (SFTP client view)
======================

pwd (SFTP client view)

Function
--------



The **pwd** command displays the present working directory on the remote SFTP server.




Format
------

**pwd**


Parameters
----------

None

Views
-----

SFTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After executing the **pwd** command, if the working directory is incorrect, then execute the cd command to modify the working directory of SFTP client.


Example
-------

# Display the working directory on the remote SFTP server.
```
<HUAWEI> system-view
[~HUAWEI] sftp 10.1.1.1
Trying 10.1.1.1 ...
Press CTRL+K to abort
Connected to 10.1.1.1 ...
Please input the username: client001
Enter password:   
sftp-client> pwd
/
sftp-client> mkdir test
Info: Succeeded in creating a directory.sftp-client> cd /test
/test
sftp-client> pwd
/test

```