Configuring an ARP-based ACL
============================

Configuring an ARP-based ACL

#### Context

An ARP-based ACL defines packet filtering rules based on the source and destination IPv4 addresses and source and destination MAC addresses of ARP packets.

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
2. Create an ARP-based ACL. You can create a numbered or named ARP-based ACL.
   
   
   * Create a numbered ARP-based ACL and enter its view.
     ```
     [acl](cmdqueryname=acl+number) [ number ] arp-acl-number 
     ```
     
     The number of an ARP-based ACL ranges from 23000 to 23999.
   * Create a named ARP-based ACL and enter its view.
     
     ```
     [acl name](cmdqueryname=acl+name+arp) arp-acl-name arp
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
5. Configure a rule for the ARP-based ACL. Run one or more of the following commands based on ARP packet types.
   
   
   * To configure an ARP-based ACL rule to match ARP request messages, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+request+source-ip+0+any+source-mac+any) [ rule-id ] [ name rule-name ] { permit | deny } [ request ] [ source-ip { source-ip-address { source-wildcard | 0 | source-netmask } | any } | source-mac { source-mac-address [ source-mac-mask ] | any } | time-range time-name ] *
     ```
   * To configure an ARP-based ACL rule to match ARP reply messages, run:
     
     ```
     [rule](cmdqueryname=rule+name+permit+deny+reply+source-ip+0+any+destination-ip+0+any) [ rule-id ] [ name rule-name ] { permit | deny } reply [ source-ip { source-ip-address { source-wildcard | 0 | source-netmask } | any } | destination-ip { destination-ip-address { destination-wildcard | 0 | destination-netmask } | any } | source-mac { source-mac-address [ source-mac-mask ] | any } | destination-mac { destination-mac-address [ destination-mac-mask ] | any } | time-range time-name ] *
     ```
   
   In this example, only one permit or deny rule is configured. In actual configuration, you can configure multiple ACL rules and decide the matching order of the rules according to service requirements.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To configure a time-based ARP-based ACL, you must create a time range. For details, see [Creating a Time Range in Which an ACL Takes Effect](vrp_acl_cfg_0009.html).
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

* Configure a rule for filtering ARP reply messages based on a source MAC address and a destination MAC address.
  
  Configure a rule in ACL 23000 to permit the ARP reply messages with the destination MAC address of 00e0-fc00-0001 and the source MAC address of 00e0-fc00-0002.
  
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl 23000
  [*HUAWEI-acl-arp-23000] rule permit reply destination-mac 00e0-fc00-0001 source-mac 00e0-fc00-0002
  [*HUAWEI-acl-arp-23000] quit
  [*HUAWEI] commit
  ```

#### Verifying the Configuration

Run the [**display acl**](cmdqueryname=display+acl+name+all) { *arp-acl-number* | **name** *arp-acl-name* | **all** } command to check the configuration of the ARP-based ACL.


#### Follow-up Procedure

Apply the ARP-based ACL to a service module so that the ARP-based ACL rules can be delivered and take effect.