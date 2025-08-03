Example for Configuring a POS-Trunk Interface
=============================================

To implement linear multiplex section protection (LMSP), add POS interfaces to an LMSP group, configure them as working and protection interfaces in the group, and then add them to a POS-Trunk interface.

#### Networking Requirements

It is required that a POS-Trunk logical link be established between DeviceA and DeviceB.

**Figure 1** Networking diagram for configuring a POS-Trunk interface![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent POS0/1/0 and POS0/2/0, respectively.


  
![](figure/en-us_image_0000001163461636.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Connect DeviceA and DeviceB through POS interfaces.
2. Create a POS-Trunk interface.
3. Add the POS interfaces to an LMSP group and configure them as working and protection interfaces in the group. In addition, specify a working mode for the protection interface.
4. Add the POS interfaces to the POS-Trunk interface.

#### Data Preparation

To complete the configuration, you need the following data:

* DeviceA-side IP address of the POS-Trunk interface
* DeviceB-side IP address of the POS-Trunk interface

#### Procedure

1. Configure DeviceA.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   
   # Create a POS-Trunk interface and configure an IP address for it.
   
   ```
   [~DeviceA] interface pos-trunk1
   ```
   ```
   [*DeviceA-Pos-Trunk1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-Pos-Trunk1] undo shutdown
   ```
   ```
   [*DeviceA-Pos-Trunk1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Add POS0/1/0 and POS0/2/0 to an LMSP group and configure them as working and protection interfaces, respectively.
   
   ```
   [~DeviceA] interface pos0/1/0
   ```
   ```
   [~DeviceA-Pos0/1/0] link-protocol ppp
   ```
   ```
   [*DeviceA-Pos0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-Pos0/1/0] aps group 1
   ```
   ```
   [*DeviceA-Pos0/1/0] aps working
   ```
   ```
   [*DeviceA-Pos0/1/0] quit
   ```
   ```
   [*DeviceA] interface pos0/2/0
   ```
   ```
   [~DeviceA-Pos0/2/0] link-protocol ppp
   ```
   ```
   [*DeviceA-Pos0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-Pos0/2/0] aps group 1
   ```
   ```
   [*DeviceA-Pos0/2/0] aps protect
   ```
   ```
   [*DeviceA-Pos0/2/0] aps mode one-plus-one unidirection
   ```
   ```
   [*DeviceA-Pos0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Add POS0/1/0 and POS0/2/0 to POS-Trunk1.
   
   ```
   [~DeviceA] interface pos0/1/0
   ```
   ```
   [~DeviceA-Pos0/1/0] pos-trunk 1
   ```
   ```
   [*DeviceA-Pos0/1/0] quit
   ```
   ```
   [*DeviceA] interface pos0/2/0
   ```
   ```
   [~DeviceA-Pos0/2/0] pos-trunk 1
   ```
   ```
   [*DeviceA-Pos0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure DeviceB.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [*HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   
   # Create a POS-Trunk interface and configure an IP address for it.
   
   ```
   [~DeviceB] interface pos-trunk1
   ```
   ```
   [*DeviceB-Pos-Trunk1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*DeviceB-Pos-Trunk1] undo shutdown
   ```
   ```
   [*DeviceB-Pos-Trunk1] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Add POS0/1/0 and POS0/2/0 to an LMSP group and configure them as working and protection interfaces, respectively.
   
   ```
   [~DeviceB] interface pos0/1/0
   ```
   ```
   [~DeviceBâPos0/1/0] link-protocol ppp
   ```
   ```
   [*DeviceBâPos0/1/0] undo shutdown
   ```
   ```
   [*DeviceBâPos0/1/0] aps group 1
   ```
   ```
   [*DeviceBâPos0/1/0] aps working
   ```
   ```
   [*DeviceBâPos0/1/0] quit
   ```
   ```
   [*DeviceB] interface pos0/2/0
   ```
   ```
   [~DeviceBâPos0/2/0] link-protocol ppp
   ```
   ```
   [*DeviceBâPos0/2/0] undo shutdown
   ```
   ```
   [*DeviceBâPos0/2/0] aps group 1
   ```
   ```
   [*DeviceBâPos0/2/0] aps protect
   ```
   ```
   [*DeviceBâPos0/2/0] aps mode one-plus-one unidirection
   ```
   ```
   [*DeviceBâPos0/2/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Add POS0/1/0 and POS0/2/0 to POS-Trunk1.
   
   ```
   [~DeviceB] interface pos0/1/0
   ```
   ```
   [*DeviceBâPos0/1/0] pos-trunk 1
   ```
   ```
   [*DeviceBâPos0/1/0] quit
   ```
   ```
   [*DeviceB] interface pos0/2/0
   ```
   ```
   [*DeviceBâPos0/2/0] pos-trunk 1
   ```
   ```
   [*DeviceBâPos0/2/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
3. Verify the configuration.
   
   
   
   Run the [**display aps group**](cmdqueryname=display+aps+group) command on DeviceA or DeviceB to check the LMSP group configuration.
   
   The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display aps group 1
   ```
   ```
   APS Group  1: Pos0/1/0 working channel 1(Active)
                 Pos0/2/0 protection channel 0(Inactive)
                 Unidirection, 1+1 mode, No Revert mode
                 No Request on Both Working and Protection Side
   
   ------------------------------------------------------------------------
   Group Work-Channel Protect-Channel Wtr W-State P-State Switch-Cmd Switch-Result
   ------------------------------------------------------------------------
   1     Pos0/1/0      Pos0/2/0       NA    ok      ok         NA          idle
   ------------------------------------------------------------------------
   total entry: 1
   ```
   
   Run the [**display pos-trunk**](cmdqueryname=display+pos-trunk) command on DeviceA or DeviceB. The command output shows that the interface state is **Up**.
   
   The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display pos-trunk 1
   ```
   ```
   Interface Pos-Trunk1's state information is:
   Operate status: up     Number Of Up Port In Trunk: 2
   --------------------------------------------------------------------------------
   PortName    Status    Active Status
   Pos0/1/0    Up        Active
   Pos0/2/0    Up        Inactive 
   ```
   
   Check that DeviceA and DeviceB can successfully ping each other through the POS-Trunk interface.
   
   ```
   [~DeviceA] ping -a 10.1.1.1 10.1.1.2
   ```
   ```
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=62 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=62 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=62 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=62 ms
   ```
   ```
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=62 ms
   ```
   ```
     --- 10.1.1.2 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 62/62/62 ms
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
  interface Pos-Trunk1
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface Pos0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   aps group 1
  ```
  ```
   aps working
  ```
  ```
   pos-trunk 1
  ```
  ```
  #
  ```
  ```
  interface Pos0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   aps group 1
  ```
  ```
   aps protect
  ```
  ```
   aps mode one-plus-one unidirection
  ```
  ```
   pos-trunk 1
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
  interface Pos-Trunk1
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface Pos0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   aps group 1
  ```
  ```
   aps working
  ```
  ```
   pos-trunk 1
  ```
  ```
  #
  ```
  ```
  interface Pos0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   link-protocol ppp
  ```
  ```
   aps group 1
  ```
  ```
   aps protect
  ```
  ```
   aps mode one-plus-one unidirection
  ```
  ```
   pos-trunk 1
  ```
  ```
  #
  ```
  ```
  return
  ```