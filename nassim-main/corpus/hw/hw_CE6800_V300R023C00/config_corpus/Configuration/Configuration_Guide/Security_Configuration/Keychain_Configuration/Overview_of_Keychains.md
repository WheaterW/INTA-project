Overview of Keychains
=====================

Overview of Keychains

#### Definition

A keychain, as its name implies, is a chain of keys used to open the encryption lock that is constantly changed by an application.

A key in a keychain is not an algorithm or a key string; rather, it is a set of encryption and authentication rules. A keychain centrally controls and flexibly manages a series of its own keys to provide dynamic security authentication services for applications.


#### Purpose

Before an application that runs a routing protocol (for example, RIP, IS-IS, OSPF, or BGP) establishes a session with the peer end, it needs to set up a transport-layer connection.

To ensure the security of an application's session connections and exchanged data, MD5 can be used to authenticate packets; however, this has the following disadvantages:

* The MD5 algorithm is relatively simple and cannot meet high security requirements of networks.
* MD5 keys must be manually updated at intervals to ensure key security. MD5 algorithms and keys are configured in applications, and are statically bound to applications in one-to-one mappings. Therefore, you need to manually update the keys configured on the applications of the devices at both ends one by one.

To eliminate these disadvantages, a keychain for application authentication is introduced:

* In each key of a keychain, an algorithm that is more secure than MD5 can be selected. In the future, more highly secure algorithms will be available.
* Each key in a keychain has an independent algorithm, key string, and lifetime. Applications on devices at both ends use keychain authentication; that is, they need to match multiple keys. Therefore, the authentication algorithms and key strings can be automatically and periodically updated on multiple applications of the devices at both ends based on the lifetimes of the keys.
* When keys in a keychain are dynamically updated, the transport-layer connections in use do not need to be disconnected and reconnected, maintaining the stability of session connections and service continuity.