Example for Configuring L2TPv3 over IPv4 PWs to Carry Services (Layer 2 Sub-interface)
======================================================================================

An L2TPv3 PW supports multiple types of services and processes each differently.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369204__fig_037FBC9D), an L2TPv3 PW needs to be established between PE1 and PE2, and another between PE1 and PE3. The L2TPv3 PW between PE1 and PE2 needs to support service access in S-tag+C-tag termination mode, and that between PE1 and PE3 needs to support service access in whole-interface mode. The AC interfaces of the two PWs need to be EVC Layer 2 sub-interfaces. A VLAN service needs to be configured on CEs.![](../../../../public_sys-resources/note_3.0-en-us.png) 

An L2TPv3 PW supports the following service access modes: whole-interface, C-tag termination, S-tag termination, and S-tag+C-tag termination. The service encapsulation configurations vary according to service access modes, but the L2TPv3 PW configurations for different service access modes are similar. This configuration example uses the C-tag termination mode and whole-interface mode.


**Figure 1** L2TPv3 PW networking  
![](images/fig_dc_vrp_l2tpv3_cfg_00001102.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| CE1 | GE0/1/1 | - |
| CE2 | GE0/1/1 | - |
| CE3 | GE0/1/1 | - |
| PE1 | GE0/1/1.4 | - |
| GE0/1/0.4 | - |
| Loopback2 | 1.1.1.1/32 |
| Loopback3 | 2.2.2.2/32 |
| GE0/2/1 | 192.168.14.1/24 |
| GE0/3/1 | 192.168.24.1/24 |
| PE2 | Loopback4 | 3.3.3.3/32 |
| GE0/2/1 | 192.168.14.2/24 |
| GE0/1/1.4 | - |
| PE3 | Loopback5 | 4.4.4.4/32 |
| GE0/2/1 | 192.168.24.2/24 |
| GE0/1/1.4 | - |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IS-IS on PEs.
2. Configure a VLAN service on CEs.
3. Enable L2TPv3 on PE1, PE2, and PE3.
4. Establish an L2TPv3 PW between PE1 and PE2 and another between PE1 and PE3, configure source and destination addresses and cookies for the PWs, and bind the PWs to service instances. Note that cookies need to be configured using the SHA256 algorithm.
5. Configure services on PE1, PE2, and PE3 to access L2TPv3 PWs.

#### Data Preparation

To complete the configuration, you need the following data:

* IS-IS process IDs on PEs
* VLAN IDs on CEs
* Source interfaces, source addresses, and destination addresses of L2TPv3 PWs
* Cookies for L2TPv3 PWs
* Service access types of L2TPv3 PWs
* IDs of service instances to which L2TPv3 PWs are to be bound

#### Procedure

1. Configure IS-IS on PEs.
   
   # Configure PE1.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] cost-style wide
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface loopback 2
   ```
   ```
   [*PE1-loopback2] ip address 1.1.1.1 32
   ```
   ```
   [*PE1-loopback2] isis enable 1
   ```
   ```
   [*PE1-loopback2] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/1
   ```
   ```
   [*PE1-Gigabitethernet0/2/1] ip address 192.168.14.1 24
   ```
   ```
   [*PE1-Gigabitethernet0/2/1] isis enable 1
   ```
   ```
   [*PE1-Gigabitethernet0/2/1] quit
   ```
   ```
   [*PE1] interface loopback 3
   ```
   ```
   [*PE1-loopback3] ip address 2.2.2.2 32
   ```
   ```
   [*PE1-loopback3] isis enable 1
   ```
   ```
   [*PE1-loopback3] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/3/1
   ```
   ```
   [*PE1-Gigabitethernet0/3/1] ip address 192.168.24.1 24
   ```
   ```
   [*PE1-Gigabitethernet0/3/1] isis enable 1
   ```
   ```
   [*PE1-Gigabitethernet0/3/1] commit
   ```
   ```
   [~PE1-Gigabitethernet0/3/1] quit
   ```
   
   
   # Configure PE2.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*PE2] isis 1
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface loopback 4
   ```
   ```
   [*PE2-loopback4] ip address 3.3.3.3 32
   ```
   ```
   [*PE2-loopback4] isis enable 1
   ```
   ```
   [*PE2-loopback4] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/1
   ```
   ```
   [*PE2-Gigabitethernet0/2/1] ip address 192.168.14.2 24
   ```
   ```
   [*PE2-Gigabitethernet0/2/1] isis enable 1
   ```
   ```
   [*PE2-Gigabitethernet0/2/1] commit
   ```
   ```
   [~PE2-Gigabitethernet0/2/1] quit
   ```
   
   
   # Configure PE3.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE3
   ```
   ```
   [*PE3] isis 1
   ```
   ```
   [*PE3-isis-1] cost-style wide
   ```
   ```
   [*PE3-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*PE3-isis-1] quit
   ```
   ```
   [*PE3] interface loopback 5
   ```
   ```
   [*PE3-loopback5] ip address 4.4.4.4 32
   ```
   ```
   [*PE3-loopback5] isis enable 1
   ```
   ```
   [*PE2-loopback5] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/2/1
   ```
   ```
   [*PE3-Gigabitethernet0/2/1] ip address 192.168.24.2 24
   ```
   ```
   [*PE3-Gigabitethernet0/2/1] isis enable 1
   ```
   ```
   [*PE3-Gigabitethernet0/2/1] commit
   ```
   ```
   [~PE3-Gigabitethernet0/2/1] quit
   ```
2. Configure a VLAN service on CE1.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE1] vlan 2
   ```
   ```
   [*CE1-vlan2] commit
   ```
   ```
   [~CE1-vlan2] quit
   ```
   ```
   [~CE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] commit
   ```
3. Enable L2TPv3 on PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] l2tpv3 enable
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] l2tpv3 enable
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] l2tpv3 enable
   ```
   ```
   [*PE3] commit
   ```
4. Configure services on PE1 and PE2 to access L2TPv3 PWs in C-tag termination mode.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] rewrite pop single
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To configure services on PE1 to access an L2TPv3 PW in whole-interface mode, run the following commands:
   
   ```
   [~PE1] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] encapsulation default
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] commit
   ```
   
   To configure services on PE1 to access an L2TPv3 PW in C-tag termination mode, run the following commands:
   
   ```
   [~PE1] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] rewrite pop single
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] commit
   ```
   
   To configure services on PE1 to access an L2TPv3 PW in S-tag termination mode, run the following commands:
   
   ```
   [~PE1] interface gigabitethernet0/1/1
   ```
   ```
   [*PE1-Gigabitethernet0/1/1] qinq protocol 88a8
   ```
   ```
   [*PE1-Gigabitethernet0/1/1] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] rewrite pop single
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] commit
   ```
   
   To configure services on PE1 to access an L2TPv3 PW in S-tag+C-tag termination mode, run the following commands:
   
   ```
   [~PE1] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] encapsulation qinq vid 2 ce-vid 2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] rewrite pop double
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] commit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] rewrite pop single
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To configure services on PE2 to access an L2TPv3 PW in whole-interface mode, run the following commands:
   
   ```
   [~PE2] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] encapsulation default
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] commit
   ```
   
   To configure services on PE2 to access an L2TPv3 PW in C-tag termination mode, run the following commands:
   
   ```
   [~PE2] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] rewrite pop single
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] commit
   ```
   
   To configure services on PE2 to access an L2TPv3 PW in S-tag termination mode, run the following commands:
   
   ```
   [~PE2] interface gigabitethernet0/1/1
   ```
   ```
   [*PE2-Gigabitethernet0/1/1] qinq protocol 88a8
   ```
   ```
   [*PE2-Gigabitethernet0/1/1] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] rewrite pop single
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] commit
   ```
   
   To configure services on PE2 to access an L2TPv3 PW in S-tag+C-tag termination mode, run the following commands:
   
   ```
   [~PE2] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] encapsulation qinq vid 2 ce-vid 2
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] rewrite pop double
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] commit
   ```
