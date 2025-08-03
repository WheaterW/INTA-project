Configuring a Basic ACL6
========================

Configuring a Basic ACL6

#### Context

A basic ACL6 defines packet filtering rules based on information such as source IPv6 addresses, fragment information, and time ranges.

To filter packets based only on source IPv6 addresses, configure a basic ACL6.

**When ACL6 rules are configured:**

* If the specified rule ID already exists and the new rule conflicts with the original, the original is replaced.
* Matching stops for a packet once the packet matches a rule in an ACL6.
* Many services that are not configured with ACL6 rules also occupy ACL6 resources. You can run the [**display system tcam service brief**](cmdqueryname=display+system+tcam+service+brief) command to check ACL6 resources occupied by services.

**When ACL6 rules are deleted:** The [**undo rule**](cmdqueryname=undo+rule) command can delete an ACL rule even if this rule is referenced. Before deleting a rule, run the [**display current-configuration | include acl**](cmdqueryname=display+current-configuration+%7C+include+acl) command to check whether the rule is being referenced.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a basic ACL6. You can create a numbered or named basic ACL6.
   
   
   * Create a numbered basic ACL6 and enter its view.
     ```
     [acl ipv6](cmdqueryname=acl+ipv6+number) [ number ] basic-acl6-number 
     ```
     
     The number of a basic ACL6 ranges from 2000 to 2999.
   * Create a named basic ACL6 and enter its view.
     
     ```
     [acl ipv6 name](cmdqueryname=acl+ipv6+name+basic) basic-acl6-name basic
     ```
3. (Optional) Configure an ACL6 step.
   
   
   ```
   [step](cmdqueryname=step) step-value
   ```
   
   
   
   The default ACL6 step is 5. Change the step value as required.
4. (Optional) Configure a description for the basic ACL6.
   
   
   ```
   [description](cmdqueryname=description) text
   ```
   
   The ACL6 description helps you understand and remember the functions or purpose of the ACL6.
5. Configure a rule for the basic ACL6.
   
   
   ```
   [rule](cmdqueryname=rule+name+permit+deny+fragment+source+any+time-range) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment | source { source-ipv6-address { prefix-length | source-wildcard } | source-ipv6-address/prefix-length | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
   ```
   
   In this example, only one permit or deny rule is configured. In actual configuration, you can configure multiple ACL6 rules and decide the matching order of the rules according to service requirements.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To configure a time-based basic ACL6, you must create a time range. For details, see [Creating a Time Range in Which an ACL6 Takes Effect](vrp_acl6_cfg_0009.html).
6. (Optional) Configure a description for the ACL6 rule.
   
   
   ```
   [rule](cmdqueryname=rule+description) rule-id description destext
   ```
   
   The ACL6 rule description helps you understand and remember the functions or purpose of the ACL6 rule.
   
   You must create a rule before you can configure a description for it.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Example

* Configure a packet filtering rule based on the source IPv6 address (host address).
  
  To permit packets from a host, add a rule to an ACL6. For example, to permit packets from the host at 2001:db8:1::1/128, create the following rule in ACL6 2001.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl ipv6 2001
  [*HUAWEI-acl6-basic-2001] rule permit source 2001:db8:1::1 128
  [*HUAWEI-acl6-basic-2001] quit
  [*HUAWEI] commit
  ```
* Configure a packet filtering rule based on the source IPv6 address segment.
  
  To permit packets from a host and reject packets from other hosts on the same network segment, configure rules in an ACL6. For example, to permit packets from the host at 2001:db8:1::2/128 and reject packets from other hosts on the network segment 2001:db8:1::1/64, configure the following rules in ACL6 2001.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl ipv6 2001
  [*HUAWEI-acl6-basic-2001] rule permit source 2001:db8:1::2 128
  [*HUAWEI-acl6-basic-2001] rule deny source 2001:db8:1::1 64
  [*HUAWEI-acl6-basic-2001] quit
  [*HUAWEI] commit
  ```

#### Verifying the Configuration

Run the [**display acl ipv6**](cmdqueryname=display+acl+ipv6+name+all) { *basic-acl6-number* | **name** *basic-acl6-name* | **all** } command to check the configuration of the basic ACL6.


#### Follow-up Procedure

Apply the basic ACL6 to a service module so that the basic ACL6 rules can be delivered and take effect.