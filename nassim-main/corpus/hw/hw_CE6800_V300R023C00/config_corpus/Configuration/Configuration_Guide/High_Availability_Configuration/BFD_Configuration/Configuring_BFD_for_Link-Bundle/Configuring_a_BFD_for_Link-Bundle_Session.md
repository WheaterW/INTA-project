Configuring a BFD for Link-Bundle Session
=========================================

Configuring a BFD for Link-Bundle Session

#### Prerequisites

Before configuring a BFD for link-bundle session to monitor Layer 3 Eth-Trunk member links, you have completed the following tasks:

* Configure a Layer 3 Eth-Trunk interface and ensure that the link layer protocol on the interface is up.
* Assign an IP address to the Layer 3 Eth-Trunk interface and ensure that the Layer 3 protocol on the interface is up.

#### Procedure

1. Enable BFD globally.
   1. Enter the system view.
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enable BFD globally and enter the global BFD view.
      ```
      [bfd](cmdqueryname=bfd)
      ```
      
      You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable BFD globally.
2. Configure a BFD for link-bundle session to monitor the Eth-Trunk link.
   * Configure a BFD for link-bundle session to monitor the IPv4 Eth-Trunk link.
     1. Enter the system view.
        ```
        [system-view](cmdqueryname=system-view)
        ```
     2. Create a BFD for link-bundle session.
        ```
        [bfd](cmdqueryname=bfd) session-name bind link-bundle [ compatible-mode ] peer-ip ip-address [ vpn-instance vpn-name ] interface interface-type interface-number source-ip ip-address [ [unshared-mode](cmdqueryname=unshared-mode) ]
        ```
        ![](public_sys-resources/note_3.0-en-us.png) 
        + The peer IPv4 address of a BFD for link-bundle session must be the IPv4 address of the peer Layer 3 Eth-Trunk interface.
        + You must specify the source IPv4 address for a BFD for link-bundle session. This address is the IPv4 address of the local Layer 3 Eth-Trunk interface.
        + If **unshared-mode** is specified, the BFD for link-bundle session and the dynamic session for detecting the same link are independent of each other.
        + If **unshared-mode** is not specified, the BFD for link-bundle session shares resources with the dynamic session that detects the same link.
     3. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
   * Configure a BFD for link-bundle session to monitor the IPv6 Eth-Trunk link.![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low-latency mode does not support IPv6 functions.
     
     1. Enter the system view.
        ```
        [system-view](cmdqueryname=system-view)
        ```
     2. Create a BFD for link-bundle session.
        ```
        [bfd](cmdqueryname=bfd) session-name bind link-bundle [ compatible-mode ] peer-ipv6 ipv6-address [ vpn-instance vpn-name ] interface interface-type interface-number source-ipv6 ipv6-address [unshared-mode](cmdqueryname=unshared-mode)
        ```
        + If **unshared-mode** is specified, the BFD for link-bundle session and the dynamic session for detecting the same link are independent of each other.
        + If **unshared-mode** is not specified, the BFD for link-bundle session shares resources with the dynamic session that detects the same link.![](public_sys-resources/note_3.0-en-us.png) 
        + The peer IPv6 address of a BFD for link-bundle session must be the IPv6 address of the peer Layer 3 Eth-Trunk interface.
        + You must specify the source IPv6 address for a BFD for link-bundle session. This address is the IPv6 address of the local Layer 3 Eth-Trunk interface.
     3. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```

#### Verifying the Configuration

Run the [**display bfd link-bundle session**](cmdqueryname=display+bfd+link-bundle+session) [ **interface** *interface-type* *interface-number* ] command to check information about all BFD for link-bundle sessions or a specific one.