5. Configure an L2TPv3 PW from PE1 to PE2.
   
   
   ```
   [~PE1] l2tpv3 pw pwabc
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc] source interface LoopBack 2 1.1.1.1
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc] destination 3.3.3.3
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc] l2tpv3 local cookie key cipher XTEOWSS-1
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc] l2tpv3 remote cookie key cipher XTEOWSS-1
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4] l2tpv3 instance a123
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4-l2tpv3-instance-a123] l2tpv3 static binding pw pwabc
   ```
   ```
   [*PE1-Gigabitethernet0/1/1.4-l2tpv3-instance-a123] commit
   ```
   ```
   [~PE1-Gigabitethernet0/1/1.4-l2tpv3-instance-a123] quit
   ```
   ```
   [~PE1-Gigabitethernet0/1/1.4] quit
   ```
6. Configure an L2TPv3 PW from PE2 to PE1.
   
   
   ```
   [~PE2] l2tpv3 pw pwabc
   ```
   ```
   [*PE2-l2tpv3-pw-pwabc] source interface loopback 4 3.3.3.3
   ```
   ```
   [*PE2-l2tpv3-pw-pwabc] destination 1.1.1.1
   ```
   ```
   [*PE2-l2tpv3-pw-pwabc] l2tpv3 local cookie key cipher XTEOWSS-1
   ```
   ```
   [*PE2-l2tpv3-pw-pwabc] l2tpv3 remote cookie key cipher XTEOWSS-1
   ```
   ```
   [*PE2-l2tpv3-pw-pwabc] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4] l2tpv3 instance a234
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4-l2tpv3-instance-a234] l2tpv3 static binding pw pwabc
   ```
   ```
   [*PE2-Gigabitethernet0/1/1.4-l2tpv3-instance-a234] commit
   ```
   ```
   [~PE2-Gigabitethernet0/1/1.4-l2tpv3-instance-a234] quit
   ```
   ```
   [~PE2-Gigabitethernet0/1/1.4] quit
   ```
