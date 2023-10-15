# uh halp

Install:

```bash
pip install uh-halp
```

Usage:

```bash
$ uh check my syslog
tail -f /var/log/syslog

$ uh clean up docker disk space
docker system prune -a

$ uh sync this shit to /home/gaz/project on gaz@server
rsync -avz --progress . gaz@server:/home/gaz/project

$ uh how much space have I got free here?
df -h .

$ uh gimme a socks proxy on 192.168.0.1
ssh -D 8080 username@192.168.0.1

$ uh check if the internet is up
ping -c 3 google.com

$ uh make beeping noises forever
while true; do echo -e "\a"; done

$ uh fork bomb this terminal
:(){ :|:& };:
```

## Restrictions

OpenAI are bawbags. Expect crying if you ask it to do anything naughty or
swear at it.
