Setting the Maximum Number of Invalid IPv4 Multicast Protocol Messages That Can Be Stored
=========================================================================================

Setting the maximum number of invalid IPv4 multicast protocol messages that can be stored on a multicast device helps locate and rectify faults.

#### Usage Scenario

If forwarding entries cannot be created or Multicast Source Discovery Protocol (MSDP) peer relationships cannot be established on a multicast network, you can set the maximum number of invalid multicast protocol messages that can be stored on a multicast device and run the corresponding display command to check statistics and details about these messages. The command output helps you analyze these invalid messages and troubleshoot the faults.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast invalid-packet**](cmdqueryname=multicast+invalid-packet) { **igmp** | **mdt** | **msdp** | **pim** } **max-count** *max-number*
   
   
   
   The maximum number of invalid multicast protocol messages that the device can store is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **| include multicast invalid-packet** command to check the maximum number of invalid multicast protocol messages that the device can store.

```
<HUAWEI> display current-configuration | include multicast invalid-packet
 multicast invalid-packet igmp max-count 20
```

After setting the maximum number of invalid multicast protocol messages that the device can store, you can run the following commands to check statistics about invalid multicast protocol messages that the device stores:

* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **invalid-packet** [ **interface** *interface-type interface-number* | **message-type** { **leave** | **query** | **report** } ] \* command to check statistics about invalid IGMP messages that the device stores.
  
  ```
  <HUAWEI> display igmp invalid-packet
  
             Statistics of invalid packets for public net:
  --------------------------------------------------------------------
  IGMP Query invalid packet:
  Unwanted Source List    : 1000        Zero Max Resp Code      : 0
  Fault Length            : 1000        Invalid Multicast Group : 0
  Bad Checksum            : 0
  
  IGMP Report invalid packet:
  Fault Length            : 0           Invalid Multicast Group : 0
  Invalid Multicast Source: 0           Bad Checksum            : 0
  Illegal Report Type     : 0
  
  IGMP Leave invalid packet:
  Invalid Multicast Group : 0           Bad Checksum            : 0
  --------------------------------------------------------------------  
  ```
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **invalid-packet** [ **peer** *peer-address* | **message-type** { **keepalive** | **notification** | **sa-request** | **sa-response** | **source-active** } ] \* command to check statistics about invalid MSDP messages that the device stores.
  
  ```
  <HUAWEI> display msdp invalid-packet peer 1.1.1.1
  
               Statistics of invalid packets for public net:                      
  --------------------------------------------------------------------            
  MSDP SA invalid packet:
  Fault Length            : 0           Bad Length-x            : 0
  Bad Sprefix             : 0           Invalid Multicast Group : 0
  Invalid Multicast Source: 0           Bad Encap Data          : 0
  Illegal RP Addr         : 0           RP Loop                 : 0
  
  MSDP SA Response invalid packet:
  Fault Length            : 0           Bad Length-x            : 0
  Bad Sprefix             : 0           Invalid Multicast Group : 0
  Invalid Multicast Source: 0           Illegal RP Addr         : 0
  RP Loop                 : 0
  
  MSDP SA Request invalid packet:
  Fault Length            : 0           Invalid Multicast Group : 0
  
  MSDP Keep Alive invalid packet:
  Fault Length            : 0
  
  MSDP Notification invalid packet:
  Fault Length            : 0                         
  --------------------------------------------------------------------  
  
  ```
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **invalid-packet** [ **interface** *interface-type interface-number* | **message-type** { **hello** | **join-prune** | **assert** | **bsr** | **announcement** | **discovery** | **graft** | **graft-ack** | **state-refresh** } ] \* command to check statistics about invalid PIM messages stored on the device.
  
  ```
  <HUAWEI> display pim invalid-packet
  
               Statistics of invalid packets for public net:                      
  --------------------------------------------------------------------         
  PIM General invalid packet:
  Invalid PIM Version     : 0           Invalid PIM Type        : 0
  Fault Length            : 0           Bad Checksum            : 0
  
  PIM Register invalid packet:
  Invalid Multicast Source: 0           Invalid Multicast Group : 0
  Invalid Dest Addr       : 0
  
  PIM Register-Stop invalid packet:
  Invalid Multicast Source: 0           Invalid Multicast Group : 0
  Invalid Dest Addr       : 0           IP Source not RP        : 0
  
  PIM CRP invalid packet:
  Invalid Dest Addr       : 0           Invalid CRP Addr        : 0
  Fault Length            : 0           CRP Adv Fault Length    : 0
  Invalid Multicast Group : 0
  
  PIM Assert invalid packet:
  Invalid Dest Addr       : 0           Invalid IP Source Addr  : 0
  Invalid Multicast Source: 0           Invalid Multicast Group : 0
  
  PIM BSR invalid packet:
  Bad Payload             : 0           Fault Length            : 0
  Bad Scope Mask          : 0           Invalid Multicast Group : 0
  Not CBSR But BSR        : 0           Invalid BSR Addr        : 0
  Fault Hash Length       : 0           Invalid IP Source Addr  : 0
  
  PIM Hello invalid packet:
  Invalid Addr List       : 0           Fault Length            : 0
  Bad Holdtime Length     : 0           Bad LanPruneDelay Length: 0
  Bad DrPriority Length   : 0           Bad GenID Length        : 0
  Invalid Dest Addr       : 0           Invalid IP Source Addr  : 0
  
  PIM Join/Prune invalid packet:
  Invalid Multicast Source: 0           Invalid Multicast Group : 0
  Invalid Up Neighbor     : 0           Invalid IP Source Addr  : 0
  Invalid Dest Addr       : 0           Fault Length            : 0  
  
  PIM Graft invalid packet:
  Invalid Multicast Source: 0           Invalid Multicast Group : 0
  Invalid Up Neighbor     : 0           Invalid IP Source Addr  : 0
  Fault Length            : 0
  
  PIM Graft-Ack invalid packet:
  Invalid Multicast Source: 0           Invalid Multicast Group : 0
  Invalid Up Neighbor     : 0           Invalid IP Source Addr  : 0
  Fault Length            : 0
  
  PIM State Refresh invalid packet:
  Invalid Multicast Source: 0           Invalid Multicast Group : 0
  Invalid Originator Addr : 0           Fault Length            : 0
  --------------------------------------------------------------------   
  
  ```
