set authentication password
===========================

set authentication password

Function
--------



The **set authentication password** command sets a login password.

The **undo set authentication password** command deletes the login password.



By default:

* After a user logs in to a device for the first time, the device displays a message indicating that an authentication password has been set for the user. This password is called a local authentication password.
* When a user logs in to a device for the first time and has not set an authentication password, no authentication password exists for the user on the device.


Format
------

**set authentication password**

**set authentication password cipher** *password*

**undo set authentication password**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cipher** *password* | Specifies the password for the user interface. The authentication password displayed in ciphertext is irreversible. | * When cipher is not entered, password input is in man-machine interaction mode, and the system does not display the entered password. The password is a string of 8 to 16 case-sensitive characters. The password must contain at least two of the following characters: upper-case character, lower-case character, digit, and special character.  Special character except the question mark (?) and space. However, when double quotation marks are used around the password, spaces are allowed in the password.    + Double quotation marks cannot contain double quotation marks if spaces are used in a password.   + Double quotation marks can contain double quotation marks if no space is used in a password.For example, the password "a123"45"" is valid, but the password "a 123"45"" is invalid.   + When cipher is entered, the password is displayed in either plaintext or ciphertext during input.   + When being input in plaintext, the password requirements are the same as those when cipher is not entered. When you input a password in simple text, the system displays the password in simple text mode, which brings risks.   + When being input in ciphertext, the password must be a string of 48 to 128 consecutive characters. The password is displayed in ciphertext in the configuration file regardless of whether it is input in plaintext or cipher text. |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, password authentication is not required when you log in to a device through a console port, but password authentication is required when you log in to a device through a VTY user interface (for example, STelnet). Otherwise, you cannot log in to the device. You can run this command to set an authentication password to ensure that authorized users can log in to the device securely.

* If you run the **undo authentication-mode** command to cancel the authentication mode for logging in to the user interface, you cannot run the **set authentication password** command to change the authentication password.
* If you run the **protocol inbound** command to set the protocol supported by the user interface to SSH, the system displays an error message when you run this command. In this case, you must run the **protocol inbound** command to change the protocol supported by the user interface.

**Prerequisites**

Before using the **set authentication password** command, ensure that the authentication mode in the user interface is password. If the authentication mode of the user interface is not password, run the **authentication-mode password** command in the user interface view to change the mode to password in the VTY user interface view.

**Precautions**

* If the command is run more than once, the latest configuration overrides the previous one. When logging in to the system again, the user must enter the current password to pass the authentication.
* The password authentication mode has security risks. The AAA authentication mode is recommended. Run the **authentication-mode aaa** command in the VTY user interface view to change the authentication mode to AAA.
* After the weak password dictionary maintenance function is enabled, the passwords defined in the weak password dictionary cannot be used. You can run the **display security weak-password-dictionary** command to view the passwords.
* To ensure device security, change the password periodically.


Example
-------

# Change the local authentication password of VTY 0 to VTY 4 to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0 4
[~HUAWEI-ui-vty0-4] authentication-mode password
[*HUAWEI-ui-vty0-4] set authentication password
Please configure the login password (8-16)
Enter password:
Confirm password:

```

# Change the local authentication password of user interface console 0 to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] authentication-mode password
[*HUAWEI-ui-console0] set authentication password cipher YsHsjx_202206

```