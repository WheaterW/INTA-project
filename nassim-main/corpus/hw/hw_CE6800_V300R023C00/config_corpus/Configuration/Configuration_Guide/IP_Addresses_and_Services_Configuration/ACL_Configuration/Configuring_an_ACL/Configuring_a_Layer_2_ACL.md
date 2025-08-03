Configuring a Layer 2 ACL
=========================

Configuring a Layer 2 ACL

#### Context

A Layer 2 ACL defines packet filtering rules based on the information in Ethernet frame headers of the packets, such as source and destination MAC addresses, VLAN IDs, and Layer 2 protocol types.

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
2. Create a Layer 2 ACL. You can create a numbered or named Layer 2 ACL.
   
   
   * Create a numbered Layer 2 ACL and enter its view.
     ```
     [acl](cmdqueryname=acl+number) [ number ] link-acl-number 
     ```
     
     The number of a Layer 2 ACL ranges from 4000 to 4999.
   * Create a named Layer 2 ACL and enter its view.
     
     ```
     [acl name](cmdqueryname=acl+name+link) link-acl-name link 
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
5. Configure a rule for the Layer 2 ACL.
   
   
   ```
   [rule](cmdqueryname=rule+name+permit+deny+type+arp+ip+ipv6+mpls+rarp+source-mac) [ rule-id ] [ name rule-name ] { permit | deny } [ [ ether-ii | snap ] | [ type { type | arp | ip | ipv6 | mpls | rarp } [ fram-type-mask ] ] | source-mac src-mac-address [ src-mac-mask ] | destination-mac dest-mac-address [ dest-mac-mask ] | vlan vlan-id [ vlanid-mask ] | 8021p 8021p | inner-vlan cvlan-value [ cvlan-mask ] | inner-8021p cvlan-8021p-value | double-tag | time-range time-range-name ] *
   ```
   
   In this example, only one permit or deny rule is configured. In actual configuration, you can configure multiple ACL rules and decide the matching order of the rules according to service requirements.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To configure a time-based Layer 2 ACL, you must create a time range. For details, see [Creating a Time Range in Which an ACL Takes Effect](vrp_acl_cfg_0009.html).
   
   When a rule is configured for the Layer 2 ACL:
   * If **ether-ii** | **snap** is specified, only packets with a specified encapsulation type are filtered.
   * If no **ether-ii** | **snap** is specified, packets with all encapsulation types are filtered.
   * If **time-range** is specified, the specified time range name must exist. Otherwise, the ACL rule configuration fails.
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

* Configure packet filtering rules based on the source MAC address, destination MAC address, and Layer 2 protocol type.
  
  To permit ARP packets with the specified destination and source MAC addresses and Layer 2 protocol type, configure a rule in a Layer 2 ACL. For example, to permit ARP packets with the destination MAC address of 00e0-fc00-0001, source MAC address of 00e0-fc00-0002, and Layer 2 protocol type of 0x0806, configure the following rule in ACL 4001.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl 4001
  [*HUAWEI-acl-L2-4001] rule permit destination-mac 00e0-fc00-0001 source-mac 00e0-fc00-0002 type 0x0806
  [*HUAWEI-acl-L2-4001] quit
  [*HUAWEI] commit
  ```
  
  To reject packets with a specified Layer 2 protocol type, configure a rule in a Layer 2 ACL. For example, to reject packets with the Layer 2 protocol type of 0x8863, configure the following rule in ACL 4001.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl 4001
  [*HUAWEI-acl-L2-4001] rule deny type 0x8863
  [*HUAWEI-acl-L2-4001] quit
  [*HUAWEI] commit
  ```
* Configure a packet filtering rule based on the source MAC address segment and inner VLAN IDs.
  
  To reject packets from a specified MAC address segment in a VLAN, configure a rule in a Layer 2 ACL. For example, to reject packets from the source MAC address segment 00e0-fc01-0000 to 00e0-fc01-ffff in VLAN 10, configure the following rule in the Layer 2 ACL **deny-vlan10-mac**.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl name deny-vlan10-mac link
  [*HUAWEI-acl-L2-deny-vlan10-mac] rule deny vlan 10 source-mac 00e0-fc01-0000 00e0-fc01-ffff
  [*HUAWEI-acl-L2-deny-vlan10-mac] quit
  [*HUAWEI] commit
  ```

#### Verifying the Configuration

Run the [**display acl**](cmdqueryname=display+acl+name+all) { *link-acl-number* | **name** *link-acl-name* | **all** } command to check the configuration of the Layer 2 ACL.


#### Follow-up Procedure

Apply the Layer 2 ACL to a service module so that the Layer 2 ACL rules can be delivered and take effect.