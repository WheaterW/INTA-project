ftp server default-directory
============================

ftp server default-directory

Function
--------



The **ftp server default-directory** command sets the default working directory for FTP users.

The **undo ftp server default-directory** command cancels the setting of the default directory for FTP users.



By default, FTP users have no working directory.


Format
------

**ftp server default-directory** *directory*

**undo ftp server default-directory**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *directory* | Specifies the default working directory for FTP users. | The value is a character string in the format of [ <drive> ][ <path> ]. An absolute <path> name is a string of 1 to 255 characters. A relative <path> name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute <path> is in the format of <drive>[ <path> ], and a relative <path> is in the format of <path>. That is, a relative <path> is the root <path> of the current working <path>. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before you perform FTP operations on a file, you must specify the FTP working directory. Otherwise, you cannot use FTP to access a device.

The command takes effect for both ipv4 and ipv6 users.

**Precautions**

FTP users are classified as local AAA authentication users and remote authentication (RADIUS and HWTACACS) users.

* The **local-user ftp-directory** command must be run to specify the FTP working directory for local authentication users. Otherwise, local authentication users cannot use FTP to access the device.
* The FTP working directory for remote authentication users can be specified using the HWTACACS server. The **ftp server default-directory** command can also be used to specify the default FTP working directory for remote authentication users.The **ftp server default-directory** command applies only to remote authentication users.

Example
-------

# Set the default FTP working directory to flash:/
```
<HUAWEI> system-view
[~HUAWEI] ftp server default-directory flash:/

```