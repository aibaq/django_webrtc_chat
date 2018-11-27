Django WebRTC Video chat example
==============

## Tags
django|django-channels|django-webrtc|signalling server|webrtc|django video chat

## Installation
```
git clone https://github.com/aibaq/django_webrtc_chat
cd django_webrtc_chat
pip install -r requirements.txt
```

## Run
```
daphne -e ssl:8000:privateKey=key.pem:certKey=cert.pem django_webrtc_chat.asgi:application
https://localhost:8000/core/room_name/
```

## TLS
Some browsers require HTTPS to allow Camera access, thus self-signed certificates are provided in this example.
To obtain a new certificate, run:
```
./generate_cert.sh
```

## NAT
When p2p connection cannot be established because of NAT, turn server is required. The following url-s provide a good example how to run a turn server
[https://en.maateen.me/install-turn-server-in-ubuntu/]
[https://github.com/coturn/coturn/wiki/CoturnConfig]
```
'iceServers': [
  {'urls': 'stun:stun.stunprotocol.org:3478'},
  {
    'urls': `turn:turn_server_host`,
    'username': 'turn_server_username',
    'credential': 'turn_server_password'
  }
]
```

## Original
This repository is django implementation of [https://github.com/shanet/WebRTC-Example]

## License

The MIT License (MIT)

Copyright (c) 2018 Aibek Prenov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
