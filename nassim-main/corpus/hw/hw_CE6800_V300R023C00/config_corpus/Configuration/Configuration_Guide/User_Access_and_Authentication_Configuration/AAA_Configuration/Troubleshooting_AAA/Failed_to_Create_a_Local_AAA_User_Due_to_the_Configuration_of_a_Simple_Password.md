Failed to Create a Local AAA User Due to the Configuration of a Simple Password
===============================================================================

Failed to Create a Local AAA User Due to the Configuration of a Simple Password

#### Fault Symptom

A local AAA user fails to be created, and an error message is displayed.


#### Possible Causes

* The password length does not meet requirements.
* The password does not meet complexity requirements.

#### Troubleshooting Procedure

Rectify the fault based on the error message displayed on the device. The following table describes the troubleshooting methods.

| Message | Possible Causes and Troubleshooting Method | Solution |
| --- | --- | --- |
| **Error: The password length must range from 8 to 128.** | The minimum length of a local user password is limited, but the configured password length is less than the minimum length.  By default, a local user password contains 8 to 128 characters.  Run the **display this** command in the AAA view. If the **password min-length** *password-min-length* command is configured, the length of the local user password ranges from the value specified by *password-min-length* to 128, in characters. | During the creation of a local user, the configured password length must be greater than or equal to the minimum password length configured on the device. |
| **Error: The password is composed of digit, lowercase letter, uppercase letter or other characters, and it must meet 4 of them at leas****t.** | The password complexity check function has been enabled on the device using the **password complexity** { **two-of kinds** | **three-of-kinds** | **four-of kinds** } command. By default, a password must contain four types of the following characters: uppercase letters, lowercase letters, digits, and special characters. The password configured during the creation of a local user does not meet the preceding requirements.  NOTE:   * After the password complexity check function is enabled using the **password complexity** { **two-of kinds** | **three-of-kinds** | **four-of kinds** } command, the device checks whether a password contains at least four types of characters by default. * You can also configure the device to check whether a password contains at least three or two types of characters. The password configured during the creation of a local user does not meet the preceding requirements, and either of the following messages is displayed:   + **Error: The password is composed of digit, lowercase letter, uppercase letter or other characters, and it must meet 3 of them at leas****t**.   + **Error: The password is composed of digit, lowercase letter, uppercase letter or other characters, and it must meet 2 of them at leas****t.** | By default, during the creation of a local user, the configured password must contain the following characters: uppercase letters, lowercase letters, digits, and special characters (excluding question marks and spaces). Spaces are allowed in the password if the password is enclosed in quotation marks.   * If **three-of-kinds** is specified in the **password complexity** command during the configuration of the password complexity check function, the password configured during the creation of a local user must contain three of the four types of characters. * If **two-of kinds** is specified in the **password complexity** command during the configuration of the password complexity check function, the password configured during the creation of a local user must contain two of the four types of characters. |
| **Error: The password cannot be the same as the user's name or its inversion.** | The function of checking whether the password repeats or reverses the user name is enabled on the device. | During the creation of a local user, the configured password cannot contain the user name or its reverse. |