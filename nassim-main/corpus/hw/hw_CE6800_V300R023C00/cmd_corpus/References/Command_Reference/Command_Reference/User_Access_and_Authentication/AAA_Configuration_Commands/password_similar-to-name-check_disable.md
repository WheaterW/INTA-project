password similar-to-name-check disable
======================================

password similar-to-name-check disable

Function
--------

The **password similar-to-name-check disable** command disables the similarity check between local administrator passwords and user names.

The **undo password similar-to-name-check disable** command enables the similarity check between local administrator passwords and user names.

By default, the similarity check between the local administrator password and user name is enabled.



Format
------

**password similar-to-name-check disable**

**undo password similar-to-name-check disable**



Parameters
----------

None


Views
-----

Local administrator password policy view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To prevent accounts from being stolen due to simple passwords, run this command to configure the local administrator password not to repeat or reverse the user name.

**Precautions**

After the function of checking the similarity between the local administrator password and user name is disabled, you can configure a password that repeats or reverses the user name. Such a password, however, has security risks.



Example
-------

# Enable the similarity check between the local administrator password and user name.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-aaa-user password policy administrator
[~HUAWEI-aaa-lupp-admin] undo password similar-to-name-check disable

```