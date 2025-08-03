Verifying the Configuration
===========================

After parameters for dynamic MAC address entries are configured, you can check detailed information about the aging time and the MAC address learning limit rule.

#### Prerequisites

Parameters for dynamic MAC address entries have been configured.


#### Procedure

* Run the [**display mac-address aging-time**](cmdqueryname=display+mac-address+aging-time) command to check the aging time of dynamic MAC address entries.
* After a MAC address learning limit rule is configured, check the configuration as follows.
  
  
  
  | Type of a MAC Address Learning Limit Rule | Command for Checking the Rule |
  | --- | --- |
  | MAC address learning limit rule on an interface | [**display mac-limit**](cmdqueryname=display+mac-limit) {*interface-name* |*interface-type interface-number* } |
  | MAC address learning limit rule for a VLAN | [**display mac-limit**](cmdqueryname=display+mac-limit) **vlan** *vlan-id1* |
  | Global MAC address learning limit rule with a specified rule name | [**display mac-limit rule-name**](cmdqueryname=display+mac-limit+rule-name) [ *rule-name* ] |