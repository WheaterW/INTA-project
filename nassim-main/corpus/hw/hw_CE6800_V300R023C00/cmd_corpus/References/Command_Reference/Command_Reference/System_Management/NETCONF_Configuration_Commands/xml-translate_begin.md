xml-translate begin
===================

xml-translate begin

Function
--------



The **xml-translate begin** command accesses the CLI-to-XML translation mode.




Format
------

**xml-translate begin**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

CLI and NETCONF are two device management models. To access the CLI-to-XML translation mode, run the xml-translate begin command so that configuration commands can be translated into XML packets in the NETCONF YANG model.To exit the translation mode and enter the user view, run the quit or return command.The xml-translate function is used for the NMS user to obtain packets more conveniently. NETCONF tries to translate packets from the result. The effect of packets may be different from that of commands.

**Configuration Impact**

After you run this command to access the translation mode, the user prompt is changed to [& HUAWEI].

**Follow-up Procedure**

In the translation mode, after the configuration commands to be translated are executed, run either of the following commands as needed:

* To translate the configuration commands to XML packets in the NETCONF YANG model, run the **xml-translate end** command.
* To stop the CLI-to-XML translation and exit the translation mode, run the **xml-translate abort** command.

**Precautions**

Only administrator users can run the xml-translate begin command.After this command is run, the current running configuration database will be locked, and other users cannot commit configurations to the database.During the translation, do not install or uninstall the patch. Otherwise, the patch fails to be installed or uninstalled.If the translation takes more than 1 hour, an error is reported when the translation times out. In this case, a message is displayed, but the translation content is not displayed.This function supports only the configuration commands that meet the following conditions:

1. The configuration command is used in the Admin-VS.
2. The configuration command is a two-phase one.
3. The configuration command is different from the current device configuration.
4. The configuration command supports YANG.This command can be used to identify whether the configuration command supports YANG. The translated YANG model packet is for reference only. Modify the command based on the model packet example in the YANG API.The xml-translate command preferentially ensures correct translation of forward delivery and reverse deletion. It is not recommended that the same object be repeatedly created and deleted before translation.When the xml-translate command is used to translate command lines to YANG model packets, outdated nodes are ignored.Ignoring outdated nodes does not affect functions. You can run the display netconf data-model module name <nodule-name> format yin command in the diagnostic view to query outdated nodes. If statue is deprecated, outdated nodes are displayed.

Example
-------

# Access the CLI-to-XML translation mode.
```
<HUAWEI> system-view
[~HUAWEI] xml-translate begin
Warning: The running database will be locked when you enter the CLI-to-XML translate mode. Continue? [Y/N]:y

```