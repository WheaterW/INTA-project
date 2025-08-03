Example for Configuring DHCPv4 Relay
====================================

Example for Configuring DHCPv4 Relay

#### Context

As shown in [Figure 1](#EN-US_TASK_0000001564126237__fig143192110535), the DHCPv4 server and clients are on different network segments. A DHCPv4 relay agent must be configured to enable the DHCPv4 clients to dynamically obtain IPv4 addresses.

**Figure 1** Network diagram of configuring a DHCPv4 relay agent![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001564006461.png)

#### Procedure

1. Configure connectivity between devices.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 100 200
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type hybrid
   [*DeviceA-100GE1/0/1] port hybrid pvid vlan 200
   [*DeviceA-100GE1/0/1] port hybrid untagged vlan 200
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type hybrid
   [*DeviceA-100GE1/0/2] port hybrid pvid vlan 100
   [*DeviceA-100GE1/0/2] port hybrid untagged vlan 100
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface vlanif 200
   [*DeviceA-Vlanif200] ip address 10.10.20.1 24
   [*DeviceA-Vlanif200] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceB] vlan batch 200
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type hybrid
   [*DeviceB-100GE1/0/1] port hybrid pvid vlan 200
   [*DeviceB-100GE1/0/1] port hybrid untagged vlan 200
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface vlanif 200
   [*DeviceB-Vlanif200] ip address 10.10.20.2 24
   [*DeviceB-Vlanif200] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   ```
2. Configure DHCPv4 relay.
   
   
   
   # Enable DHCPv4 relay on DeviceA's VLANIF 100 and configure an IPv4 address for the DHCPv4 server.
   
   ```
   [~DeviceA] dhcp enable
   [*DeviceA] interface vlanif 100
   [*DeviceA-Vlanif100] ip address 10.20.20.1 24
   [*DeviceA-Vlanif100] dhcp select relay 
   [*DeviceA-Vlanif100] dhcp relay server-ip 10.10.20.2
   [*DeviceA-Vlanif100] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure the DHCPv4 server.
   
   
   
   # Configure the DHCPv4 server function based on the global address pool on DeviceB.
   
   ```
   [~DeviceB] dhcp enable
   [*DeviceB] interface vlanif 200
   [*DeviceB-Vlanif200] dhcp select global
   [*DeviceB-Vlanif200] quit
   [*DeviceB] ip pool pool1
   [*DeviceB-ip-pool-pool1] network 10.20.20.0 mask 24
   [*DeviceB-ip-pool-pool1] gateway-list 10.20.20.1
   [*DeviceB-ip-pool-pool1] option121 ip-address 10.10.20.0 24 10.20.20.1
   [*DeviceB-ip-pool-pool1] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   ```
4. Configure routes.
   
   
   
   # Configure a default route on DeviceA.
   
   
   
   ```
   [~DeviceA] ip route-static 0.0.0.0 0.0.0.0 10.10.20.2
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure a static route on DeviceB.
   
   ```
   [~DeviceB] ip route-static 10.20.20.0 255.255.255.0 10.10.20.1
   [*DeviceB] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# Run the **display dhcp relay interface vlanif 100** command on DeviceA to check the configuration of the DHCPv4 relay agent.

```
[~DeviceA] display dhcp relay interface vlanif 100
 Server IP address [00] : 10.10.20.2                                                                                                
 Gateway address in use : 10.20.20.1                                                                                                
 Gateway switch         : Disable                                                                                                   

```

# Check IPv4 address information on DHCPv4 clients to confirm that they have obtained IPv4 addresses.

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 100 200
  #
  dhcp enable
  #
  interface Vlanif100
   ip address 10.20.20.1 255.255.255.0
   dhcp select relay
   dhcp relay server-ip 10.10.20.2
  #
  interface Vlanif200
   ip address 10.10.20.1 255.255.255.0
  #
  interface 100GE1/0/1
   port link-type hybrid
   port hybrid pvid vlan 200
   port hybrid untagged vlan 200
  #
  interface 100GE1/0/2
   port link-type hybrid
   port hybrid pvid vlan 100
   port hybrid untagged vlan 100
  #
  ip route-static 0.0.0.0 0.0.0.0 10.10.20.2
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 200
  #
  dhcp enable
  #
  ip pool pool1
   gateway-list 10.20.20.1
   network 10.20.20.0 mask 255.255.255.0
   option121 ip-address 10.10.20.0 24 10.20.20.1
  #
  interface Vlanif200
   ip address 10.10.20.2 255.255.255.0
   dhcp select global
  #
  interface 100GE1/0/1
   port link-type hybrid
   port hybrid pvid vlan 200
   port hybrid untagged vlan 200
  #
  ip route-static 10.20.20.0 255.255.255.0 10.10.20.1
  #
  return
  ```