7. Configure CE2.
   
   
   ```
   [~CE2] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] commit
   ```
8. Configure services on PE1 and PE3 to access L2TPv3 PWs in whole-interface mode.
   
   
   
   # Configure PE1.
   
   ```
   [*PE1] interface gigabitethernet0/1/0.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] encapsulation default
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To configure services on PE1 to access an L2TPv3 PW in S-tag+C-tag termination mode, run the following commands:
   
   ```
   [~PE1] interface gigabitethernet0/1/0.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] encapsulation qinq vid 2 ce-vid 2
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] rewrite pop double
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] commit
   ```
   
   To configure services on PE1 to access an L2TPv3 PW in C-tag termination mode, run the following commands:
   
   ```
   [~PE1] interface gigabitethernet0/1/0.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] rewrite pop single
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] commit
   ```
   
   To configure services on PE1 to access an L2TPv3 PW in S-tag termination mode, run the following commands:
   
   ```
   [~PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-Gigabitethernet0/1/0] qinq protocol 88a8
   ```
   ```
   [*PE1-Gigabitethernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] rewrite pop single
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] commit
   ```
   
   # Configure PE3.
   
   ```
   [*PE3] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] encapsulation default
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To configure services on PE3 to access an L2TPv3 PW in S-tag+C-tag termination mode, run the following commands:
   
   ```
   [~PE3] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] encapsulation qinq vid 2 ce-vid 2
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] rewrite pop double
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] commit
   ```
   
   To configure services on PE3 to access an L2TPv3 PW in C-tag termination mode, run the following commands:
   
   ```
   [~PE3] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] rewrite pop single
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] commit
   ```
   
   To configure services on PE3 to access an L2TPv3 PW in S-tag termination mode, run the following commands:
   
   ```
   [~PE3] interface gigabitethernet0/1/1
   ```
   ```
   [*PE3-Gigabitethernet0/1/1] qinq protocol 88a8
   ```
   ```
   [*PE3-Gigabitethernet0/1/1] interface gigabitethernet0/1/1.4 mode l2
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] encapsulation dot1q vid 2
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] rewrite pop single
   ```
   ```
   [*PE3-Gigabitethernet0/1/1.4] commit
   ```
