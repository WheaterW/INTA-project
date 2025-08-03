Configuring a User-Defined ACL
==============================

Configuring a User-Defined ACL

#### Context

A user-defined ACL defines packet filtering rules based on packet headers, offsets, character string masks, and user-defined character strings. With a user-defined ACL configured, the system performs an AND operation on the packet bytes from a specified offset behind the packet header and the character string mask, compares the extracted character string against the user-defined character string, and then filters IPv4 packets.

User-defined ACLs are more accurate and flexible than basic ACLs, advanced ACLs, and Layer 2 ACLs, and provide more functions. For example, a user-defined ACL can be configured to filter ARP packets based on source IPv4 addresses and ARP packet types.

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
2. Configure a user-defined ACL. You can create a numbered or named user-defined ACL.
   
   
   * Create a numbered user-defined ACL and enter its view.
     ```
     [acl](cmdqueryname=acl+number) [ number ] user-acl-number 
     ```
     
     The number of a user-defined ACL ranges from 5000 to 5999.
   * Create a named user-defined ACL and enter its view.
     
     ```
     [acl name](cmdqueryname=acl+name+user) user-acl-name user
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
5. Configure a rule for the user-defined ACL.
   
   
   ```
   [rule](cmdqueryname=rule+name+deny+permit+l2-head+ipv4-head+l4-head+time-range) [ rule-id ] [ name rule-name ] { deny | permit } [ [ [ [ l2-head ] rule1 rulemask1 offset1-l2 [ rule2 rulemask2 offset2-l2 [ rule3 rulemask3 offset3-l2 [ rule4 rulemask4 offset4-l2 ] ] ] ] | [ ipv4-head rule1 rulemask1 offset1-ipv4 [ rule2 rulemask2 offset2-ipv4 [ rule3 rulemask3 offset3-ipv4 [ rule4 rulemask4 offset4-ipv4 ] ] ] ] | [ l4-head rule1 rulemask1 offset1-l4 [ rule2 rulemask2 offset2-l4 [ rule3 rulemask3 offset3-l4 [ rule4 rulemask4 offset4-l4 ] ] ] ] ] | [ time-range time-name ] ] *
   ```
   
   In this example, only one permit or deny rule is configured. In actual configuration, you can configure multiple ACL rules and decide the matching order of the rules according to service requirements.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To configure a time-based user-defined ACL, you must create a time range. For details, see [Creating a Time Range in Which an ACL Takes Effect](vrp_acl_cfg_0009.html).
   
   When a user-defined ACL rule is configured:
   * If you do not specify an offset, the Ethernet frame header (equivalent to the case where **l2-head** is specified) is used as an offset by default.
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

Configure packet filtering rules based on Layer 2 headers, offsets, character string masks, and user-defined character strings.

* Configure a rule in ACL 5001 to deny ARP packets from 192.168.0.2.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl 5001
  [*HUAWEI-acl-user-5001] rule deny l2-head 0x00000806 0x0000ffff 10 0x0000c0a8 0x0000ffff 26 0x00020000 0xffff0000 30
  [*HUAWEI-acl-user-5001] quit
  [*HUAWEI] commit
  ```
  
  In the preceding rule:
  
  + 0x00000806 indicates the ARP protocol.
  + 0x0000ffff is the character string mask.
  + 10 indicates the offset of the Protocol Type field in an ARP packet without VLAN ID.
  + 0x0000c0a8 and 0x00020000 are the hexadecimal format of 192.168.0.2. The source IP address (the hexadecimal value 0xc0a80002 in this example) needs to be divided into two segments for matching. This is because the IP Address of Sender field in an ARP packet begins at the 28th byte in the Layer 2 header and occupies 4 bytes, and the Layer 2 header's offset defined in a user-defined ACL must be 4 x *n* + 2 (*n* is an integer). The two low-order bytes among the four bytes behind the offset of 26 (4 x 6 + 2) and the two high-order bytes among the four bytes behind the offset of 30 (4 x 7 + 2) are matched separately. To filter ARP packets with VLAN IDs, add 4 to each offset.
  + 26 and 30 indicate the offsets of two high-order bytes and two low-order bytes of the IP Address of Sender field in an ARP packet without VLAN ID, respectively.**Figure 1** Offset of the IP Address of Sender field in the Layer 2 header of an ARP packet  
    ![](figure/en-us_image_0000001130782828.png)
* Configure a rule in a user-defined ACL named **deny-tcp** to deny all TCP packets.
  ```
  <HUAWEI> system-view
  [~HUAWEI] acl name deny-tcp user
  [*HUAWEI-acl-user-deny-tcp] rule 5 deny ipv4-head 0x00060000 0x00ff0000 8
  [*HUAWEI-acl-user-5001] quit
  [*HUAWEI] commit
  ```
  
  In the preceding rule:
  
  + 0x00060000 indicates the TCP protocol.
  + 8 indicates the offset of the Protocol field in an IP packet. The Protocol field begins at the 10th byte of the IPv4 header and occupies 1 byte. The IPv4 header's offset defined in a user-defined ACL must be 4 x *n* (*n* is an integer). Therefore, the second high-order byte among the 4 bytes behind the offset of 8 in the IPv4 header is matched.**Figure 2** Offset of the Protocol field in the IPv4 header  
  ![](figure/en-us_image_0000001130623040.png)

#### Verifying the Configuration

Run the [**display acl**](cmdqueryname=display+acl+name+all) { *user-acl-number* | **name** *user-acl-name* | **all** } command to check the configuration of the user-defined ACL.


#### Follow-up Procedure

Apply the user-defined ACL to a service module so that the user-defined ACL rules can be delivered and take effect.