#based on a post from here
# https://www.learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/

import socket
import logging
import threading
import queue
import re
import json


class ChatHandler (threading.Thread):
    def __init__(self, actions:queue,twitch_connection_info_filepath):
        threading.Thread.__init__(self)
        self.actions = actions
        self.twitch_connection_info_filepath = twitch_connection_info_filepath

    def run(self):
        twitch_info = json.loads(self.twitch_connection_info_filepath)

        server = twitch_info["server"]
        port = twitch_info["port"]
        nickname = twitch_info["nickname"]
        token = twitch_info["token"]
        channel = twitch_info["channel"]

        sock = socket.socket()
        sock.connect((server, port))
        sock.send(f"PASS {token}\n".encode('utf-8'))
        sock.send(f"NICK {nickname}\n".encode('utf-8'))
        sock.send(f"JOIN {channel}\n".encode('utf-8'))
        resp = sock.recv(2048).decode('utf-8')


        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s — %(message)s',
                            datefmt='%Y-%m-%d_%H:%M:%S',
                            handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

        logging.info(resp)

        while True:
            resp = sock.recv(2048).decode('utf-8')

            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))


            elif len(resp) > 0:
                lines = resp.split("\r\n")
                for line in lines:
                    logging.info(line)
                    if not line:
                        continue
                    try:
                        # print(line)
                        username_message = line.split('—')[1:]
                        if len(username_message) == 0:
                            username_message = line.split('-')[0:]
                        # print(username_message)
                        username_message = '—'.join(username_message).strip()
                        username, channel, message = re.search(':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)',
                                                               username_message).groups()
                        logging.info(f"username: {username}, channel: {channel}, message: {message}")
                        # print(message)
                        self.actions.put(message)
                    except Exception as e:
                        logging.error(e)
