Overview of HTTPS
=================

Overview of HTTPS

#### Definition

The Hypertext Transfer Protocol (HTTP) is an application-layer protocol that transfers hypertext from WWW servers to local browsers. This protocol transmits a variety of data, such as web pages, based on the TCP/IP protocol, and uses a client-server model in which requests and responses are exchanged.

Hypertext Transfer Protocol Secure (HTTPS) is an HTTP protocol that runs on top of Secure Sockets Layer (SSL) for secure transactions.


#### Purpose

The HTTP function provides a unified interface for users and features that use the HTTP protocol to transmit data. HTTP, however, does not have any security mechanisms; it transmits data in clear text and does not authenticate either communication party. Therefore, data transmitted over such a protocol is vulnerable to tampering, sacrificing transmission security. To overcome this, HTTPS establishes an SSL encryption layer on HTTP, and is therefore more secure. HTTPS improves device security in the following ways:

* The data exchanged between a client and a server is encrypted to ensure data security and integrity, implementing secure device management.
* Certificate-based authentication is performed on a server and a client.
* The message authentication code (MAC) algorithm is used to verify message integrity during message transmission.

The HTTPS client function is required when:

* The configuration data of a specified YANG file is loaded from an HTTPS server to a configuration database through HTTPS in a Network Configuration Protocol (NETCONF) scenario.