Example for Filtering the Routes to Be Received and Advertised
==============================================================

Filters can be applied to the routes to be received and advertised based on networking requirements.

#### Networking Requirements

On the OSPF network shown in [Figure 1](#EN-US_TASK_0172366589__fig173341440154413), DeviceA receives routes from the Internet and provides some of the Internet routes for DeviceB. It is required that DeviceA provide only routes 172.16.17.0/24, 172.16.18.0/24, and 172.16.19.0/24 to DeviceB, DeviceC accept only 172.16.18.0/24, and that DeviceD accept all the routes provided by DeviceB.

**Figure 1** Network diagram of filtering routes to be received and advertised![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0000001410717820.png)

#### Precautions

During the configuration, pay attention to the following points:

* When configuring an IP prefix list, you need to specify the IP prefix range as required.
* The name of the IP prefix list to be referenced is case-sensitive.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions on DeviceA, DeviceB, DeviceC, and DeviceD.
2. Configure static routes on DeviceA and import them to the OSPF routing table.
3. Configure an export policy on DeviceA and check the filtering result on DeviceB.
4. Configure an import policy on DeviceC and check the filtering result on DeviceC.

#### Data Preparation

To complete the configuration, you need the following data:

* Five static routes imported by DeviceA
* OSPF backbone area (area 0) where DeviceA, DeviceB, DeviceC, and DeviceD reside
* Name of the IP prefix list, which is used to filter routes

#### Procedure

1. Assign an IP address to each interface.
2. Configure OSPF.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceA-ospf-1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospf
   ```
   ```
   [*DeviceC-ospf-1] area 0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceC-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceC-ospf-1] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] ospf
   ```
   ```
   [*DeviceD-ospf-1] area 0
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceD-ospf-1-area-0.0.0.0] quit
   ```
3. Configure five static routes on DeviceA and import them to the OSPF routing table.
   
   
   ```
   [~DeviceA] ip route-static 172.16.16.0 24 NULL0
   ```
   ```
   [*DeviceA] ip route-static 172.16.17.0 24 NULL0
   ```
   ```
   [*DeviceA] ip route-static 172.16.18.0 24 NULL0
   ```
   ```
   [*DeviceA] ip route-static 172.16.19.0 24 NULL0
   ```
   ```
   [*DeviceA] ip route-static 172.16.20.0 24 NULL0
   ```
   ```
   [*DeviceA] ospf
   ```
   ```
   [*DeviceA-ospf-1] import-route static
   ```
   ```
   [*DeviceA-ospf-1] commit
   ```
   ```
   [~DeviceA-ospf-1] quit
   ```
   
   # Check the IP routing table on DeviceB. The command output shows the five static routes imported by OSPF.
   
   ```
   [~DeviceB] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : Public
            Destinations : 22       Routes : 22
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
           1.1.1.1/32  Direct 0    0             D  127.0.0.1       LoopBack1
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
      172.16.16.0/24  O_ASE  150  1             D  192.168.1.1     GigabitEthernet0/1/0
      172.16.17.0/24  O_ASE  150  1             D  192.168.1.1     GigabitEthernet0/1/0
      172.16.18.0/24  O_ASE  150  1             D  192.168.1.1     GigabitEthernet0/1/0
      172.16.19.0/24  O_ASE  150  1             D  192.168.1.1     GigabitEthernet0/1/0
      172.16.20.0/24  O_ASE  150  1             D  192.168.1.1     GigabitEthernet0/1/0
       192.168.1.0/24  Direct 0    0             D  192.168.1.2     GigabitEthernet0/1/0
       192.168.1.1/32  Direct 0    0             D  192.168.1.1     GigabitEthernet0/1/0
       192.168.1.2/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
     192.168.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
       192.168.2.0/24  Direct 0    0             D  192.168.2.1     GigabitEthernet0/3/0
       192.168.2.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/3/0
       192.168.2.2/32  Direct 0    0             D  192.168.2.2     GigabitEthernet0/3/0
     192.168.2.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/3/0
       192.168.3.0/24  Direct 0    0             D  192.168.3.1     GigabitEthernet0/2/0
       192.168.3.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
       192.168.3.2/32  Direct 0    0             D  192.168.3.2     GigabitEthernet0/2/0
     192.168.3.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
   ```
4. Configure an export policy to filter routes to be advertised.
   
   
   
   # Configure an IP prefix list named **a2b** on DeviceA.
   
   ```
   [~DeviceA] ip ip-prefix a2b index 10 permit 172.16.17.0 24
   ```
   ```
   [*DeviceA] ip ip-prefix a2b index 20 permit 172.16.18.0 24
   ```
   ```
   [*DeviceA] ip ip-prefix a2b index 30 permit 172.16.19.0 24
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure an export policy that is based on the IP prefix list **a2b** on DeviceA.
   
   ```
   [~DeviceA] ospf
   ```
   ```
   [*DeviceA-ospf-1] filter-policy ip-prefix a2b export static
   ```
   ```
   [*DeviceA-ospf-1] commit
   ```
   ```
   [~DeviceA-ospf-1] quit
   ```
   
   # Check the IP routing table on DeviceB. The command output shows that DeviceB accepted only the three routes defined in IP prefix list **a2b**.
   
   ```
   [~DeviceB] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : Public
            Destinations : 20       Routes : 20
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
           1.1.1.1/32  Direct 0    0             D  127.0.0.1       LoopBack1
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
      172.16.17.0/24  O_ASE  150  1             D  192.168.1.1     GigabitEthernet0/1/0
      172.16.18.0/24  O_ASE  150  1             D  192.168.1.1     GigabitEthernet0/1/0
      172.16.19.0/24  O_ASE  150  1             D  192.168.1.1     GigabitEthernet0/1/0
       192.168.1.0/24  Direct 0    0             D  192.168.1.2     GigabitEthernet0/1/0
       192.168.1.1/32  Direct 0    0             D  192.168.1.1     GigabitEthernet0/1/0
       192.168.1.2/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
     192.168.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
       192.168.2.0/24  Direct 0    0             D  192.168.2.1     GigabitEthernet0/3/0
       192.168.2.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/3/0
       192.168.2.2/32  Direct 0    0             D  192.168.2.2     GigabitEthernet0/3/0
     192.168.2.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/3/0
       192.168.3.0/24  Direct 0    0             D  192.168.3.1     GigabitEthernet0/2/0
       192.168.3.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
       192.168.3.2/32  Direct 0    0             D  192.168.3.2     GigabitEthernet0/2/0
     192.168.3.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
   ```
