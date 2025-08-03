Configuring a Basic ACL
=======================

Configuring a Basic ACL

#### Context

A basic ACL defines packet filtering rules based on information such as source IPv4 addresses, fragment information, and time ranges.

To filter packets based only on source IPv4 addresses, configure a basic ACL.

**When ACL rules are configured:**

* If the specified rule ID already exists and the new rule conflicts with the original, the original is replaced.
* Matching stops for a packet once the packet matches a rule in an ACL.
* Many services that are not configured with ACL rules also occupy ACL resources. You can run the [**display system tcam service brief**](cmdqueryname=display+system+tcam+service+brief) command to check ACL resources occupied by services.

**When ACL rules are deleted:** The [**undo rule**](cmdqueryname=undo+rule) command can delete an ACL rule even if this rule is referenced. Before deleting a rule, run the [**display current-configuration | include acl**](cmdqueryname=display+current-configuration+%7C+include+acl) command to check whether the rule is being referenced.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a basic ACL. You can create a numbered or named basic ACL.
   
   
   * Create a numbered basic ACL and enter its view.
     ```
     [acl](cmdqueryname=acl+number) [ number ] basic-acl-number  
     ```
     
     The number of a basic ACL ranges from 2000 to 2999.
   * Create a named basic ACL and enter its view.
     
     ```
     [acl name](cmdqueryname=acl+name+basic) basic-acl-name basic 
     ```
3. (Optional) Configure an ACL step.
   
   
   ```
   [step](cmdqueryname=step) step-value
   ```
   
   
   
   The default ACL step is 5. Change the step value as required.
4. (Optional) Configure a description for the basic ACL.
   
   
   ```
   [description](cmdqueryname=description) text
   ```
   
   The ACL description helps you understand and remember the functions or purpose of the ACL.
5. Configure a rule for the basic ACL.
   
   
   ```
   [rule](cmdqueryname=rule+name+permit+deny+fragment-type+fragment+source+0+any) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment-type fragment | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
   ```
   
   In this example, only one permit or deny rule is configured. In actual configuration, you can configure multiple ACL rules and decide the matching order of the rules according to service requirements.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To configure a time-based basic ACL, you must create a time range. For details, see [Creating a Time Range in Which an ACL Takes Effect](vrp_acl_cfg_0009.html).
6. (Optional) Configure a description for the ACL rule.
   
   
   ```
   [rule](cmdqueryname=rule+description) rule-id description destext
   ```
   
   The ACL rule description helps you understand and remember the functions or purpose of the ACL rule.
   
   You must create a rule before you can configure a description for it.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Example

* Configure a packet filtering rule based on the source IPv4 address (host address).
  
  To permit packets from a host, add a rule to an ACL. For example, to permit packets from the host at 192.168.1.3, create the following rule in ACL 2001.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl 2001
  [*HUAWEI-acl4-basic-2001] rule permit source 192.168.1.3 0
  [*HUAWEI-acl4-basic-2001] quit
  [*HUAWEI] commit
  ```
* Configure a packet filtering rule based on the source IPv4 address segment.
  
  To permit packets from a host and reject packets from other hosts on the same network segment, configure rules in an ACL. For example, to permit packets from the host at 192.168.1.3 and reject packets from other hosts on the network segment 192.168.1.0/24, configure the following rules in ACL 2001 and configure the description "permit only 192.168.1.3 through" for the ACL.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl 2001
  [*HUAWEI-acl4-basic-2001] rule permit source 192.168.1.3 0
  [*HUAWEI-acl4-basic-2001] rule deny source 192.168.1.0 0.0.0.255
  [*HUAWEI-acl4-basic-2001] description permit only 192.168.1.3 through
  [*HUAWEI-acl4-basic-2001] quit
  [*HUAWEI] commit
  ```
* Configure a time-based ACL rule.
  
  Create a time range **working-time** (for example, 08:00 to 18:00 on Monday through Friday). Configure a rule in the ACL **work-acl** to reject packets from the network segment 192.168.1.0/24 within the time range.
  ```
  <HUAWEI> system-view
  [~HUAWEI] time-range working-time 8:00 to 18:00 working-day
  [*HUAWEI] acl name work-acl basic
  [*HUAWEI-acl4-basic-work-acl] rule deny source 192.168.1.0 0.0.0.255 time-range working-time
  [*HUAWEI-acl4-basic-work-acl] quit
  [*HUAWEI] commit
  ```
* Configure a packet filtering rule based on the IP fragment information and source IPv4 address segment.
  
  For example, to reject all fragments except the first from the network segment 192.168.1.0/24, configure the following rule in ACL 2001.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl 2001
  [*HUAWEI-acl4-basic-2001] rule deny source 192.168.1.0 0.0.0.255 fragment-type fragment
  [*HUAWEI-acl4-basic-2001] quit
  [*HUAWEI] commit
  ```

#### Verifying the Configuration

Run the [**display acl**](cmdqueryname=display+acl+name+all) { *basic-acl-number* | **name** *basic-acl-name* | **all** } command to check the configuration of the basic ACL.


#### Follow-up Procedure

Apply the basic ACL to a service module so that the basic ACL rules can be delivered and take effect.