* Run the [**display multicast-domain**](cmdqueryname=display+multicast-domain) { **vpn-instance** *vpn-instance-name* | **all-instance** } **invalid-packet** command to check statistics about invalid group switching messages stored on the device.
  
  ```
  <HUAWEI> display multicast-domain vpn-instance vpn1 invalid-packet
               Statistics of invalid packets for vpn1:            
  --------------------------------------------------------------------            
  MDT Switch invalid packet:
  Fault Length            : 0           Invalid Message Type    : 0
  Invalid Multicast Source: 0           Invalid Multicast Group : 0
  Invalid Switch Group    : 0                 
  --------------------------------------------------------------------
  ```

After setting the maximum number of invalid multicast protocol messages that the device can store, you can run the following commands to check detailed information about invalid multicast protocol messages that the device stores:

* Run the [**display igmp invalid-packet**](cmdqueryname=display+igmp+invalid-packet) [ *packet-number* ] **verbose** command to check details about invalid IGMP messages that the device stores.
  
  ```
  <HUAWEI> display igmp invalid-packet 1 verbose
         Detailed information of invalid packets
  -----------------------------------------------------
  Packet information (Index 6):
  -----------------------------------------------------
  Interface           :  GigabitEthernet0/1/1
  Time                :  2010-6-9 11:03:51 UTC-08:00
  Message Length      :  24
  Invalid Type        :  Invalid Multicast Group
  Source Address      :  10.0.3.3
  0000: 16 3c 00 00 01 34 04 04
  -----------------------------------------------------
  ```
* Run the [**display msdp invalid-packet**](cmdqueryname=display+msdp+invalid-packet) [ *packet-number* ] **verbose** command to check details about invalid MSDP messages that the device stores.
  
  ```
  <HUAWEI> display msdp invalid-packet 1 verbose
         Detailed information of invalid packets         
  -----------------------------------------------------  
  Packet information (Index 1):                          
  -----------------------------------------------------  
  Interface           :  GigabitEthernet0/1/1                   
  Time                :  2010-6-9 11:25:46 UTC-08:00     
  Message Length      :  22                              
  Invalid Type        :  Invalid Addr List               
  Peer Address         :  10.42.162.13
  0000: 00 01 00 02 00 69 00 13 00 04 00 00 00 64 00 02  
  0010: 00 04 81 f4 09 c4                                
  -----------------------------------------------------  
  ```

* Run the [**display pim invalid-packet**](cmdqueryname=display+pim+invalid-packet) [ *packet-number* ] **verbose** command to check details about invalid PIM messages that the device stores.
  
  ```
  <HUAWEI> display pim invalid-packet 1 verbose
         Detailed information of invalid packets
  -----------------------------------------------------
  Packet information (Index 1):
  -----------------------------------------------------
  Interface           :  GigabitEthernet0/1/1
  Time                :  2010-6-1 20:04:35 UTC-08:00
  Message Length      :  26
  Invalid Type        :  Invalid Multicast Source
  Source Address      :  10.0.3.3
  0000: 25 00 96 77 01 00 00 20 e1 01 01 01 01 00 e0 00
  0010: 00 00 80 00 00 64 00 00 00 00
  -----------------------------------------------------  
  ```
* Run the [**display multicast-domain**](cmdqueryname=display+multicast-domain) **invalid-packet** [ *packet-number* ] **verbose** command to check details about invalid group switching messages that the device stores.
  
  ```
  <HUAWEI> display multicast-domain invalid-packet 1 verbose
         Detailed information of invalid packets      
  -----------------------------------------------------   
  Packet information (Index 1):                         
  ----------------------------------------------------- 
  Neighbor           :  1.1.1.1
  Time                :  2011-8-9 10:50:08 UTC-08:00
  Message Length      :  16
  Invalid Type        :  Invalid Switch Group
  0000: 01 00 10 00 64 64 64 64 e8 00 00 00 0a 00 00 00 
  -----------------------------------------------------
  ```