5. Configure an import policy.
   
   
   
   # Configure an IP prefix list named **in** on DeviceC.
   
   ```
   [~DeviceC] ip ip-prefix in index 10 permit 172.16.18.0 24
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure an import policy that is based on the IP prefix list **in** on DeviceC.
   
   ```
   [~DeviceC] ospf
   ```
   ```
   [*DeviceC-ospf-1] filter-policy ip-prefix in import
   ```
   ```
   [*DeviceC-ospf-1] commit
   ```
   
   # Check the IP routing table on DeviceC. The command output shows that DeviceC accepted only one route (the one matching IP prefix list **in**).
   
   ```
   [~DeviceC] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : Public
            Destinations : 12       Routes : 12
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
           1.1.1.1/32  O_ASE  10   1             D  192.168.2.1     GigabitEthernet0/1/0
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
      172.16.18.0/24  O_ASE  150  1             D  192.168.2.1     GigabitEthernet0/1/0
       192.168.1.0/24  O_ASE  10   2             D  192.168.2.1     GigabitEthernet0/1/0
       192.168.2.0/24  Direct 0    0             D  192.168.2.2     GigabitEthernet0/1/0
       192.168.2.1/32  Direct 0    0             D  192.168.2.1     GigabitEthernet0/1/0
       192.168.2.2/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
     192.168.2.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
       192.168.3.0/24  O_ASE  10   2             D  192.168.2.1     GigabitEthernet0/1/0
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   filter-policy ip-prefix a2b export static
  ```
  ```
   import-route static
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ip ip-prefix a2b index 10 permit 172.16.17.0 24
  ```
  ```
  ip ip-prefix a2b index 20 permit 172.16.18.0 24
  ```
  ```
  ip ip-prefix a2b index 30 permit 172.16.19.0 24
  ```
  ```
  #
  ```
  ```
  ip route-static 172.16.16.0 255.255.255.0 NULL0
  ```
  ```
  ip route-static 172.16.17.0 255.255.255.0 NULL0
  ```
  ```
  ip route-static 172.16.18.0 255.255.255.0 NULL0
  ```
  ```
  ip route-static 172.16.19.0 255.255.255.0 NULL0
  ```
  ```
  ip route-static 172.16.20.0 255.255.255.0 NULL0
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.3.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
    network 192.168.3.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   filter-policy ip-prefix in import
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  ip ip-prefix in index 10 permit 172.16.18.0 24
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.3.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.3.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```