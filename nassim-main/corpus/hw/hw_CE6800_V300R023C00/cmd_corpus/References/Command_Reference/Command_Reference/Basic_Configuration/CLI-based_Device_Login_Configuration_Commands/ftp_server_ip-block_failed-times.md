ftp server ip-block failed-times
================================

ftp server ip-block failed-times

Function
--------



The **ftp server ip-block failed-times** command sets the maximum number of consecutive FTP authentication failures within a specified period. If the number is reached, the system locks out the IP address of user.

The undo ftp server ip-block failed-times command restores the maximum number of consecutive FTP authentication failures and the period in which consecutive authentication failures are counted to default values.



By default, the maximum number of consecutive FTP authentication failures before the IP address of user lockout is 6, and the period is 5 minutes.


Format
------

**ftp server ip-block failed-times** *failed-times* **period** *period*

**undo ftp server ip-block failed-times** *failed-times* **period** *period*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *failed-times* | Specifies the maximum number of consecutive FTP authentication failures before the IP address of user lockout. | The value is an integer ranging from 1 to 10. |
| **period** *period* | Specifies a period in which consecutive FTP authentication failures are counted. | The value is an integer ranging from 1 to 120, in minutes. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To set the maximum number of consecutive authentication failures withina specified period, run the ftp server ip-block failed-times command.If the number is reached, the system locks out the IP address of user, which prevents the user from accessing the device through FTP. The system automatically unlocks the IP address of user until the unlocking period expires. This improves device security.To manually unlock the IP address of user, run the activate ftp server ip-block ip-address command.


Example
-------

# Set the maximum number of consecutive authentication failures before the IP address of user lockout to 3 and the period in which consecutive FTP authentication failures are counted to 6 minutes.
```
<HUAWEI> system-view
[~HUAWEI] ftp server ip-block failed-times 3 period 6

```