9. Configure an L2TPv3 PW from PE1 to PE3.
   
   
   ```
   [~PE1] l2tpv3 pw pwabc1
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc1] l2tpv3 local session-id 10
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc1] source interface LoopBack 3 2.2.2.2
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc1] destination 4.4.4.4
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc1] l2tpv3 local cookie key cipher XTEOWSS-1
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc1] l2tpv3 remote cookie key cipher XTEOWSS-1
   ```
   ```
   [*PE1-l2tpv3-pw-pwabc1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0.4 mode l2
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4] l2tpv3 instance a345
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4-l2tpv3-instance-a345] l2tpv3 static binding pw pwabc1
   ```
   ```
   [*PE1-Gigabitethernet0/1/0.4-l2tpv3-instance-a345] commit
   ```
   ```
   [~PE1-Gigabitethernet0/1/0.4-l2tpv3-instance-a345] quit
   ```
   ```
   [~PE1-Gigabitethernet0/1/0.4] quit
   ```
10. Configure an L2TPv3 PW from PE3 to PE1.
    
    
    ```
    [~PE3] l2tpv3 pw pwabc1
    ```
    ```
    [*PE3-l2tpv3-pw-pwabc1] l2tpv3 remote session-id 10
    ```
    ```
    [*PE3-l2tpv3-pw-pwabc1] source interface loopback 5 4.4.4.4
    ```
    ```
    [*PE3-l2tpv3-pw-pwabc1] destination 2.2.2.2
    ```
    ```
    [*PE3-l2tpv3-pw-pwabc1] l2tpv3 local cookie key cipher XTEOWSS-1
    ```
    ```
    [*PE3-l2tpv3-pw-pwabc1] l2tpv3 remote cookie key cipher XTEOWSS-1
    ```
    ```
    [*PE3-l2tpv3-pw-pwabc1] quit
    ```
    ```
    [*PE3] interface gigabitethernet0/1/1.4 mode l2
    ```
    ```
    [*PE3-Gigabitethernet0/1/1.4] l2tpv3 instance a456
    ```
    ```
    [*PE3-Gigabitethernet0/1/1.4-l2tpv3-instance-a456] l2tpv3 static binding pw pwabc1
    ```
    ```
    [*PE3-Gigabitethernet0/1/1.4-l2tpv3-instance-a456] commit
    ```
    ```
    [~PE3-Gigabitethernet0/1/1.4-l2tpv3-instance-a456] quit
    ```
    ```
    [~PE3-Gigabitethernet0/1/1.4] quit
    ```
11. Configure CE3.
    
    
    ```
    [~CE3] interface gigabitethernet 0/1/1
    ```
    ```
    [~CE3-GigabitEthernet0/1/1] portswitch
    ```
    ```
    [*CE3-GigabitEthernet0/1/1] undo shutdown
    ```
    ```
    [*CE3-GigabitEthernet0/1/1] port link-type trunk
    ```
    ```
    [*CE3-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
    ```
    ```
    [*CE3-GigabitEthernet0/1/1] quit
    ```
    ```
    [*CE3] commit
    ```
