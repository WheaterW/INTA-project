xml-translate end
=================

xml-translate end

Function
--------



The **xml-translate end** command translates configuration commands into XML packets in the NETCONF YANG model.




Format
------

**xml-translate end**


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

After the configuration commands to be translated are executed, to start the CLI-to-XML translation, run the **xml-translate end** command. The translation mode quits after the translation is complete.

**Prerequisites**

The CLI-to-XML translation mode has been accessed using the **xml-translate begin** command, and all the configuration commands to be translated have been executed.

**Configuration Impact**

After the xml-translate abort command is run, the current running configuration database is unlocked, and the system view is returned.


Example
-------

# Translate configuration commands to XML packets in the NETCONF YANG model.
```
<HUAWEI> system-view
[~HUAWEI] xml-translate begin
Warning: The running database will be locked when you enter the CLI-to-XML translate mode.Continue? [Y/N]:y
[&HUAWEI] acl 2001
[&HUAWEI-acl4-basic-2001] quit
[&HUAWEI] xml-translate end
Info: It will take a long time if the data is too much, press CTRL_C to break.
...
<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="cli2xml-0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <edit-config>
    <target>
      <candidate/>
    </target>
    <default-operation>none</default-operation>
    <test-option>set</test-option>
    <error-option>rollback-on-error</error-option>
    <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <acl xmlns="urn:huawei:yang:huawei-acl">
        <groups>
          <group nc:operation="merge">
            <identity>2001</identity>
            <type>basic</type>
          </group>
        </groups>
      </acl>
    </config>   
  </edit-config>
</rpc>

```