ftp server ip-block reactive
============================

ftp server ip-block reactive

Function
--------



The **ftp server ip-block reactive** command sets a period after which the system automatically unlocks an IP address of a user.

The **undo ftp server ip-block reactive** command restores the default period.



By default, the period is 5 minutes.


Format
------

**ftp server ip-block reactive** *reactive-period*

**undo ftp server ip-block reactive** [ *reactive-period* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *reactive-period* | Specifies a period after which the system automatically unlocks an IP address of user. | The value is an integer ranging from 1 to 1000, in minute. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To set a period after which the system automatically unlocks an IP address of user, run the ftp server ip-block reactive command. A locked IP address of user cannot access the device through FTP. The system automatically unlocks the IP address of user until the unlocking period expires. This improves device security.To manually unlock the IP address of user, run the activate ftp server ip-block ip-address command.


Example
-------

# Set the period after which the system automatically unlocks the IP address of user to 50 minutes.
```
<HUAWEI> system-view
[~HUAWEI] ftp server ip-block reactive 50

```