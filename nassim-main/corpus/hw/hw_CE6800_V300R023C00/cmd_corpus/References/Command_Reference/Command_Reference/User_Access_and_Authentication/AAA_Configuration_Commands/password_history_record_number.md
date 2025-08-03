password history record number
==============================

password history record number

Function
--------

The **password history record number** command sets the maximum number of historical passwords recorded for each user.

The **undo password history record number** command restores the default maximum number of historical passwords recorded for each user.

By default, a maximum of 10 historical passwords can be recorded for each user in the administrator password policy view and a maximum of 5 historical passwords can be recorded for each user in the common access user password policy view.



Format
------

**password history record number** *number*

**undo password history record number**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Indicates the maximum number of historical passwords recorded for each user.  If the value is set to 0, the device will not check whether a changed password is the same as any historical password. | The value is an integer that ranges from 0 to 12. In the administrator password policy view, the default value is 10. In the common access user password policy view, the default value is 5. |




Views
-----

Local access user password policy view,Local administrator password policy view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To improve password security, it is not recommended that you use a previously used password. You can set the maximum number of historical passwords recorded for each user. When a user changes the password, the device compares the new password against the historical passwords stored on the device. If the new password is the same as a stored password, the device displays an error message to prompt the user that password change fails.

**Precautions**

When the number of recorded historical passwords reaches the maximum value, the later password will overwrite the earliest password on the device.

After the historical password recording function is disabled, the device does not record historical passwords; however, the passwords that have been stored are not deleted.

Example
-------

# Set the maximum number of historical passwords recorded for each administrator to 10.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-aaa-user password policy administrator
[*HUAWEI-aaa-lupp-admin] password history record number 10

```