12. Verify the configuration.
    
    
    
    After the configuration is complete, run the **display l2tpv3 pw** command to check tunnel status. If **Tunnel State** is displayed as **up**, the L2TPv3 PWs are successfully configured.
    
    ```
    [~PE1] display l2tpv3 pw pwabc
     Tunnel Name                   : pwabc
     Client interface              : GigabitEthernet0/1/1.4 
     Tunnel State                  : up
     Source Interface              : LoopBack2
     Source Address                : 1.1.1.1
     Destination Address           : 3.3.3.3
     Local Session ID              : 4294967295
     Remote Session ID             : 4294967295
    ```
    ```
    [~PE1] display l2tpv3 pw pwabc1
     Tunnel Name                   : pwabc1
     Client interface              : GigabitEthernet0/1/1.4 
     Tunnel State                  : up
     Source Interface              : LoopBack3
     Source Address                : 2.2.2.2
     Destination Address           : 4.4.4.4
     Local Session ID              : 10
     Remote Session ID             : 4294967295
    ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  vlan 2
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0002.00
  #
  interface loopback 2
   ip address 1.1.1.1 32
   isis enable 1
  #
  interface loopback 3
  ip address 2.2.2.2 32
   isis enable 1
  #
  interface gigabitethernet0/2/1
   ip address 192.168.14.1 24
   isis enable 1
  #
  interface gigabitethernet0/3/1
   ip address 192.168.24.1 24
   isis enable 1
  #
  l2tpv3 enable
  #
  l2tpv3 pw pwabc
   source interface LoopBack 2 1.1.1.1
   destination 3.3.3.3
   l2tpv3 local cookie key cipher %#%#1"*U8`%XqIko*T4Kj"}/8.j!Ge-"~KlLv=<!p(!-%#%#
   l2tpv3 remote cookie key cipher %#%#ZM`lUZ0(E$diG3OR%[U&Z_3!GBp>24#caX%uAn^D%#%#
  #
  l2tpv3 pw pwabc1
   l2tpv3 local session-id 10
   source interface LoopBack 3 2.2.2.2
   destination 4.4.4.4
   l2tpv3 local cookie key cipher %#%#uOIwFI,!_<-$&.)+{Lq#zoI.OAoao+c$I3=huT>:%#%#
   l2tpv3 remote cookie key cipher %#%#>nJTCLh0U*#U%jF@i'0LqO}*JZYL]Mq=M($'&}KL%#%#
  #
  interface Gigabitethernet0/1/1.4 mode l2
   encapsulation dot1q vid 2
   rewrite pop single
   l2tpv3 instance a123
    l2tpv3 static binding pw pwabc
  #
  interface Gigabitethernet0/1/0.4 mode l2
   encapsulation default
   l2tpv3 instance a345
    l2tpv3 static binding pw pwabc1
  #
  
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0003.00
  #
  interface loopback 4
   ip address 3.3.3.3 32
   isis enable 1
  #
  interface gigabitethernet0/2/1
   ip address 192.168.14.2 24
   isis enable 1
  #
  l2tpv3 enable
  #
  l2tpv3 pw pwabc
   source interface LoopBack 4 3.3.3.3
   destination 1.1.1.1
   l2tpv3 local cookie key cipher %#%#M;2^%B|jX,Ss!DM\]dc:Y45_!URg>4M2/058ub+=%#%#
   l2tpv3 remote cookie key cipher %#%#8u.iEnZN^1Xj`ZS@S|@55%.3LN3=r)I_o{W~R8V"%#%#
  #
  interface GigabitEthernet0/1/1.4 mode l2
   encapsulation dot1q vid 2
   rewrite pop single
   l2tpv3 instance a234
    l2tpv3 static binding pw pwabc
  #
  
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0004.00
  #
  interface loopback 5
   ip address 4.4.4.4 32
   isis enable 1
  #
  interface gigabitethernet0/2/1
   ip address 192.168.24.2 24
   isis enable 1
  #
  l2tpv3 enable
  #
  l2tpv3 pw pwabc1
   l2tpv3 remote session-id 10
   source interface LoopBack 5 4.4.4.4
   destination 2.2.2.2
   l2tpv3 local cookie key cipher %#%#8Hj5Wwpi80&\BuS<)1g1vscEDe\9gX-CVR$rGsYS%#%#
   l2tpv3 remote cookie key cipher %#%#6v3(+'}M%Cn]3'>g\>v$1,h`LfZ'AV,JoI.-%I,Q%#%#
  #
  interface Gigabitethernet0/1/1.4 mode l2
   encapsulation default
   l2tpv3 instance a456
    l2tpv3 static binding pw pwabc1
  #
  
  ```
* CE3 configuration file
  
  ```
  #
  sysname CE3
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
  #
  return
  ```