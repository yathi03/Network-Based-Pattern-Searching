# Network-Based-Pattern-Searching
Searching in Python
This project demonstrates a network-based pattern searching system using Python. It includes a server, a client, and a search script to find a specific word in a text file.

Project Structure
server.py: The server script that listens for incoming client connections.
client.py: The client script that connects to the server and sends the word to be searched.
search.py: The search script that performs the pattern search in the text file.
data.txt: The text file in which the word will be searched.
How It Works
Server: The server script (server.py) runs and waits for client connections.
Client: The client script (client.py) connects to the server and sends the word to be searched.
Search: The server receives the word and invokes the search script (search.py) to search for the word in data.txt.
Output: The search script returns the result to the server, which then sends it back to the client.
Getting Started
Prerequisites
Python 3.x installed on your machine.
Running the Project
Start the Server:
python server.py

Run the Client:
python client.py <word_to_search>

Replace <word_to_search> with the word you want to search in data.txt.
Example
Start the server:
python server.py

In another terminal, run the client with the word to search:
python client.py example

If the word “example” is found in data.txt, the server will return the result to the client.
Files
server.py: Handles client connections and coordinates the search.
client.py: Sends the search word to the server.
search.py: Searches for the word in data.txt and returns the result.
data.txt: The text file containing the data to be searched.
