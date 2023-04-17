# NetworkTools - tool for easy switching network card mode between DHCP and static

NetworkTools is a tool created for IT teams that need an easy way to switch network card mode between DHCP and static and store IP addresses, MAC addresses, and host names in a Google Sheets file.

## How it works

NetworkTools uses a simple GUI that allows the user to easily switch the network card mode between DHCP and static. The tool automatically scans the network for available IP addresses.

After configuring the network interface, NetworkTools automatically adds the IP address, MAC address, and host name to the Google Sheets file.

The NetworkTools server runs in the background and allows clients to connect to it using a socket connection. The server processes client requests and saves IP addresses, MAC addresses, and host names to the Google Sheets file.

## Requirements

To use the NetworkTools tool, you need a Windows operating system and Python version 3.6 or higher.

## How to install and run

1. Clone the NetworkTools repository from GitHub.


2. Set the configuration values in the `config.py` file.

4. Create a `credentials.json` file that allows the tool to access the Google Sheets file.

5. Start the server using the command `python socketserver.py`.

6. Run the client program by double-clicking the `client.exe` file.

## How to use

1. Run the client program by double-clicking the `client.exe` file.
2. Select the network card mode - Dynamic or Static.
3. Enter the host name and click the "Save" button.
4. The IP address, MAC address, and host name will be saved to the Google Sheets file.

## How to configure the Google Sheets connection

1. Create a `credentials.json` file that allows the tool to access the Google Sheets file.
